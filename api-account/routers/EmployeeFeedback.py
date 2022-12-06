from fastapi import APIRouter, Depends, Response, HTTPException, status
from typing import Union, List
from queries.EmployeeFeedback_queries import (
    EmployeeFeedbackFormIn,
    EmployeeFeedbackFormOut,
    EmployeeFeedbackRepository,
    EmployeeFeedbackFormOut2,
    Error,
)
from RoleChecker import RoleChecker

from queries.accounts import AccountRepo

router = APIRouter()

checker = RoleChecker("Employee")

## POST ##
# creating new employee feedback form #
@router.post(
    "/employee-feedback-form/{account_id}",
    tags=["Employee Feedback Form"],
    response_model=EmployeeFeedbackFormOut,
)
def create_employee_feedback_form(
    new_form: EmployeeFeedbackFormIn,
    account_id: int,
    repo: EmployeeFeedbackRepository = Depends(),
    repo1: AccountRepo = Depends(),
    checked_role: bool = Depends(checker),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are employer. Please use employer feedback form",
    )
    if checked_role:
        not_final = repo.create(new_form, account_id).dict()
        not_final["account_id"] = repo1.get(account_id).dict()
        return not_final
    raise credentials_exception

## GET ##
# getting detail feedback from employee
@router.get(
    "/employee-feedback-form/{EmployeeFeedback_id}",
    tags=["Employee Feedback Form"],
    response_model=Union[EmployeeFeedbackFormOut, Error],
)
def get_one_employee_feedback_form(
    EmployeeFeedback_id: int,
    response: Response,
    repo: EmployeeFeedbackRepository = Depends(),
    repo1: AccountRepo = Depends()
) -> EmployeeFeedbackFormOut:
    credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="employee feedback not found",
    )
    EmployeeFeedback = repo.get_one(EmployeeFeedback_id).dict()
    EmployeeFeedback["account_id"] = repo1.get(EmployeeFeedback["account_id"]).dict()
    if EmployeeFeedback:
        return EmployeeFeedback
    raise credentials_exception


## GET ##
# getting list of feedback from employees
@router.get(
    "/employee-feedbacks/{account_id}",
    tags=["Employee Feedback Form"],
    response_model=Union[List[EmployeeFeedbackFormOut2], Error],
)
def get_all(
    account_id: int,
    repo: EmployeeFeedbackRepository = Depends(),
):
    return repo.get_all(account_id)


## PUT ##
# Edit feedback #
@router.patch(
    "/employee-feedback-form/{EmployeeFeedback_id}",
    tags=["Employee Feedback Form"],
    response_model=Union[EmployeeFeedbackFormOut, Error],
)
def Edit_Employee_Feedback(
    EmployeeFeedback_id: int,
    FeedbackForm: EmployeeFeedbackFormIn,
    repo: EmployeeFeedbackRepository = Depends(),
) -> Union[Error, EmployeeFeedbackFormOut]:
    return repo.update(EmployeeFeedback_id, FeedbackForm)


## DELETE ##
# Delete feedback #
@router.delete(
    "/employee-feedback-form/{EmployeeFeedback_id}",
    tags=["Employee Feedback Form"],
    response_model=bool,
)
def Delete_Employee_Feedback(
    EmployeeFeedback_id: int,
    repo: EmployeeFeedbackRepository = Depends(),
) -> bool:
    return repo.delete(EmployeeFeedback_id)
