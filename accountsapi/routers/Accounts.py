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
    print("HEHEHE")
    hashed_password = authenticator.hash_password(info.password)
    print("PLZ")
    account = repo.create(info, hashed_password)
    print(account)
    form = AccountForm(username=info.email, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    x = AccountToken(account=account, **token.dict())
    print("XXXXX", x)
    return x


@router.get("/api/get_account/{account_id}", tags=["Accounts"])
async def get_one_account(
    account_id: int, response: Response, repo: AccountRepo = Depends()
) -> AccountOut:
    AccountDetail = repo.get(account_id)
    if AccountDetail is None:
        response.status_code = 404
    return AccountDetail


@router.get("/api/get_all_account", tags=["Accounts"])
async def get_all_account(repo: AccountRepo = Depends()):
    return repo.get_all()


@router.delete("/api/delete_account", tags=["Accounts"])
async def delete_account(account_id: int, repo: AccountRepo = Depends()) -> bool:
    return repo.delete(account_id)


@router.get("/get_token", response_model=AccountToken | None)
async def get_token(
    request: Request, account: dict = Depends(authenticator.get_current_account_data)
) -> AccountToken | None:
    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }
