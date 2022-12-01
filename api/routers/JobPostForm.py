from fastapi import APIRouter, Depends, Response, HTTPException, status
from typing import List, Optional, Union
from queries.JobForm_queries import (
    JobPostFormIn,
    JobPostFormOut,
    JobFormRepository,
    Tags,
    Error,
    JobPostForm,
    JobPostFormOut2
)
from queries.accounts import AccountRepo
from RoleChecker import RoleChecker

router = APIRouter()

checker = RoleChecker("Employer")

# creating new job form
@router.post('/create_form/{account_id}', tags=["JobForm"], response_model=JobPostFormOut2)
def create_job_form(
    new_form: JobPostFormIn,
    account_id: int,
    repo: JobFormRepository = Depends(),
    repo1: AccountRepo = Depends(),
    checked_role: bool = Depends(checker),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You do not have access to this as employee. TURN BACK NOW!",
    )
    if checked_role:
        not_final = repo.create(new_form, account_id).dict()
        not_final["account_id"] = repo1.get(account_id).dict()
        return not_final
    raise credentials_exception

@router.get('/get_all_form', tags=["JobForm"], response_model=Union[List[JobPostForm], Error])
def get_all_job_form(repo: JobFormRepository = Depends()):

    return repo.get_all()

@router.get('/get_form/{form_id}', tags=["JobForm"], response_model=Union[JobPostFormOut, Error])
def get_one_job_form(form_id: int, response: Response, repo: JobFormRepository = Depends()) -> JobPostFormOut:
    FormDetail = repo.get_one(form_id)
    if FormDetail is None:
        response.status_code = 404
    return FormDetail

@router.put('/update_job_form/{id}', tags=["JobForm"], response_model=Union[JobPostFormOut, Error])
def Update_Job_Form(form_id: int, UpdatedJobForm: JobPostFormIn, repo: JobFormRepository = Depends()) -> Union[JobPostFormOut, Error]:
    return repo.update(form_id, UpdatedJobForm)

@router.delete('/delete_job_form/{id}', tags=["JobForm"], response_model=bool)
def Delete_Job_Form(form_id: int, repo: JobFormRepository = Depends()) -> bool:
    return repo.delete(form_id)
