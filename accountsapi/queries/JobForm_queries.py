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
    # email: str
    # position: str
    full_name: str
    education: str
    account_id: Account | None = None
class ApplicantsOut(BaseModel):
    id: int
    # email: str
    # position: str
    full_name: str
    education: str
    employer_id: int
    account_id: Account | None = None

class JobFormRepository:
    def get_one(self, JobForm_id: int) -> Optional[JobPostFormOut]:
        print("EREE")
        try:
            # connect the database
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
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
        except Exception as e:
            return {"message": "Could not get that JobForm"}

    def get_all(self) -> Union[List[JobPostForm], Error]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
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
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
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
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
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
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
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

    def get_applicants(self) -> Union[List[ApplicantsOut], Error]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                with conn.cursor() as db:
                    result = db.execute(
                    """
                    SELECT id, account_id, employer_id, full_name, education
                    FROM applied
                    ORDER BY id
                    """
                    )
                    resultList = list(result)
                    print("RESULTLIST", resultList)
                y = [self.record_Applicants_all(record) for record in resultList]
                print("Y", y)
                return y
        except Exception as e:
            return {"message": "Could not get any applicants"}

    def send_application(self, Form: Applicants) -> ApplicantsOut:
        print("Form", Form)
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO applied
                            (account_id, full_name, education, employer_id)
                        VALUES
                            (%s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            Form.account_id["id"],
                            Form["full_name"],
                            Form["education"],
                            Form["employer_id"]
                        ],
                    )
                    id = result.fetchone()[0]
                    print(id)
                    print("FORM1111", form)
                    return self.Application_dict(id, Form)
                return result
        except Exception as e:
            print(e)
            return False

    def Job_Post_in_to_out(self, id: int, JobForm: JobPostFormIn):
        old_data = JobForm.dict()
        return JobPostFormOut1(id=id, **old_data)

    def Application_dict(self, id: int, JobForm: Applicants):
        # old_data = JobForm.dict()
        return Applicants(id=id, **old_data)

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
            description=record[5]
        )

    def record_Applicants_all(self, record):
        print(record)
        z = Applicants(
            id=record[0],
            position=record[1],
            full_name=record[2],
            education=record[3],
            applied_id=record[4]
        )
        print("Z", z)
