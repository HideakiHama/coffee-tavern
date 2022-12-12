from fastapi import FastAPI
from routers import (
    TagRoutes,
)
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = [
    os.environ.get("CORS_HOST", "http://localhost:3000"),
    os.environ.get("ACCOUNTS_CORS_HOST", "http://localhost:8000"),

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(TagRoutes.router),
