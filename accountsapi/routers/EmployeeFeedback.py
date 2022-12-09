from fastapi import APIRouter, Depends, HTTPException, status
from typing import Union, List
from queries.EmployeeFeedback_queries import (
    EmployeeFeedbackFormIn,
    EmployeeFeedbackFormOut,
    EmployeeFeedbackRepository,
    EmployeeFeedbackFormOut2,
    Error,
)
from authenticator import authenticator

router = APIRouter()


# POST #
# creating new employee feedback form
@router.post(
    "/employee-feedback-form/{account_id}",
    tags=["Employee Feedback Form"],
    response_model=EmployeeFeedbackFormOut,
)
def create_employee_feedback_form(
    new_form: EmployeeFeedbackFormIn,
    repo: EmployeeFeedbackRepository = Depends(),
    account: dict = Depends(authenticator.get_current_account_data),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are employer. Please use employer feedback form",
    )
    if account["role"] == "Employee":
        not_final = repo.create(new_form, account["id"]).dict()
        not_final["account_id"] = account
        return not_final
    raise credentials_exception


# GET #
# getting detail feedback from employee
@router.get(
    "/employee-feedback-form/{EmployeeFeedback_id}",
    tags=["Employee Feedback Form"],
    response_model=Union[EmployeeFeedbackFormOut, Error],
)
def get_one_employee_feedback_form(
    EmployeeFeedback_id: int,
    account: dict = Depends(authenticator.get_current_account_data),
    repo: EmployeeFeedbackRepository = Depends(),
) -> EmployeeFeedbackFormOut:
    credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="employee feedback not found",
    )
    EmployeeFeedback = repo.get_one(EmployeeFeedback_id).dict()
    EmployeeFeedback["account_id"] = account

    if EmployeeFeedback:
        return EmployeeFeedback
    raise credentials_exception


# GET #
# getting list of feedback from specific employees
@router.get(
    "/employee-feedbacks/{account_id}",
    tags=["Employee Feedback Form"],
    response_model=Union[List[EmployeeFeedbackFormOut2], Error],
)
def get_all_with_id(
    account_id: int,
    account: dict = Depends(authenticator.get_current_account_data),
    repo: EmployeeFeedbackRepository = Depends(),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="employee feedback not found",
    )
    AllIdEmployeeFeedback = repo.get_all_with_id(account_id)
    if AllIdEmployeeFeedback:
        return AllIdEmployeeFeedback
    raise credentials_exception


# GET #
# Get all the EmployeeFeedbacks Regardless of who wrote it
@router.get("/get_all_employeeFeedbacks", tags=["Employee Feedback Form"])
def get_all_employee_feedbacks(
    # account: dict = Depends(authenticator.get_current_account_data),
    repo: EmployeeFeedbackRepository = Depends(),
):
    return repo.get_all_feedbacks()


# PUT #
# Edit feedback #
@router.put(
    "/employee-feedback-form/{EmployeeFeedback_id}",
    tags=["Employee Feedback Form"],
    response_model=Union[EmployeeFeedbackFormOut, Error],
)
def Edit_Employee_Feedback(
    EmployeeFeedback_id: int,
    FeedbackForm: EmployeeFeedbackFormIn,
    repo: EmployeeFeedbackRepository = Depends(),
    account: dict = Depends(authenticator.get_current_account_data),
) -> Union[Error, EmployeeFeedbackFormOut]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are employee. Only the employer can edit",
    )

    # x = repo.get_one(EmployeeFeedback_id)
    if account["role"] == "Employee":
        return repo.update(EmployeeFeedback_id, FeedbackForm)
    raise credentials_exception


# DELETE #
# Delete feedback #
@router.delete(
    "/employee-feedback-form/{EmployeeFeedback_id}",
    tags=["Employee Feedback Form"],
    response_model=bool,
)
def Delete_Employee_Feedback(
    EmployeeFeedback_id: int,
    repo: EmployeeFeedbackRepository = Depends(),
    account: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are employee. Only the employer can edit",
    )

    # x = repo.get_one(EmployeeFeedback_id)
    if account["role"] == "Employee":
        return repo.delete(EmployeeFeedback_id)
    raise credentials_exception
