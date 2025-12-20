from backend.embeddings.log_embeddings import LogEmbeddingStore

class RAGService:
    def __init__(self):
        self.store = LogEmbeddingStore()

    def ingest_logs(self,logs):
        self.store.add_logs(logs)  # this will load logs into vector DB

    def answer(self, query):
        """
        -------------------------------------------------------------
        This is called on every user query 
        It performs : 1. Retrieval , 2. Explanation (Generation)
        -------------------------------------------------------------
        """
        retrieved_logs = self.store.search(query)

        #LLM Placeholder
        explanation = self._explain(query, retrieved_logs)

        return {
            "query": query,
            "retrieved_logs": retrieved_logs,
            "explanation": explanation
        }
    def _explain(self, query, logs):
        """
        Temporary stand-in for an LLM
        Logic-based explanation
        """
        if not logs:
            return " No Relevant Logs Found."
        
        if any("DB_TIMEOUT" in log for log in logs):
            return (
            "The payment service failed due to a database timeout. "
            "This usually indicates slow database responses or connection issues."
            )
        if any("CACHE_MISS" in log for log in logs):
            return (
                "The service experienced cache misses, leading to increased latency. "
            )
        
        return (
                "The issue appears to be related to general service instability. "
                "Please inspect the logs for more details."
        )