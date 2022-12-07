from pydantic import BaseModel
from typing import Optional, List, Union, Literal
from queries.pool import keepalive_kwargs
import os
from psycopg import connect


class Error(BaseModel):
    message: str


class Account(BaseModel):
    id: int
    email: str
    hashed_password: str
    user_name: str
    role: str


class AccountIn(BaseModel):
    email: str
    password: str
    user_name: str
    role: Literal["Employee", "Employer"]


class AccountOut(BaseModel):
    id: int
    email: str
    user_name: str
    role: str


class AccountRepo:
    def get_all(self) -> List[AccountOut]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, email, user_name, role
                        FROM accounts
                        ORDER BY id
                        """
                    )
                    resultList = list(result)
                return [self.account_all(record) for record in resultList]
        except Exception as e:
            return {"message": "Could not get account"}

    def get(self, email: str) -> Optional[Account]:
        with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id, email, hashed_password, user_name, role
                    FROM accounts
                    WHERE email = %s
                    """,
                    [email],  # email variable get replace with %s
                )
                record = result.fetchone()
                if record is None:
                    return None
                return Account(
                    id=record[0],
                    email=record[1],
                    hashed_password=record[2],
                    user_name=record[3],
                    role=record[4],
                )

    def create(self, account: AccountIn, hashed_password: str) -> Account:
        with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO accounts
                        (email, hashed_password, user_name, role)
                    VALUES
                        (%s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [account.email, hashed_password, account.user_name, account.role],
                )
                id = result.fetchone()[0]
                return Account(
                    id=id,
                    email=account.email,
                    hashed_password=hashed_password,
                    user_name=account.user_name,
                    role=account.role,
                )

    def delete(self, account_id: int) -> bool:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM accounts
                        WHERE id = %s
                        """,
                        [account_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def account_all(self, record):
        return AccountOut(
            id=record[0], email=record[1], user_name=record[2], role=record[3]
        )
