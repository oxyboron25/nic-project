# LangChain RAG Chatbot for Document Question-Answering

This is a full-stack Retrieval-Augmented Generation (RAG) chatbot system that allows users to upload documents (PDF, DOCX, HTML), ask natural language questions, and get intelligent answers grounded in the uploaded content. It uses **LangChain**, **OpenAI**, **ChromaDB**, **FastAPI**, and **Streamlit**.

---

## 🚀 Features

- 📤 Upload documents and automatically index them into a vector store
- 💬 Ask questions in a chat interface and get context-aware answers
- 🧠 Uses OpenAI (`gpt-4o`, `gpt-4o-mini`) with LangChain
- 💾 Stores embeddings persistently with ChromaDB
- 🗂️ Stores chat history and document metadata in SQLite
- 🔧 Clean separation of backend (FastAPI) and frontend (Streamlit)

---

## 📂 Project Structure

```

nic-rag-project/
│
├── api/                  # FastAPI backend
│   ├── main.py
│   ├── db\_utils.py
│   ├── chroma\_utils.py
│   ├── langchain\_utils.py
│   └── pydantic\_models.py
│
├── app/                  # Streamlit frontend
│   ├── streamlit\_app.py
│   ├── chat\_interface.py
│   ├── sidebar.py
│   └── api\_utils.py
│
├── docs/                 # Sample test PDFs
│
├── chroma\_db/            # Persistent vector storage (auto-created)
├── rag\_app.db            # SQLite DB for logs and metadata (auto-created)
├── requirements.txt
└── .env                  # OpenAI API key (not committed)

````

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/nic-rag-project.git
cd nic-rag-project
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file

Create a file called `.env` in the root with:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🔧 Running the App

### Step 1: Start the FastAPI backend

```bash
cd api
uvicorn main:app --reload --port 8000
```

Visit the Swagger API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Step 2: Start the Streamlit frontend (in a new terminal)

```bash
cd app
streamlit run streamlit_app.py
```

Visit [http://localhost:8501](http://localhost:8501) to interact with the chatbot UI.

---

## 🧪 Example Use Case

1. Upload `svamitva-test.pdf` via the sidebar
2. Ask: *"What is the SVAMITVA scheme?"*
3. Get a grounded response sourced from the document

---

## 📌 Notes

* Uploaded documents are embedded and stored in `./chroma_db/`
* You do **not need to re-upload** them after restarting the app
* Documents and chat logs are stored in `rag_app.db` (SQLite)
* Deleting a document via UI removes it from both Chroma and the DB

---

## 🧱 Built With

* [LangChain](https://www.langchain.com/)
* [OpenAI](https://openai.com/)
* [ChromaDB](https://www.trychroma.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Streamlit](https://streamlit.io/)
* [SQLite](https://sqlite.org/)

---

## 📝 License

This project is licensed under the MIT License.
