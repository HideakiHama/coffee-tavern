from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
from queries.JobForm_queries import (
    JobPostForm,
    JobPostFormIn,
    Tags
)

router = APIRouter()

# creating new job form
@router.post('/create_form', response_model=JobPostForm)
def create_job_form(
    new_form: JobPostFormIn,
    queries: UserQueries = Depends()
):
    return queries.create(new_form)
