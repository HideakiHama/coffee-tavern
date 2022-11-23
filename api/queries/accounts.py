from pydantic import BaseModel
from typing import Optional, List, Union, Literal
from queries.pool import pool


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
    role: Literal["Employer", "Employee"]


class AccountOut(BaseModel):
    id: int
    email: str
    user_name: str
    role: str


class AccountRepo:
    def get(self, email: str) -> Optional[Account]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                  SELECT id, email, hashed_password, user_name, role
                  FROM accounts
                  WHERE email = %s
                  """,
                    [email],
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
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO accounts
                        (email, hashed_password, user_name, role)
                    VALUES
                        (%s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                        account.email,
                        hashed_password,
                        account.user_name,
                        account.role,
                    ],
                )

                id = result.fetchone()[0]
                return Account(
                    id=id,
                    email=account.email,
                    hashed_password=hashed_password,
                    role=account.role,
                )
