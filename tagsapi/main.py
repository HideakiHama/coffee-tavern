from fastapi import FastAPI
from routers import (
    TagRoutes,
)

app = FastAPI()

app.include_router(TagRoutes.router),

