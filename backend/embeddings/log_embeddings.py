from sentence_transformers import SentenceTransformer 
import faiss 
import numpy as np  
import os 
import pickle 

class LogEmbeddingStore:
    """
    This class is doing two jobs:
        Store knowledge (logs → embeddings → vector DB) 
        Retrieve knowledge (question → similar logs)
    That is Retrieval in RAG (Retrieval Augmented Generation).
    
    """
    def __init__(self, index_path="data/faiss.index", meta_path="data/logs.pkl"):
        # Load embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Correct attribute names
        self.index_path = index_path
        self.meta_path = meta_path

        os.makedirs("data", exist_ok=True)

        # Load existing index + logs if present
        if os.path.exists(self.index_path) and os.path.exists(self.meta_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.meta_path, "rb") as f:
                self.logs = pickle.load(f)

            # Safety check
            if self.index.ntotal != len(self.logs):
                print("FAISS index and logs mismatch. Reinitializing.")
                self.index = faiss.IndexFlatL2(384)
                self.logs = []
        else:
            self.index = faiss.IndexFlatL2(384)
            self.logs = []

    def add_logs(self, log_texts):
        """
        Add new logs to vector store
        """
        embeddings = self.model.encode(log_texts)
        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)
        self.logs.extend(log_texts)

        # Persist to disk
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.logs, f)

    def search(self, query, top_k=3):
        """
        Retrieve most relevant logs for a query
        """
        if self.index.ntotal == 0:
            return []

        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        return [self.logs[i] for i in indices[0] if 0 <= i < len(self.logs)]


print(" LOG_EMBEDDINGS.PY LOADED")