from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool


class Error(BaseModel):
    message: str


class EmployeeFeedbackFormIn(BaseModel):
    employer_name: str
    description: str


class EmployeeFeedbackFormOut(BaseModel):
    id: int
    employer_name: str
    description: str


# Employer Feedback of Employee
class EmployeeFeedbackRepository:
    ## GET ##
    def get_one(self, EmployeeFeedback_id: int) -> Optional[EmployeeFeedbackFormOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                        , employer_name
                        , description
                        FROM employee_form
                        WHERE id = %s
                        """,
                        [
                            EmployeeFeedback_id,
                        ],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_employee_feedback_out(record)  # refactored
        except Exception as e:
            return {"message": "Could not get employee feedback form"}

    ## GET ##
    def get_all(self) -> Union[List[EmployeeFeedbackFormOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, employer_name, description
                        FROM employee_form
                        ORDER BY id
                        """
                    )
                    resultList = list(result)
                return [
                    self.record_to_employee_feedback_out(record)
                    for record in resultList
                ]  # refactored
        except Exception as e:
            return {"message": "Could not get employee feedback form"}

    ## POST ##
    def create(self, FeedbackForm: EmployeeFeedbackFormIn) -> EmployeeFeedbackFormOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO employee_form
                            (employer_name, description)
                        VALUES
                            (%s, %s)
                        RETURNING id;
                        """,
                        [FeedbackForm.employer_name, FeedbackForm.description],
                    )
                    id = result.fetchone()[0]
                    return self.feedback_post_in_to_out(id, FeedbackForm)
        except Exception:
            return {"message": "Couldn't create feedback"}

    ## PUT ##
    def update(
        self, EmployeeFeedback_id: int, FeedbackForm: EmployeeFeedbackFormIn
    ) -> Union[EmployeeFeedbackFormOut, Error]:
        try:

            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE employee_form
                        SET employer_name = %s
                            , description = %s
                        WHEN id = %s
                        """,
                        [
                            FeedbackForm.employer_name,
                            FeedbackForm.description,
                            FeedbackForm.id,
                        ],
                    )
                    old_data = FeedbackForm.dict()
                    return EmployeeFeedbackFormOut(EmployeeFeedback_id, **old_data)
        except Exception:
            return {"message": "Could not update the Feedback"}

    def feedback_post_in_to_out(self, id: int, FeedbackForm: EmployeeFeedbackFormIn):
        old_data = FeedbackForm.dict()
        return EmployeeFeedbackFormOut(id=id, **old_data)

    # refactored function for GET#
    def record_to_employee_feedback_out(self, record):
        return EmployeeFeedbackFormOut(
            id=record[0], employer_name=record[1], description=record[2]
        )
