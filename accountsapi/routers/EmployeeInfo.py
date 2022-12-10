from fastapi import APIRouter, Depends
from queries.EmployeeInfo_queries import (
    EmployeeInfoIn,
    EmployeeInfoRepo,
    EmployeeInfoOut,
)
from queries.accounts import AccountRepo
from RoleChecker import RoleChecker
from authenticator import authenticator

router = APIRouter()

checker = RoleChecker("Employer")


@router.post("/users/{account_id}/create_employee_info", tags=["User Info"])
def create_employee_info(
    employee_info: EmployeeInfoIn,
    repo: EmployeeInfoRepo = Depends(),
    account: dict = Depends(authenticator.get_current_account_data),
) -> EmployeeInfoOut:
    info = repo.create(employee_info, account["id"]).dict()
    info["account_id"] = account
    return info


@router.get("/users/{account_id}/get_employee_info", tags=["User Info"])
def get_employee_info_by_id(
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
    repo1: AccountRepo = Depends(),
) -> EmployeeInfoOut:
    print("Hello")
    info = repo.get_one(account_id)
    print("Info", info)
    if info:
        EmployeeInfo = repo.get_one(account_id).dict()
        return EmployeeInfo
    else:
        print("unable to find info")
        return {}
    # EmployeeInfo["account_id"] = repo1.getId(account_id).dict()


@router.put("/users/{account_id}/update_employee_info", tags=["User Info"])
def update_employee_info(
    employee_info: EmployeeInfoIn,
    repo: EmployeeInfoRepo = Depends(),
    account: dict = Depends(authenticator.get_current_account_data),
) -> EmployeeInfoOut:
    # final = repo.get_one(account["id"])
    Updated = repo.update(employee_info, account["id"]).dict()
    print("updated", Updated)
    # Updated["account_id"] = final.account_id
    return Updated


# GET #
# Get all the Employee Profile
@router.get("/get_all_employee_profile", tags=["User Info"])
def get_all_employee_profile(
    account: dict = Depends(authenticator.get_current_account_data),
    repo: EmployeeInfoRepo = Depends(),
):
    return repo.get_all_profile()
