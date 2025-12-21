from fastapi import APIRouter
from backend.api.schemas import IngestRequest
from backend.rag.rag_singleton import rag_service as rag

router = APIRouter()


@router.post("/ingest")
def ingest_logs(request: IngestRequest):
    rag.ingest_logs(request.logs)
    return {"status": "logs ingested successfully", "count": len(request.logs)}

