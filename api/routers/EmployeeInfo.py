from fastapi import APIRouter, Depends
from queries.EmployeeInfo_queries import EmployeeInfoIn, EmployeeInfoRepo, EmployeeInfoOut

router = APIRouter()

@router.post("/users/{account_id}")
def create_employee_info(
    employee_info: EmployeeInfoIn,
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
) -> EmployeeInfoOut:
    return repo.create(employee_info, account_id)

@router.put("/users/{account_id}")
def update_employee_info(
    employee_info: EmployeeInfoIn,
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
) -> EmployeeInfoOut:
    return repo.update(employee_info, account_id)
