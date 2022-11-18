from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool


class Error(BaseModel):
    message: str


class EmployerFeedbackFormIn(BaseModel):
    employee_name: str
    description: str


class EmployerFeedbackFormOut(BaseModel):
    id: int
    employee_name: str
    description: str


# Employer Feedback of Employee
class EmployerFeedbackRepository:
    ## GET ##
    def get_one(self, EmployerFeedback_id: int) -> Optional[EmployerFeedbackFormOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                        , employee_name
                        , description
                        FROM employer_form
                        WHERE id = %s
                        """,
                        [
                            EmployerFeedback_id,
                        ],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_employer_feedback_out(record)  # refactored
        except Exception as e:
            return {"message": "Could not get employer feedback form"}

    ## GET ##
    def get_all(self) -> Union[List[EmployerFeedbackFormOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, employee_name, description
                        FROM employer_form
                        ORDER BY id
                        """
                    )
                    resultList = list(result)
                return [
                    self.record_to_employer_feedback_out(record)
                    for record in resultList
                ]  # refactored
        except Exception as e:
            return {"message": "Could not get employer feedback form"}

    ## POST ##
    def create(self, FeedbackForm: EmployerFeedbackFormIn) -> EmployerFeedbackFormOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO employer_form
                            (employee_name, description)
                        VALUES
                            (%s, %s)
                        RETURNING id;
                        """,
                        [FeedbackForm.employee_name, FeedbackForm.description],
                    )
                    print("RESULT", result)
                    id = result.fetchone()[0]
                    print("ID", id)
                    return self.feedback_post_in_to_out(id, FeedbackForm)
        except Exception:
            return {"message": "Couldn't create feedback"}

    ## PUT ##
    def update(
        self, EmployerFeedback_id: int, FeedbackForm: EmployerFeedbackFormIn
    ) -> Union[EmployerFeedbackFormOut, Error]:
        try:

            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE employer_form
                        SET employee_name = %s
                            , description = %s
                        WHEN id = %s
                        """,
                        [
                            FeedbackForm.employee_name,
                            FeedbackForm.description,
                            FeedbackForm.id,
                        ],
                    )
                    old_data = FeedbackForm.dict()
                    return EmployerFeedbackFormOut(EmployerFeedback_id, **old_data)
                    # return self.feedback_post_in_to_out(
                    #     EmployerFeedback_id, FeedbackForm
                    # )
        except Exception:
            return {"message": "Could not update the Feedback"}

    def feedback_post_in_to_out(self, id: int, FeedbackForm: EmployerFeedbackFormIn):
        old_data = FeedbackForm.dict()
        return EmployerFeedbackFormOut(id=id, **old_data)

    # refactored function for GET#
    def record_to_employer_feedback_out(self, record):
        return EmployerFeedbackFormOut(
            id=record[0], employee_name=record[1], description=record[2]
        )
