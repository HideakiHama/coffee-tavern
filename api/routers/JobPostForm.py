from fastapi import APIRouter, Depends, Response, HTTPException, status
from typing import List, Optional, Union
from queries.JobForm_queries import (
    JobPostFormIn,
    JobPostFormOut,
    JobFormRepository,
    Tags,
    Error,
    JobPostForm,
)
from RoleChecker import RoleChecker

router = APIRouter()

checker = RoleChecker("Employer")

# creating new job form
@router.post("/create_form", tags=["JobForm"], response_model=JobPostFormOut)
def create_job_form(
    new_form: JobPostFormIn,
    repo: JobFormRepository = Depends(),
):
    return repo.create(new_form)


@router.get(
    "/get_all_form", tags=["JobForm"], response_model=Union[List[JobPostForm], Error]
)
def get_all_job_form(repo: JobFormRepository = Depends()):

    return repo.get_all()


@router.get(
    "/get_form/{form_id}", tags=["JobForm"], response_model=Union[JobPostFormOut, Error]
)
def get_one_job_form(
    form_id: int, response: Response, repo: JobFormRepository = Depends()
) -> JobPostFormOut:
    FormDetail = repo.get_one(form_id)
    if FormDetail is None:
        response.status_code = 404
    return FormDetail


@router.post(
    "/update_job_form/{id}",
    tags=["JobForm"],
    response_model=Union[JobPostFormOut, Error],
)
def Update_Job_Form(
    form_id: int,
    UpdatedJobForm: JobPostFormIn,
    repo: JobFormRepository = Depends(),
    checked_role: bool = Depends(checker),
) -> Union[JobPostFormOut, Error]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are employee. Only the employer can edit",
    )
    if checked_role:
        return repo.update(form_id, UpdatedJobForm)
        # not_final = repo.create(new_form, account_id).dict()  ####
        # not_final["account_id"] = repo1.get(account_id).dict()
        # return not_final
    raise credentials_exception


@router.delete("/delete_job_form/{id}", tags=["JobForm"], response_model=bool)
def Delete_Job_Form(form_id: int, repo: JobFormRepository = Depends()) -> bool:
    return repo.delete(form_id)
