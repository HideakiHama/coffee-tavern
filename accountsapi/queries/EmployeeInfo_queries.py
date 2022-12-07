from pydantic import BaseModel
from typing import List, Optional, Union
from queries.pool import keepalive_kwargs
import os
from psycopg import connect


class Error(BaseModel):
    message: str


class EmployeeInfoIn(BaseModel):
    career_title: Optional[str]
    location: Optional[str]
    education: Optional[str]
    about: Optional[str]


class EmployeeInfoOut(BaseModel):
    career_title: Optional[str]
    location: Optional[str]
    education: Optional[str]
    about: Optional[str]
    account_id: int


class EmployeeInfoRepo:
    def create(
        self, info: EmployeeInfoIn, account_id: int
    ) -> Union[List[EmployeeInfoOut], Error]:
        try:
            # connect the database
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO employee_info
                            (career_title, location, education, about, account_id)
                        VALUES
                            (%s, %s, %s, %s, %s)
                        """,
                        [
                            info.career_title,
                            info.location,
                            info.education,
                            info.about,
                            account_id,
                        ],
                    )
                    # get current user id
                    return EmployeeInfoOut(account_id=account_id, **info.dict())
        except Exception:
            return {"message": "Create did not work"}

    def get_one(self, account_id: int) -> Optional[EmployeeInfoOut]:
        try:
            # connect the database
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our SELECT statement
                    result = db.execute(
                        """
                        SELECT
                            career_title,
                            location,
                            education,
                            about,
                            account_id
                        FROM employee_info
                        WHERE account_id = %s
                        """,
                        [account_id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_employee_form_out(record)
        except Exception as e:
            return {"message": "Could not get employer info"}

    def update(
        self, info: EmployeeInfoIn, account_id: int
    ) -> Union[List[EmployeeInfoOut], Error]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE employee_info
                        SET
                            career_title = %s,
                            location = %s,
                            education = %s,
                            about = %s
                        WHERE account_id = (%s);
                        """,
                        [
                            info.career_title,
                            info.location,
                            info.education,
                            info.about,
                            account_id,
                        ],
                    )
                    return EmployeeInfoOut(account_id=account_id, **info.dict())
        except Exception:
            return {"message": "Update did not work"}

    def record_employee_form_out(self, record):
        return EmployeeInfoOut(
            career_title=record[0],
            location=record[1],
            education=record[2],
            about=record[3],
            account_id=record[4],
        )
