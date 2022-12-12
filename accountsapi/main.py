from fastapi import FastAPI
from routers import (
    Accounts,
    JobPostForm,
    EmployerFeedback,
    EmployeeFeedback,
    UploadResume,
    EmployeeInfo,
    EmployerInfo,
)
from authenticator import authenticator
from fastapi.middleware.cors import CORSMiddleware
import os
# Registration for models similar to Django admin
app = FastAPI()

origins = [
    os.environ.get("CORS_HOST", "http://localhost:3000"),
    os.environ.get("TAGSAPI_CORS_HOST", "http://localhost:8100"),

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Accounts.router),
app.include_router(JobPostForm.router),
app.include_router(EmployerFeedback.router)
app.include_router(EmployeeFeedback.router)
app.include_router(authenticator.router)
app.include_router(UploadResume.router)
app.include_router(EmployeeInfo.router)
app.include_router(EmployerInfo.router)
