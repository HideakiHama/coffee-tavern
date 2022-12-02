from pydantic import BaseModel
from typing import List, Optional, Union
from queries.pool import pool

class Error(BaseModel):
    message: str
    
class EmployerInfo(BaseModel):
    pass
    
class EmployerInfoIn(BaseModel):
    job_type: Optional[str]
    location: Optional[str]
    about: Optional[str]

class EmployerInfoOut(BaseModel):
    job_type: Optional[str]
    location: Optional[str]
    about: Optional[str]
    account_id: int
    
class EmployerInfoRepo:
    
    def create(self, info: EmployerInfoIn, account_id: int) -> Union[List[EmployerInfoOut], Error]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO employer_info
                            (job_type, location, about, account_id)
                        VALUES
                            (%s, %s, %s, %s)
                        """,
                        [
                            info.job_type,
                            info.location,
                            info.about,
                            account_id
                        ],
                    )
                    # get current user id
                    return EmployerInfoOut(account_id=account_id, **info.dict())
        except Exception:
            return {"message": "Create did not work"}
        
    def get_one(self, account_id: int) -> Optional[EmployerInfoOut]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our SELECT statement
                    result = db.execute(
                        """
                        SELECT
                            job_type,
                            location,
                            about,
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
        except Exception as e:
            return {"message": "Could not get employer info"}
        
    def update(self, info: EmployerInfoIn, account_id: int) -> Union[List[EmployerInfoOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE employer_info
                        SET
                            job_type = %s,
                            location = %s,
                            about = %s
                        WHERE account_id = %s
                        """,
                        [
                            info.job_type,
                            info.location,
                            info.about,
                            account_id
                        ]
                    )
                    return EmployerInfoOut(account_id=account_id, **info.dict())
        except Exception:
            return {"message": "Update did not work"}
        
    def record_employer_form_out(self, record):
        return EmployerInfoOut(
            job_type=record[0],
            location=record[1],
            about=record[2],
            account_id=record[3]
        )