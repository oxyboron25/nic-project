# # api/main.py

# from fastapi import FastAPI, UploadFile, File
# from pydantic import BaseModel
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import RetrievalQA
# from langchain.text_splitter import CharacterTextSplitter
# import fitz

# app = FastAPI()

# conversation_chain = None  # global state for now

# def extract_text_from_pdf(file: UploadFile):
#     text = ""
#     pdf = fitz.open(stream=file.file.read(), filetype="pdf")
#     for page in pdf:
#         text += page.get_text()
#     return text

# def build_chain(text: str):
#     splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#     chunks = splitter.split_text(text)
#     vectordb = FAISS.from_texts(chunks, OpenAIEmbeddings())
#     return RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=vectordb.as_retriever())

# class QueryRequest(BaseModel):
#     question: str

# @app.post("/upload")
# async def upload_pdf(file: UploadFile = File(...)):
#     global conversation_chain
#     text = extract_text_from_pdf(file)
#     conversation_chain = build_chain(text)
#     return {"message": "PDF processed and chain initialized."}

# @app.post("/ask")
# async def ask_question(request: QueryRequest):
#     if conversation_chain is None:
#         return {"error": "Upload a PDF first using /upload."}
#     answer = conversation_chain.run(request.question)
#     return {"response": answer}
