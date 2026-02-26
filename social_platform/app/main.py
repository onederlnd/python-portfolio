# main.py

from fastapi import FastAPI
from app.routes import router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Social Media API", version="1.0.0")
app.include_router(router)

# server frontend static files
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
