from fastapi import APIRouter
from backend.api.schemas import QueryRequest

print("🔥 QUERY.PY LOADED")

router = APIRouter()

@router.post("/query")
def query_logs(request: QueryRequest):
    return {
        "query": request.query,
        "message": "RAG pipeline is not connected yet"
    }
