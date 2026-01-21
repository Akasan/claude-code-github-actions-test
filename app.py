from fastapi import FastAPI

app = FastAPI(title="FastAPI Server", version="1.0.0")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
