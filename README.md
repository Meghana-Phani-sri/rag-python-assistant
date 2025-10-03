# RAG-Based Python QA Assistant

This project is a Retrieval-Augmented Generation (RAG) assistant built with Python and LangChain. It answers Python-related questions by searching a custom knowledge base of .txt files using HuggingFace Embeddings and FAISS.

## Features

- Local retrieval of information from provided documents
- OpenAI API needed
- Easy to extend by adding new .txt files to the docs folder

## How to Run

1. Create and activate a virtual environment:
    
    python -m venv venv
    venv\Scripts\activate
    

2. Install requirements:
    
    pip install -r requirements.txt
    

3. Add your .txt files to the docs folder.

4. Run the assistant:
    
    python main.py
    

5. Type a question and get answers extracted from your docs.

## Example
Ask a question (or type exit): What is list comprehension?List comprehensions provide a concise way to create lists in Python. Example: [x*x for x in range(10)] creates a list of squares.
 ## Folder Structure

- main.py: Main assistant script
- requirements.txt: Python dependencies
- README.md: Project documentation
- docs/: All knowledge base .txt files

## Notes

- If you see any deprecation warning about HuggingFaceEmbeddings on latest LangChain, it is safe to ignore.

- Modify/add .txt files to expand your assistant’s knowledge.
