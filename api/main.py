from fastapi import FastAPI
from routers import UserModels, Accounts, JobPostForm


## Registration for models similar to Django admin
app = FastAPI()

app.include_router(UserModels.router),
app.include_router(Accounts.router),
app.include_router(JobPostForm.router)


