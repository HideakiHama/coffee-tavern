from pydantic import BaseModel
from typing import Optional, List, Literal
from queries.pool import keepalive_kwargs
import os
from psycopg import connect


class Error(BaseModel):
    message: str


class Account(BaseModel):
    id: int
    user_name: str
    email: str
    hashed_password: str
    role: str


class AccountIn(BaseModel):
    user_name: str
    email: str
    password: str
    role: Literal["Employee", "Employer"]


class AccountOut(BaseModel):
    id: int
    user_name: str
    email: str
    role: str


class AccountRepo:
    def get_all(self) -> List[AccountOut]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"],
                         **keepalive_kwargs) as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, user_name, email, role
                        FROM accounts
                        ORDER BY id
                        """
                    )
                    resultList = list(result)
                return [self.account_all(record) for record in resultList]
        except Exception:
            return {"message": "Could not get account"}

    def get(self, user_name: str) -> Optional[Account]:
        with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id, user_name, email, hashed_password, role
                    FROM accounts
                    WHERE user_name = %s
                    """,
                    [user_name],
                )
                record = result.fetchone()
                if record is None:
                    return None
                return Account(
                    id=record[0],
                    user_name=record[1],
                    email=record[2],
                    hashed_password=record[3],
                    role=record[4],
                )

    # For Getting account by user ID (/api/get_account/{account_id})
    def getId(self, user_name: str) -> Optional[Account]:
        with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id, user_name, email, hashed_password, role
                    FROM accounts
                    WHERE id = %s
                    """,
                    [user_name],
                )
                record = result.fetchone()
                if record is None:
                    return None
                return Account(
                    id=record[0],
                    user_name=record[1],
                    email=record[2],
                    hashed_password=record[3],
                    role=record[4],
                )

    def create(self, account: AccountIn, hashed_password: str) -> Account:
        with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO accounts
                        (user_name, email, hashed_password, role)
                    VALUES
                        (%s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [account.user_name, account.email, hashed_password, account.role],
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
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM accounts
                        WHERE id = %s
                        """,
                        [account_id],
                    )
                    return True
        except Exception:
            return False

    def account_all(self, record):
        return AccountOut(
            id=record[0], user_name=record[1], email=record[2], role=record[3]
        )
