from fastapi import APIRouter, Depends
from queries.EmployeeInfo_queries import EmployeeInfoIn, EmployeeInfoRepo, EmployeeInfoOut
from queries.accounts import AccountRepo

router = APIRouter()

@router.post("/users/{account_id}", tags=["User Info"])
def create_employee_info(
    employee_info: EmployeeInfoIn,
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
    repo1: AccountRepo = Depends(),
) -> EmployeeInfoOut:
    not_final = repo1.get(account_id)
    # print(type(not_final))
    return repo.create(employee_info, not_final)

@router.put("/users/{account_id}", tags=["User Info"])
def update_employee_info(
    employee_info: EmployeeInfoIn,
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
) -> EmployeeInfoOut:
    return repo.update(employee_info, account_id)
