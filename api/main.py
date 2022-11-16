from fastapi import FastAPI
from routers import account

app = FastAPI()
app.include_router(account.routers)
