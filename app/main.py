"""FastAPI app entry point; mounts routers + static files."""
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.database import init_db
from app.routers import auth_router, pages_router

app = FastAPI(title="UCSD Citizen App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pages_router.router)
app.include_router(auth_router.router)

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/login")
def login_page():
    return FileResponse(STATIC_DIR / "login.html")


app.mount("/", StaticFiles(directory=STATIC_DIR), name="static")
