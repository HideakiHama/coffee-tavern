from pydantic import BaseModel
from typing import List, Optional, Union
import os
from psycopg import connect
from queries.pool import keepalive_kwargs


class Error(BaseModel):
    message: str


class EmployeeInfoIn(BaseModel):
    full_name: Optional[str]
    career_title: Optional[str]
    location: Optional[str]
    education: Optional[str]
    about: Optional[str]
    pic_url: Optional[str]


class EmployeeInfoOut(BaseModel):
    full_name: Optional[str]
    career_title: Optional[str]
    location: Optional[str]
    education: Optional[str]
    about: Optional[str]
    pic_url: Optional[str]
    account_id: int


class EmployeeInfoRepo:
    def create(
        self, info: EmployeeInfoIn, account_id: int
    ) -> Union[List[EmployeeInfoOut], Error]:
        try:
            # connect the database
            with connect(
                conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs
            ) as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO employee_info
                            (full_name, career_title, location, education, about, pic_url, account_id)
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s)
                        """,
                        [
                            info.full_name,
                            info.career_title,
                            info.location,
                            info.education,
                            info.about,
                            info.pic_url,
                            account_id,
                        ],
                    )
                    print(result)
                    return EmployeeInfoOut(account_id=account_id, **info.dict())
        except Exception:
            return {"message": "Create did not work"}

    def get_one(self, account_id: int) -> Optional[EmployeeInfoOut]:
        try:
            # connect the database
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our SELECT statement
                    result = db.execute(
                        """
                        SELECT
                            full_name,
                            career_title,
                            location,
                            education,
                            about,
                            pic_url,
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
            print(e)
            return {"message": "Could not get employee info"}

    def update(
        self, info: EmployeeInfoIn, account_id: int
    ) -> Union[List[EmployeeInfoOut], Error]:
        try:
            with connect(
                conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs
            ) as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE employee_info
                        SET
                            full_name = %s,
                            career_title = %s,
                            location = %s,
                            education = %s,
                            about = %s,
                            pic_url = %s
                        WHERE account_id = (%s);
                        """,
                        [
                            info.full_name,
                            info.career_title,
                            info.location,
                            info.education,
                            info.about,
                            info.pic_url,
                            account_id,
                        ],
                    )
                    print(result)
                    return EmployeeInfoOut(account_id=account_id, **info.dict())
        except Exception:
            return {"message": "Update did not work"}

    # GET #
    def get_all_profile(self) -> List[EmployeeInfoOut]:
        try:
            with connect(
                conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs
            ) as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                            full_name,
                            career_title,
                            location,
                            education,
                            about,
                            pic_url,
                            account_id
                        FROM employee_info
                        ORDER BY full_name
                        """
                    )
                    resultList = list(result)
                return [self.record_employee_form_out(record) for record in resultList]
        except Exception:
            return {"message": "Could not get list of employee"}

    def record_employee_form_out(self, record):
        return EmployeeInfoOut(
            full_name=record[0],
            career_title=record[1],
            location=record[2],
            education=record[3],
            about=record[4],
            pic_url=record[5],
            account_id=record[6],
        )
