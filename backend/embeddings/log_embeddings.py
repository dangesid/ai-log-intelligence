from sentence_transformers import SentenceTransformer 
import faiss 
import numpy as np  

class LogEmbeddingStore:
    """
    This class is doing two jobs:
        Store knowledge (logs → embeddings → vector DB) 
        Retrieve knowledge (question → similar logs)
    That is Retrieval in RAG (Retrieval Augmented Generation).
    
    """
    def __init__(self):
        #Loading emvedding model 
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Vector Dimension for this model = 384 
        self.index = faiss.IndexFlatL2(384)

        #Store Original logs for retrieval
        self.logs = []

    def add_logs(self, log_texts):
        """
        log_texts: this is the list of strings ----> List[str]
        --------------------------------------------------------------------
        | This function adds new log messages into the vector store          |
        -------------------------------------------------------------------
        """
        embeddings = self.model.encode(log_texts)
        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)
        self.logs.extend(log_texts)

    def search(self, query, top_k=3):
        query_embeddings = self.model.encode([query])
        query_embeddings = np.array(query_embeddings).astype("float32")

        distances, indices = self.index.search(query_embeddings, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.logs):
                results.append(self.logs[idx])

        return results
    print("🔥 LOG_EMBEDDINGS.PY LOADED")
