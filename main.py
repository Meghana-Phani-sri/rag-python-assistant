import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

docs_dir = "docs"
files = [os.path.join(docs_dir, f) for f in os.listdir(docs_dir) if f.endswith('.txt')]
all_docs = []
for file in files:
    loader = TextLoader(file)
    all_docs.extend(loader.load())
blocked_keywords = [
    "hack",
    "malware",
    "exploit",
    "phishing"
]

if any(
    word in user_query.lower()
    for word in blocked_keywords
):
    print(
        "Sorry, this request is not allowed."
    )
    exit()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
documents = text_splitter.split_documents(all_docs)

embeddings = HuggingFaceEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever()
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
from langchain.memory import ConversationBufferMemory
def run_query(query):
    result = qa_chain({
    "question": query
})

answer = result["answer"]
    print("
Top answers from your docs:
")
    for idx, doc in enumerate(results):
        print(f"{idx+1}. {doc.page_content}
---")

if _name_ == "_main_":
    print("RAG Python Assistant (using HuggingFace embeddings)")
    print("-" * 50)
    while True:
        user_q = input("
Ask a question (or type exit): ")
        if user_q.lower() == "exit":
            break
        run_query(user_q)
