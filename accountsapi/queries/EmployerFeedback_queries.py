from pydantic import BaseModel, ValidationError
from typing import Optional, List, Union
from queries.pool import keepalive_kwargs
import os
from psycopg import connect
from datetime import date
from queries.accounts import Account


class Error(BaseModel):
    message: str


class EmployerFeedbackFormIn(BaseModel):
    employee_name: str
    date: date
    description: str


class EmployerFeedbackFormOut(BaseModel):
    id: int
    employee_name: str
    date: date
    description: str
    account_id: Account | None = None


class EmployerFeedbackFormOut2(BaseModel):
    id: int
    employee_name: str
    date: date
    description: str
    account_id: int


# Employer Feedback of Employee
class EmployerFeedbackRepository:
    ## GET ##
    def get_one(self, EmployerFeedback_id: int) -> Optional[EmployerFeedbackFormOut]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                        , employee_name
                        , date
                        , description
                        , account_id
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
    def get_all(self, account_id: int) -> Union[List[EmployerFeedbackFormOut2], Error]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, employee_name, date, description, account_id
                        FROM employer_form
                        ORDER BY id
                        """
                    )
                    resultList = list(result)

                y = [
                    self.record_to_employer_feedback_out(record).dict()
                    for record in resultList
                ]

                list1 = []
                for i in y:
                    if i["account_id"] == account_id:
                        list1.append(i)

                return list1
        except Exception as e:
            return {"message": "Could not get employer feedback form"}

    ## POST ##
    def create(
        self, FeedbackForm: EmployerFeedbackFormIn, account_id: int
    ) -> EmployerFeedbackFormOut:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO employer_form
                            (employee_name, date, description, account_id)
                        VALUES
                            (%s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            FeedbackForm.employee_name,
                            FeedbackForm.date,
                            FeedbackForm.description,
                            account_id,
                        ],
                    )
                    id = result.fetchone()[0]
                return self.feedback_post_in_to_out(id, FeedbackForm)
        except ValidationError:
            return {"message": "Couldn't create feedback"}

    ## PUT ##
    def update(
        self, EmployerFeedback_id: int, FeedbackForm: EmployerFeedbackFormIn
    ) -> Union[EmployerFeedbackFormOut2, Error]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE employer_form
                        SET employee_name = %s
                            , date = %s
                            , description = %s
                        WHERE id = %s
                        """,
                        [
                            FeedbackForm.employee_name,
                            FeedbackForm.date,
                            FeedbackForm.description,
                            EmployerFeedback_id,
                        ],
                    )
                    return self.feedback_post_in_to_out(
                        EmployerFeedback_id, FeedbackForm
                    )
        except Exception:
            return {"message": "Could not update the Feedback"}

    ## DELETE ##
    def delete(self, EmployerFeedback_id: int) -> bool:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM employer_form
                        WHERE id = %s
                        """,
                        [EmployerFeedback_id],
                    )
                    return True
        except Exception:
            return False

    def feedback_post_in_to_out(self, id: int, FeedbackForm: EmployerFeedbackFormIn):
        old_data = FeedbackForm.dict()
        return EmployerFeedbackFormOut(id=id, **old_data)

    # refactored function for # GET #
    def record_to_employer_feedback_out(self, record):

        return EmployerFeedbackFormOut2(
            id=record[0],
            employee_name=record[1],
            date=record[2],
            description=record[3],
            account_id=record[4],
        )
