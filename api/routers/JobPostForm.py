from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
from queries.JobForm_queries import (
    JobPostFormIn,
    JobPostFormOut,
    JobFormRepository,
    Tags
)


router = APIRouter()

# creating new job form
@router.post('/create_form', response_model=JobPostFormOut)
def create_job_form(
    new_form: JobPostFormIn,
    repo: JobFormRepository = Depends(),
):
    return repo.create(new_form)
