from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.EmployerFeedback_queries import (
    EmployerFeedbackFormIn,
    EmployerFeedbackFormOut,
    EmployerFeedbackRepository,
    Error,
)

from fastapi.encoders import jsonable_encoder


router = APIRouter()

## POST ##
# creating new employer feedback form #
@router.post(
    "/employer-feedback-form/",
    tags=["Feedback"],
    response_model=EmployerFeedbackFormOut,
)
def create_employer_feedback_form(
    new_form: EmployerFeedbackFormIn,
    repo: EmployerFeedbackRepository = Depends(),
):
    return repo.create(new_form)


## GET ##
# getting detail feedback from employer
@router.get(
    "/employer-feedback-form/{EmployerFeedback_id}",
    tags=["Feedback"],
    response_model=Union[EmployerFeedbackFormOut, Error],
)
def get_one_employer_feedback_form(
    EmployerFeedback_id: int,
    response: Response,
    repo: EmployerFeedbackRepository = Depends(),
) -> EmployerFeedbackFormOut:
    EmployerFeedback = repo.get_one(EmployerFeedback_id)
    if EmployerFeedback is None:
        response.status_code = 404
    return EmployerFeedback


## GET ##
# getting list of feedback from employers
@router.get(
    "/employer-feedbacks/",
    tags=["Feedback"],
    response_model=Union[List[EmployerFeedbackFormOut], Error],
)
def get_all(
    repo: EmployerFeedbackRepository = Depends(),
):
    return repo.get_all()


## POST ##
# Edit feedback #
@router.put(
    "/employer-feedback-form/{EmployerFeedback_id}",
    tags=["Feedback"],
    response_model=Union[EmployerFeedbackFormOut, Error],
)
def Edit_Employer_Feedback(
    EmployerFeedback_id: int,
    FeedbackForm: EmployerFeedbackFormIn,
    repo: EmployerFeedbackRepository = Depends(),
) -> Union[Error, EmployerFeedbackFormOut]:
    return repo.update(EmployerFeedback_id, FeedbackForm)
