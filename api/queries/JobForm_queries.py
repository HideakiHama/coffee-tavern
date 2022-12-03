from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import date
from queries.pool import pool
from queries.accounts import Account


class Error(BaseModel):
    message: str


class JobPostForm(BaseModel):
    id: int
    employer: str
    position: str
    location: str
    tag: str
    description: str


class JobPostFormIn(BaseModel):
    employer: str
    position: str
    location: str
    from_date: date
    to_date: date
    tag: str
    description: str


# response shape
class JobPostFormOut(BaseModel):
    id: int
    employer: str
    position: str
    location: str
    from_date: date
    to_date: date
    tag: str
    description: str


class JobPostFormOut2(BaseModel):
    id: int
    employer: str
    position: str
    location: str
    from_date: date
    to_date: date
    tag: str
    description: str
    account_id: Account | None = None


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
                            location,
                            from_date,
                            to_date,
                            tag,
                            description
                        FROM jobs
                        WHERE id = %s
                        """,
                        [JobForm_id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_JobForm_out(record)
        except Exception as e:
            return {"message": "Could not get that JobForm"}

    def get_all(self) -> Union[List[JobPostForm], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, employer, position, location, tag, description
                        FROM jobs
                        ORDER BY id
                        """
                    )
                    resultList = list(result)
                return [self.record_JobForm_all(record) for record in resultList]

        except Exception as e:
            return {"message": "Could not get any job form today"}

    def create(self, JobForm: JobPostFormIn, account_id: int) -> Union[List[JobPostFormOut2], Error]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO jobs
                            (employer, position, location, from_date, to_date, tag, description, account_id)
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            JobForm.employer,
                            JobForm.position,
                            JobForm.location,
                            JobForm.from_date,
                            JobForm.to_date,
                            JobForm.tag,
                            JobForm.description,
                            account_id
                        ],
                    )
                    id = result.fetchone()[0]
                    print("ID", id)
                    return self.Job_Post_in_to_out(id, JobForm)
        except Exception:
            return {"message": "Create did not work"}

    def update(
        self, Form_id: int, UpdatedJobForm: JobPostFormIn
    ) -> Union[JobPostFormOut, Error]:
        print("UpdatedJobForm", UpdatedJobForm)
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE jobs
                        SET employer = %s,
                        position = %s,
                        location = %s,
                        from_date = %s,
                        to_date = %s,
                        tag = %s,
                        description = %s
                        WHERE id = %s
                        """,
                        [
                            UpdatedJobForm.employer,
                            UpdatedJobForm.position,
                            UpdatedJobForm.location,
                            UpdatedJobForm.from_date,
                            UpdatedJobForm.to_date,
                            UpdatedJobForm.tag,
                            UpdatedJobForm.description,
                            Form_id,
                        ],
                    )
                    return self.Job_Post_in_to_out(Form_id, UpdatedJobForm)
        except Exception:
            return {"message": "Could not update the Job Form"}

    def delete(self, Form_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM jobs
                        WHERE id = %s
                        """,
                        [Form_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def Job_Post_in_to_out(self, id: int, JobForm: JobPostFormIn):
        old_data = JobForm.dict()
        print(old_data)
        return JobPostFormOut(id=id, **old_data)

    def record_JobForm_out(self, record):
        return JobPostFormOut(
            id=record[0],
            employer=record[1],
            position=record[2],
            location=record[3],
            from_date=record[4],
            to_date=record[5],
            tag=record[6],
            description=record[7],
        )

    def record_JobForm_all(self, record):
        return JobPostForm(
            id=record[0],
            employer=record[1],
            position=record[2],
            location=record[3],
            tag=record[4],
            description=record[5]
        )
