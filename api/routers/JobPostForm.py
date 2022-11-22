from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
from queries.JobForm_queries import (
    JobPostFormIn,
    JobPostFormOut,
    JobFormRepository,
    Tags,
    Error,
    JobPostForm
)


router = APIRouter()

# creating new job form
@router.post('/create_form', response_model=JobPostFormOut)
def create_job_form(
    new_form: JobPostFormIn,
    repo: JobFormRepository = Depends(),
):
    return repo.create(new_form)

@router.get('/get_all_form', response_model=Union[List[JobPostForm], Error])
def get_all_job_form(repo: JobFormRepository = Depends()):

    return repo.get_all()

@router.get('/get_form/{form_id}', response_model=Union[JobPostFormOut, Error])
def get_one_job_form(form_id: int, response: Response, repo: JobFormRepository = Depends()) -> JobPostFormOut:
    FormDetail = repo.get_one(form_id)
    if FormDetail is None:
        response.status_code = 404
    return FormDetail

@router.put('/update_job_form/{id}', response_model=Union[JobPostFormOut, Error])
def Update_Job_Form(form_id: int, UpdatedJobForm: JobPostFormIn, repo: JobFormRepository = Depends()) -> Union[JobPostFormOut, Error]:
    return repo.update(form_id, UpdatedJobForm)

@router.delete('/delete_job_form/{id}', response_model=bool)
def Delete_Job_Form(form_id: int, repo: JobFormRepository = Depends()) -> bool:
    return repo.delete(form_id)
