from fastapi import FastAPI

from backend.api.ai import router as ai_router

app = FastAPI()

app.include_router(ai_router)

@app.get("/")
def root():
    return {"status": "running"}