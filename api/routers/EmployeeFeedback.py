from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.EmployeeFeedback_queries import (
    EmployeeFeedbackFormIn,
    EmployeeFeedbackFormOut,
    EmployeeFeedbackRepository,
    Error,
)

from fastapi.encoders import jsonable_encoder


router = APIRouter()

## POST ##
# creating new employee feedback form #
@router.post(
    "/employee-feedback-form/",
    tags=["Feedback"],
    response_model=EmployeeFeedbackFormOut,
)
def create_employee_feedback_form(
    new_form: EmployeeFeedbackFormIn,
    repo: EmployeeFeedbackRepository = Depends(),
):
    return repo.create(new_form)


## GET ##
# getting detail feedback from employee
@router.get(
    "/employee-feedback-form/{EmployeeFeedback_id}",
    tags=["Feedback"],
    response_model=Union[EmployeeFeedbackFormOut, Error],
)
def get_one_employee_feedback_form(
    EmployeeFeedback_id: int,
    response: Response,
    repo: EmployeeFeedbackRepository = Depends(),
) -> EmployeeFeedbackFormOut:
    EmployeeFeedback = repo.get_one(EmployeeFeedback_id)
    if EmployeeFeedback is None:
        response.status_code = 404
    return EmployeeFeedback


## GET ##
# getting list of feedback from employees
@router.get(
    "/employee-feedbacks/",
    tags=["Feedback"],
    response_model=Union[List[EmployeeFeedbackFormOut], Error],
)
def get_all(
    repo: EmployeeFeedbackRepository = Depends(),
):
    return repo.get_all()


## POST ##
# Edit feedback #
@router.put(
    "/employee-feedback-form/{EmployeeFeedback_id}",
    tags=["Feedback"],
    response_model=Union[EmployeeFeedbackFormOut, Error],
)
def Edit_Employee_Feedback(
    EmployeeFeedback_id: int,
    FeedbackForm: EmployeeFeedbackFormIn,
    repo: EmployeeFeedbackRepository = Depends(),
) -> Union[Error, EmployeeFeedbackFormOut]:
    return repo.update(EmployeeFeedback_id, FeedbackForm)
