from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool
from datetime import date


class Error(BaseModel):
    message: str


class EmployeeFeedbackFormIn(BaseModel):
    employer_name: str
    date: date
    description: str


class EmployeeFeedbackFormOut(BaseModel):
    id: int
    employer_name: str
    date: date
    description: str


# SELECT id
# , employer_name
# , description
# FROM employee_form
# WHERE id = %s

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
                            , date
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
                        SELECT id, employer_name, date, description
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
                            (employer_name, date, description)
                        VALUES
                            (%s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            FeedbackForm.employer_name,
                            FeedbackForm.date,
                            FeedbackForm.description,
                        ],
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
                            , date = %s
                            , description = %s
                        WHERE id = %s
                        """,
                        [
                            FeedbackForm.employer_name,
                            FeedbackForm.date,
                            FeedbackForm.description,
                            EmployeeFeedback_id,
                        ],
                    )
                    return self.feedback_post_in_to_out(
                        EmployeeFeedback_id, FeedbackForm
                    )
        except Exception:
            return {"message": "Could not update the Feedback"}

    ## DELETE ##
    def delete(self, EmployeeFeedback_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM employee_form
                        WHERE id = %s
                        """,
                        [EmployeeFeedback_id],
                    )
                    return True
        except Exception:
            return False

    def feedback_post_in_to_out(self, id: int, FeedbackForm: EmployeeFeedbackFormIn):
        old_data = FeedbackForm.dict()
        return EmployeeFeedbackFormOut(id=id, **old_data)

    # refactored function for GET#
    def record_to_employee_feedback_out(self, record):
        return EmployeeFeedbackFormOut(
            id=record[0], employer_name=record[1], date=record[2], description=record[3]
        )
