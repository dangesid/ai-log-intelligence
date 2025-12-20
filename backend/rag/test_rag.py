from backend.rag.rag_service import RAGService


logs = [
    "ERROR payments DB_TIMEOUT",
    "ERROR payments CACHE_MISS"
]

rag = RAGService()
rag.ingest_logs(logs)

query = "Why did the payment service fail?" 

response = rag.answer(query)

print("User query:", response["query"])
print("\nRetrieved logs:")
for log in response["retrieved_logs"]:
    print("-", log)

print("\nAI Answer:")
print(response["explanation"])