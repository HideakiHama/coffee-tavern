from fastapi import APIRouter, Depends, Response
from typing import Union
from queries.EmployerInfo_queries import EmployerInfoRepo, EmployerInfoIn, EmployerInfoOut, Error
from queries.accounts import AccountRepo

router = APIRouter()

@router.post("/users/{account_id}/create_employer_info", tags=["User Info"])
def create_employer_info(
    employer_info: EmployerInfoIn,
    account_id: int,
    repo: EmployerInfoRepo = Depends(),
    repo1: AccountRepo = Depends()
) -> EmployerInfoOut:
    info = repo.create(employer_info, account_id).dict()
    info["account_id"] = repo1.get(account_id).dict()
    return info

@router.get('/users/{account_id}/get_employer_info', tags=["User Info"])
def get_employer_info_by_id(
    account_id: int, 
    repo: EmployerInfoRepo = Depends(),
    repo1: AccountRepo = Depends()
    ) -> EmployerInfoOut:
    EmployerInfo = repo.get_one(account_id).dict()
    EmployerInfo["account_id"] = repo1.get(account_id).dict()
    return EmployerInfo

@router.put("/users/{account_id}/update_employer_info", tags=["User Info"])
def update_employer_info(
    employer_info: EmployerInfoIn,
    account_id: int,
    repo: EmployerInfoRepo = Depends(),
    repo1: AccountRepo = Depends()
) -> EmployerInfoOut:
    Updated = repo.update(employer_info, account_id).dict()
    Updated["account_id"] = repo1.get(account_id).dict()
    return Updated