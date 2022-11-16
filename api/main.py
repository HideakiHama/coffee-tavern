from fastapi import FastAPI
from routers import UserModels, Accounts

## Registration for models similar to Django admin
app = FastAPI()
app.include_router(UserModels.router),
app.include_router(Accounts.router),
