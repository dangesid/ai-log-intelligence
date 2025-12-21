from fastapi import FastAPI
from backend.api.routes.health import router as health_router
from backend.api.routes.query import router as query_router
from backend.api.routes.ingest import router as ingest_router

print("🔥 MAIN.PY LOADED")

app = FastAPI(title="AI Log Intelligence")

app.include_router(ingest_router)
app.include_router(query_router)
app.include_router(health_router)