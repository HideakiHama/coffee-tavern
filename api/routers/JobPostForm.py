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
from authenticator import authenticator

router = APIRouter()

# creating new job form
@router.post('/create_form/', tags=["JobForm"], response_model=JobPostFormOut2)
def create_job_form(
    new_form: JobPostFormIn,
    repo: JobFormRepository = Depends(),
    repo1: AccountRepo = Depends(),
    account: dict = Depends(authenticator.get_current_account_data)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You do not have access to this as employee. TURN BACK NOW!",
    )
    print("ACC", account["id"])
    if account["role"] == "Employer":
        not_final = repo.create(new_form, account["id"]).dict()
        not_final["account_id"] = account
        return not_final
    raise credentials_exception


@router.get("/get_all_form", tags=["JobForm"], response_model=Union[List[JobPostForm], Error])
def get_all_job_form(repo: JobFormRepository = Depends(), account: dict = Depends(authenticator.get_current_account_data)):
    return repo.get_all()

@router.get("/get_form/{form_id}", tags=["JobForm"], response_model=Union[JobPostFormOut, Error])
def get_one_job_form(form_id: int, response: Response, repo: JobFormRepository = Depends(), account: dict = Depends(authenticator.get_current_account_data)) -> JobPostFormOut:
    FormDetail = repo.get_one(form_id)
    if FormDetail is None:
        response.status_code = 404
    return FormDetail

@router.post("/update_job_form/{id}", tags=["JobForm"], response_model=Union[JobPostFormOut, Error],)
def Update_Job_Form(
    form_id: int,
    UpdatedJobForm: JobPostFormIn,
    repo: JobFormRepository = Depends(),
    account: dict = Depends(authenticator.get_current_account_data)
) -> Union[JobPostFormOut, Error]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are employee. Only the employer can edit",
    )
    if account["role"] == "Employer":
        return repo.update(form_id, UpdatedJobForm)
    raise credentials_exception


@router.delete("/delete_job_form/{id}", tags=["JobForm"], response_model=bool)
def Delete_Job_Form(form_id: int, repo: JobFormRepository = Depends(), account: dict = Depends(authenticator.get_current_account_data)) -> bool:
    if account["role"] == "Employer":
        return repo.delete(form_id)
