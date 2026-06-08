test_questions = [
    "What is RAG?",
    "Explain embeddings",
    "What is vector search?"
]

for q in test_questions:
    response = qa_chain.run(q)

    print("Question:", q)
    print("Answer:", response)
    print("-" * 50)
