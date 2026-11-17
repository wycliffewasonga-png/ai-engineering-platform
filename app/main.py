from fastapi import FastAPI

app = FastAPI(
    title="AI Engineering Platform",
    description="An AI application platform integrating LLMs, RAG, AI agents, and machine learning.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "AI Engineering Platform is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Engineering Platform",
    }
