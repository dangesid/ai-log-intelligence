from pydantic import BaseModel

print("🔥 SCHEMAS.PY LOADED")

class QueryRequest(BaseModel):
    query: str
    log_data: str
