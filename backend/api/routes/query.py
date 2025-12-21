from fastapi import APIRouter
from backend.api.schemas import QueryRequest
from backend.rag.rag_service import RAGService

print("🔥 QUERY.PY LOADED")

router = APIRouter()
rag = RAGService()

@router.post("/query",)
def query_logs(request: QueryRequest):
    result = rag.answer(request.query)
    return result
