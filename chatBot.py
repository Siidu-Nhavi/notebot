import os
import time
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

st.header("NoteBot 📓")

with st.sidebar:
    st.title("My Notes")
    file = st.file_uploader("Upload notes PDF", type="pdf")

if file is not None:
    # Reset if new file uploaded
    if "last_file" not in st.session_state or st.session_state.last_file != file.name:
        st.session_state.pop("vector_store", None)
        st.session_state.last_file = file.name

    if "vector_store" not in st.session_state:
        with st.spinner("Processing PDF..."):
            pdf = PdfReader(file)
            text = "".join([page.extract_text() or "" for page in pdf.pages])

            if not text.strip():
                st.error("Could not extract text. PDF may be image-based.")
                st.stop()

            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            chunks = splitter.split_text(text)

            embeddings = GoogleGenerativeAIEmbeddings(
                model="models/gemini-embedding-001",
                google_api_key=GOOGLE_API_KEY
            )
            st.session_state.vector_store = FAISS.from_texts(chunks, embeddings)
            st.success(f"✅ Indexed {len(chunks)} chunks!")

    user_query = st.text_input("Ask a question about your notes")

    if user_query and "vector_store" in st.session_state:
        with st.spinner("Thinking..."):
            matching_chunks = st.session_state.vector_store.similarity_search(user_query, k=4)

            llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash-lite",  # Free tier friendly
                google_api_key=GOOGLE_API_KEY
            )

            prompt = ChatPromptTemplate.from_template("""
            Answer the question based only on the context below.
            If the answer isn't in the context, say "I couldn't find that in your notes."

            Context: {context}
            Question: {input}
            """)

            chain = create_stuff_documents_chain(llm, prompt)
            try:
                response = chain.invoke({  #here invoke method handles the request i.e rate limit
                    "input": user_query,
                    "context": matching_chunks
                })
                st.write(response)
            except Exception as e:
                if "429" in str(e):
                    st.warning("⏳ Rate limit hit. Waiting 30 seconds and retrying...")
                    time.sleep(30)
                    st.rerun()
                else:
                    st.error(f"Error: {str(e)}")

        st.write(response)