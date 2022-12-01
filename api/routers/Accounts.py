# accounts.py  in the router folder
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator

from pydantic import BaseModel

from queries.accounts import AccountIn, AccountOut, AccountRepo, Error

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# import jwt
# import secrets
# from decouple import config

# JWT_SECRET = config("secret")
# JWT_ALGORITHM = config("algorithm")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# print("####", oauth2_scheme)


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: AccountOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post(
    "/api/accounts", tags=["Accounts"], response_model=AccountToken | HttpError
)
async def create_account(
    info: AccountIn,
    request: Request,
    response: Response,
    repo: AccountRepo = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)

    account = repo.create(info, hashed_password)
    form = AccountForm(username=info.email, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    return AccountToken(account=account, **token.dict())


@router.get("/api/get_account/{account_email}", tags=["Accounts"])
async def get_one_account(
    account_email: str, response: Response, repo: AccountRepo = Depends()
) -> AccountOut:
    AccountDetail = repo.get(account_email)
    if AccountDetail is None:
        response.status_code = 404
    return AccountDetail


@router.get("/api/get_all_account", tags=["Accounts"])
async def get_all_account(repo: AccountRepo = Depends()):
    return repo.get_all()


@router.delete("/api/delete_account", tags=["Accounts"])
async def delete_account(account_id: int, repo: AccountRepo = Depends()) -> bool:
    return repo.delete(account_id)
