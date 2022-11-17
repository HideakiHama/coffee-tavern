from fastapi import FastAPI
from routers import UserModels, Accounts, JobPostForm
import services as _services

## Registration for models similar to Django admin
app = FastAPI()

app.include_router(UserModels.router),
app.include_router(Accounts.router),
app.include_router(JobPostForm.router)


_services.create.database() ##creates a database