from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.base import api_router
from core.config import settings

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# static_html = FileResponse("vite-project/dist/index.html")
# @app.get("/product/{full_path:path}")
# def index():
#     return static_html

app.include_router(api_router, prefix="/api")
app.mount("/api", api_router, name="api")
app.mount("/", StaticFiles(directory="vite-project/dist", html=True), name="ui")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True,
    )
