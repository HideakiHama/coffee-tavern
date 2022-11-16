from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import date
from queries.pool import pool

class JobPostFormIn(BaseModel):
    position: str
    location: str
    from_date: date
    to_date: date
    tag: str
    description: Optional[str]

#response shape
class JobPostFormOut(BaseModel):
    id: int
    position: str
    location: str
    from_date: date
    to_date: date
    tag: str
    description: Optional[str]

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

    def record_JobForm_out(self, record):
        return VacationOut(
            id=record[0],
            position=record[1],
            from_date=record[2],
            to_date=record[3],
            tag=record[4],
            description=record[5]
        )
