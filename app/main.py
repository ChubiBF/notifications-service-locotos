from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router as notifications_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(notifications_router)

@app.get("/health", tags=["Utility"])
async def health_check():
    return {
        "status": "online",
        "service": settings.PROJECT_NAME
    }