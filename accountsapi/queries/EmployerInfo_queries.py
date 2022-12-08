from pydantic import BaseModel
from typing import List, Optional, Union
import os
from psycopg import connect
from queries.pool import keepalive_kwargs


class Error(BaseModel):
    message: str


class EmployerInfo(BaseModel):
    pass


class EmployerInfoIn(BaseModel):
    company_name: Optional[str]
    job_type: Optional[str]
    location: Optional[str]
    about: Optional[str]
    pic_url: Optional[str]

class EmployerInfoOut(BaseModel):
    company_name: Optional[str]
    job_type: Optional[str]
    location: Optional[str]
    about: Optional[str]
    pic_url: Optional[str]
    account_id: int


class EmployerInfoRepo:
    def create(self, info: EmployerInfoIn, account_id: int) -> Union[List[EmployerInfoOut], Error]:
        try:
            # connect the database
            with connect(conninfo=os.environ["DATABASE_URL"],
                         **keepalive_kwargs) as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO employer_info
                            (company_name, job_type, location, about, pic_url, account_id)
                        VALUES
                            (%s, %s, %s, %s, %s, %s)
                        """,
                        [
                            info.company_name,
                            info.job_type,
                            info.location,
                            info.about,
                            info.pic_url,
                            account_id
                        ],
                    )
                    return EmployerInfoOut(account_id=account_id, **info.dict())
        except Exception:
            return {"message": "Create did not work"}

    def get_one(self, account_id: int) -> Optional[EmployerInfoOut]:
        try:
            # connect the database
            with connect(conninfo=os.environ["DATABASE_URL"],
                         **keepalive_kwargs) as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                            company_name,
                            job_type,
                            location,
                            about,
                            pic_url,
                            account_id
                        FROM employer_info
                        WHERE account_id = %s
                        """,
                        [account_id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_employer_form_out(record)
        except Exception:
            return {"message": "Could not get employer info"}

    def update(self, info: EmployerInfoIn, account_id: int) -> Union[List[EmployerInfoOut], Error]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"],
                         **keepalive_kwargs) as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE employer_info
                        SET
                            company_name = %s,
                            job_type = %s,
                            location = %s,
                            about = %s,
                            pic_url = %s
                        WHERE account_id = %s
                        """,
                        [
                            info.company_name,
                            info.job_type,
                            info.location,
                            info.about,
                            info.pic_url,
                            account_id
                        ]
                    )
                    print(result)
                    return EmployerInfoOut(account_id=account_id, **info.dict())
        except Exception:
            return {"message": "Update did not work"}

    def record_employer_form_out(self, record):
        return EmployerInfoOut(
            company_name=record[0],
            job_type=record[1],
            location=record[2],
            about=record[3],
            pic_url=record[4],
            account_id=record[5]
        )
