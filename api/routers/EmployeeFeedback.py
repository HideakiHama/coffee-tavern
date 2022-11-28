from fastapi import APIRouter, Depends, Response, HTTPException, status
from typing import Union, List
from queries.EmployeeFeedback_queries import (
    EmployeeFeedbackFormIn,
    EmployeeFeedbackFormOut,
    EmployeeFeedbackRepository,
    Error,
)
from RoleChecker import RoleChecker

router = APIRouter()

checker = RoleChecker("Employee")

## POST ##
# creating new employee feedback form #
@router.post(
    "/employee-feedback-form/",
    tags=["Employee Feedback"],
    response_model=EmployeeFeedbackFormOut,
)
def create_employee_feedback_form(
    new_form: EmployeeFeedbackFormIn,
    repo: EmployeeFeedbackRepository = Depends(),
    checked_role: bool = Depends(checker),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are employer. Please use employer feedback form",
    )
    if checked_role:
        return repo.create(new_form)
    raise credentials_exception


## GET ##
# getting detail feedback from employee
@router.get(
    "/employee-feedback-form/{EmployeeFeedback_id}",
    tags=["Employee Feedback"],
    response_model=Union[EmployeeFeedbackFormOut, Error],
)
def get_one_employee_feedback_form(
    EmployeeFeedback_id: int,
    response: Response,
    repo: EmployeeFeedbackRepository = Depends(),
) -> EmployeeFeedbackFormOut:
    credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="employee feedback not found",
    )
    EmployeeFeedback = repo.get_one(EmployeeFeedback_id)
    if EmployeeFeedback:
        return EmployeeFeedback
    raise credentials_exception


## GET ##
# getting list of feedback from employees
@router.get(
    "/employee-feedbacks/",
    tags=["Employee Feedback"],
    response_model=Union[List[EmployeeFeedbackFormOut], Error],
)
def get_all(
    repo: EmployeeFeedbackRepository = Depends(),
):
    return repo.get_all()


## PUT ##
# Edit feedback #
@router.put(
    "/employee-feedback-form/{EmployeeFeedback_id}",
    tags=["Employee Feedback"],
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
    tags=["Employee Feedback"],
    response_model=bool,
)
def Delete_Employee_Feedback(
    EmployeeFeedback_id: int,
    repo: EmployeeFeedbackRepository = Depends(),
) -> bool:
    return repo.delete(EmployeeFeedback_id)
