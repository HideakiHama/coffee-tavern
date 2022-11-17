from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import date
from queries.pool import pool


class Error(BaseModel):
    message: str
class JobPostFormIn(BaseModel):
    employer: str
    position: str
    location: str
    from_date: date
    to_date: date
    tag: str
    description: str

#response shape
class JobPostFormOut(BaseModel):
    id: int
    employer: str
    position: str
    location: str
    from_date: date
    to_date: date
    tag: str
    description: str

class Tags(BaseModel):
    tag: str

class JobFormRepository:
    def get_one(self, JobForm_id: int) -> Optional[JobPostFormOut]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our SELECT statement
                    result = db.execute(
                        """
                        SELECT id,
                            employer,
                            position,
                            from_date,
                            to_date,
                            tag,
                            description
                        FROM JobPostModel
                        WHERE id = %s
                        """,
                        [JobForm_id]
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_JobForm_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get that JobForm"}


    def create(self, JobForm: JobPostFormIn) -> Union[JobPostFormOut, Error]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO vacations
                            (employer, position, location, from_date, to_date, tags, description)
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            JobForm.employer,
                            JobForm.position,
                            JobForm.location,
                            JobForm.from_date,
                            JobForm.to_date,
                            JobForm.tags,
                            JobForm.description
                        ]
                    )
                    id = result.fetchone()[0]
                    # Return new data
                    # old_data = vacation.dict()
                    # return VacationOut(id=id, **old_data)
                    return self.Job_Post_in_to_out(id, JobForm)
        except Exception:
            return {"message": "Create did not work"}

    def Job_Post_in_to_out(self, id: int, JobForm: JobPostFormIn):
        old_data = JobForm.dict()
        return JobPostFormOut(id=id, **old_data)

    def record_JobForm_out(self, record):
        return JobPostFormOut(
            id=record[0],
            employer=record[1],
            position=record[2],
            from_date=record[3],
            to_date=record[4],
            tag=record[5],
            description=record[6]
        )
