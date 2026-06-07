# 📓 NoteBot — AI-Powered Notes Assistant

A **NotebookLM-style RAG (Retrieval-Augmented Generation)** application that lets you upload your notes as a PDF and ask questions about them. Built with LangChain, Google Gemini, FAISS, and Streamlit.

---

## 🚀 Live Demo
👉 [Try NoteBot Live](https://your-app-link.streamlit.app) ← *(update after deployment)*

---

## 🧠 How It Works

```
PDF Upload → Text Extraction → Chunking → Embeddings → FAISS Vector Store
                                                                  ↓
User Query → Semantic Search → Relevant Chunks → Gemini LLM → Answer
```

1. Upload any PDF (lecture notes, textbooks, documents)
2. PDF is split into chunks and embedded using Google Gemini Embeddings
3. Chunks are stored in a FAISS vector store
4. When you ask a question, the most relevant chunks are retrieved
5. Gemini LLM generates an answer based strictly on your notes

---

## ✨ Features

- 📄 Upload PDF notes and get instant answers
- 🔍 Semantic search using FAISS vector database
- 🤖 Powered by Google Gemini LLM
- 💾 Session-based caching — PDF is processed only once
- ⚠️ Rate limit handling with auto-retry
- 🚫 Answers only from your notes — no hallucination

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| LLM | Google Gemini 1.5 Flash |
| Embeddings | Google Gemini Embedding 001 |
| Vector Store | FAISS |
| Framework | LangChain |
| Language | Python 3.11+ |

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Siidu-Nhavi/notebot.git
cd notebot
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up API Key
Create a `.env` file in the root folder:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```
Get your free API key from 👉 [aistudio.google.com](https://aistudio.google.com)

### 5. Run the app
```bash
streamlit run chatBot.py
```

Open your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
notebot/
│
├── chatBot.py          # Main Streamlit application 
├── .env                # API keys (not pushed to GitHub)
├── .gitignore          # Git ignore file
└── README.md           # Project documentation
```

---

## 🔑 Environment Variables

| Variable | Description |
| `GOOGLE_API_KEY` | Your Google Gemini API Key from AI Studio |

---

## 📸 Screenshot

> <img width="1920" height="880" alt="Screenshot (203)" src="https://github.com/user-attachments/assets/787e2eec-878a-4fa6-a581-ec4b29ae256f" />

---

## 🎯 Use Cases

- 📚 Ask questions about your college lecture notes
- 📖 Query textbook chapters instantly
- 🗒️ Search through research papers
- 📋 Get answers from any PDF document

---

## 🔮 Future Improvements

- [ ] Support for multiple PDF uploads
- [ ] Chat history / conversation memory
- [ ] Support for TXT, DOCX file formats
- [ ] Better UI with dark mode
- [ ] Deploy on GCP Cloud Run

---

## 👨‍💻 Author

Siddu Nhavi — Aspiring ML Engineer  
B.Tech CSE | TKIET, Warananagar  

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
