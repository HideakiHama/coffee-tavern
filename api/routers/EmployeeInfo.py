from fastapi import APIRouter, Depends, Response
from typing import Union
from queries.EmployeeInfo_queries import EmployeeInfoIn, EmployeeInfoRepo, EmployeeInfoOut, Error

router = APIRouter()

@router.post("/users/{account_id}/create_employee_info", tags=["User Info"])
def create_employee_info(
    employee_info: EmployeeInfoIn,
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
) -> EmployeeInfoOut:
    return repo.create(employee_info, account_id)

@router.get("/users/{account_id}/get_employee_info", tags=["User Info"], response_model=Union[EmployeeInfoOut, Error])
def get_employee_info_by_id(
    account_id: int, 
    response: Response, 
    repo: EmployeeInfoRepo = Depends()
    ) -> EmployeeInfoOut:
    EmployeeInfo = repo.get_one(account_id)
    if EmployeeInfo is None:
        response.status_code = 404
    return EmployeeInfo

@router.put("/users/{account_id}/update_employee_info", tags=["User Info"])
def update_employee_info(
    employee_info: EmployeeInfoIn,
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
) -> EmployeeInfoOut:
    return repo.update(employee_info, account_id)
