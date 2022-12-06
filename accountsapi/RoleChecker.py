from authenticator import secret_key
from queries.accounts import Account
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = jwt.decode(token, secret_key, algorithms="HS256")
    print("PAYLOAD", payload)
    role: str = payload["account"].get("role")
    if role is None:
        raise credentials_exception
    return role


class RoleChecker:
    def __init__(self, allowed_roles: str):
        self.allowed_roles = allowed_roles

    def __call__(self, role: Account = Depends(get_current_user)):
        if role:
            return self.allowed_roles in role
        return False
