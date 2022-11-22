from fastapi import FastAPI
from routers import Accounts, JobPostForm, PostEmployerFeedback, UploadResume
from authenticator import authenticator

## Registration for models similar to Django admin
app = FastAPI()

# app.include_router(UserModels.router),
app.include_router(Accounts.router),
app.include_router(JobPostForm.router),
app.include_router(PostEmployerFeedback.router)
app.include_router(authenticator.router)  # problem to check
app.include_router(UploadResume.router)