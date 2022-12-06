from fastapi import APIRouter, Depends, Response, HTTPException, status
from typing import Union
from queries.EmployeeInfo_queries import EmployeeInfoIn, EmployeeInfoRepo, EmployeeInfoOut, Error
from queries.accounts import AccountRepo
from RoleChecker import RoleChecker

router = APIRouter()

checker = RoleChecker("Employer")

@router.post("/users/{account_id}/create_employee_info", tags=["User Info"])
def create_employee_info(
    employee_info: EmployeeInfoIn,
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
    repo1: AccountRepo = Depends(),
    # checked_role: bool = Depends(checker),
) -> EmployeeInfoOut:
    # credentials_exception = HTTPException(
    #     status_code=status.HTTP_403_FORBIDDEN,
    #     detail="You are an employer, you should fill out employer info"
    # )
    # if checked_role:
    info = repo.create(employee_info, account_id).dict()
    info["account_id"] = repo1.get(account_id).dict()
    return info
    # raise credentials_exception

@router.get("/users/{account_id}/get_employee_info", tags=["User Info"])
def get_employee_info_by_id(
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
    repo1: AccountRepo = Depends()
    ) -> EmployeeInfoOut:
    EmployeeInfo = repo.get_one(account_id).dict()
    EmployeeInfo["account_id"] = repo1.get(account_id).dict()
    return EmployeeInfo

@router.put("/users/{account_id}/update_employee_info", tags=["User Info"])
def update_employee_info(
    employee_info: EmployeeInfoIn,
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
    repo1: AccountRepo = Depends()
) -> EmployeeInfoOut:
    Updated = repo.update(employee_info, account_id).dict()
    Updated["account_id"] = repo1.get(account_id).dict()
    return Updated
