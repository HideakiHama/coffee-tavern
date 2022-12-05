from fastapi import APIRouter, Depends, Response, HTTPException, status
from typing import Union, List
from queries.EmployerFeedback_queries import (
    EmployerFeedbackFormIn,
    EmployerFeedbackFormOut,
    EmployerFeedbackRepository,
    EmployerFeedbackFormOut2,
    Error,
)
from queries.accounts import AccountRepo
from authenticator import authenticator

from queries.accounts import AccountIn, AccountOut, AccountRepo, Error

router = APIRouter()


## POST ##
# creating new employer feedback form #
@router.post(
    "/employer-feedback-form/{account_id}",
    tags=["Employer Feedback Form"],
    response_model=EmployerFeedbackFormOut,
)
async def create_employer_feedback_form(
    new_form: EmployerFeedbackFormIn,
    repo: EmployerFeedbackRepository = Depends(),
    account: dict = Depends(authenticator.get_current_account_data),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are employee. Please use employee feedback form",
    )
    if account["role"] == "Employer":
        not_final = repo.create(new_form, account["id"]).dict()  ####
        not_final["account_id"] = account
        return not_final
    raise credentials_exception


## GET ##
# getting detail feedback from employer
@router.get(
    "/employer-feedback-form/{EmployerFeedback_id}",
    tags=["Employer Feedback Form"],
    response_model=Union[EmployerFeedbackFormOut, Error],
)
def get_one_employer_feedback_form(
    EmployerFeedback_id: int,
    account: dict = Depends(authenticator.get_current_account_data),
    repo: EmployerFeedbackRepository = Depends(),
) -> EmployerFeedbackFormOut:
    credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="employee feedback not found",
    )
    EmployerFeedback = repo.get_one(EmployerFeedback_id).dict()
    EmployerFeedback["account_id"] = account

    if EmployerFeedback:
        return EmployerFeedback
    raise credentials_exception


## GET ##
# getting list of feedback from employers
@router.get(
    "/employer-feedbacks/{account_id}",
    tags=["Employer Feedback Form"],
    response_model=Union[List[EmployerFeedbackFormOut2], Error],
)
def get_all(
    account_id: int,
    repo: EmployerFeedbackRepository = Depends(),
    account: dict = Depends(authenticator.get_current_account_data),
):
    return repo.get_all(account_id)


## PUT ##
# Edit feedback #
@router.put(
    "/employer-feedback-form/{EmployerFeedback_id}",
    tags=["Employer Feedback Form"],
    response_model=Union[EmployerFeedbackFormOut, Error],
)
def Edit_Employer_Feedback(
    EmployerFeedback_id: int,
    FeedbackForm: EmployerFeedbackFormIn,
    repo: EmployerFeedbackRepository = Depends(),
    account: dict = Depends(authenticator.get_current_account_data),
) -> Union[Error, EmployerFeedbackFormOut]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are employee. Only the employer can edit",
    )

    x = repo.get_one(EmployerFeedback_id)
    # print(x.account_id)
    if x.account_id == account["id"]:
        return repo.update(EmployerFeedback_id, FeedbackForm)
    raise credentials_exception


## DELETE ##
# Delete feedback #
@router.delete(
    "/employer-feedback-form/{EmployerFeedback_id}",
    tags=["Employer Feedback Form"],
    response_model=bool,
)
def Delete_Employer_Feedback(
    EmployerFeedback_id: int,
    repo: EmployerFeedbackRepository = Depends(),
    account: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are employee. Only the employer can edit",
    )

    x = repo.get_one(EmployerFeedback_id)
    # print(x.account_id)
    if x.account_id == account["id"]:
        return repo.delete(EmployerFeedback_id)
    raise credentials_exception
