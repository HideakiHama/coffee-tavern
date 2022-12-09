from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import date
from queries.accounts import Account
import os
from psycopg import connect
from queries.pool import keepalive_kwargs


class Error(BaseModel):
    message: str


class JobPostForm(BaseModel):
    id: int
    employer: str
    position: str
    location: str
    tag: str
    description: str
    account_id: int


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
    account_id: int


class JobPostFormOut1(BaseModel):
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


class Applicants(BaseModel):
    id: int
    full_name: str
    education: str
    employer_id: int
    account_id: int


class ApplicantsIn(BaseModel):
    id: int
    full_name: str
    education: str
    employer_id: int
    account_id: int


class ApplicantsOut(BaseModel):
    id: int
    full_name: str
    education: str
    employer_id: int
    account_id: Account | None = None


class JobFormRepository:
    def get_one(self, JobForm_id: int) -> Optional[JobPostFormOut]:
        print("EREE")
        try:
            # connect the database
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
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
                            description,
                            account_id
                        FROM jobs
                        WHERE id = %s
                        """,
                        [JobForm_id],
                    )
                    record = result.fetchone()
                    print("RECORD", record)
                    if record is None:
                        return None
                    return self.record_JobForm_out(record)
        except Exception:
            return {"message": "Could not get that JobForm"}

    def get_all(self) -> Union[List[JobPostForm], Error]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, employer, position, location, tag, description, account_id
                        FROM jobs
                        ORDER BY id
                        """
                    )
                    resultList = list(result)
                return [self.record_JobForm_all(record) for record in resultList]
        except Exception:
            return {"message": "Could not get any job form today"}

    def create(self, JobForm: JobPostFormIn, account_id: int) -> Union[List[JobPostFormOut2], Error]:
        try:
            # connect the database
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
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
                    return self.Job_Post_in_to_out(id, JobForm)
        except Exception:
            return {"message": "Create did not work"}

    def update(
        self, Form_id: int, UpdatedJobForm: JobPostFormIn
    ) -> Union[JobPostFormOut, Error]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
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
                    z = self.Job_Post_in_to_out(Form_id, UpdatedJobForm)
                    return z
        except Exception:
            return {"message": "Could not update the Job Form"}

    def delete(self, Form_id: int) -> bool:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM jobs
                        WHERE id = %s
                        """,
                        [Form_id],
                    )
                    return True
        except Exception:
            return False

    def get_all_applicants(self, curr_account_id: int) -> Union[List[ApplicantsIn], Error]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, account_id, employer_id, full_name, education
                        FROM applied
                        ORDER BY id
                        """
                    )
                    resultList = list(result)
                filtered = list(filter(lambda p: p[2] == curr_account_id, resultList))
            return [self.record_Applicants_all(record).dict() for record in filtered]
        except Exception:
            return {"message": "Could not get any applicants"}

    def send_application(self, Form: Applicants, employer_id: int) -> ApplicantsOut:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO applied
                            (account_id, employer_id, full_name, education)
                        VALUES
                            (%s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            Form.account_id["id"],
                            employer_id,
                            Form.full_name,
                            Form.education,
                        ],
                    )
                    id = result.fetchone()[0]
                    return self.Application_dict(id, Form, employer_id)
        except Exception:
            return False

    def delete_apply(self, apply_id: int) -> bool:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM applied
                        WHERE id = %s
                        """,
                        [apply_id],
                    )
                    return True
        except Exception:
            return False

    def Job_Post_in_to_out(self, id: int, JobForm: JobPostFormIn):
        old_data = JobForm.dict()
        return JobPostFormOut1(id=id, **old_data)

    def Application_dict(self, id: int, JobForm: ApplicantsOut, employer_id: int):
        old_data = JobForm.dict()
        old_data["employer_id"] = employer_id
        return ApplicantsOut(id=id, **old_data)

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
            account_id=record[8]
        )

    def record_JobForm_all(self, record):
        return JobPostForm(
            id=record[0],
            employer=record[1],
            position=record[2],
            location=record[3],
            tag=record[4],
            description=record[5],
            account_id=record[6]
        )

    def record_Applicants_all(self, record):
        return ApplicantsIn(
            id=record[0],
            account_id=record[1],
            employer_id=record[2],
            full_name=record[3],
            education=record[4],
        )
