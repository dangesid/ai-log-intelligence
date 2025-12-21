from pydantic import BaseModel
from typing import List 

print("🔥 SCHEMAS.PY LOADED")

class IngestRequest(BaseModel):
    logs: List[str]

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    retrieved_logs: List[str]
    explanation: str