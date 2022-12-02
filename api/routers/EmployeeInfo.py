from fastapi import APIRouter, Depends
from queries.EmployeeInfo_queries import EmployeeInfoIn, EmployeeInfoRepo, EmployeeInfoOut
from queries.accounts import AccountRepo

router = APIRouter()

@router.post("/users/{account_id}/create_employee_info", tags=["User Info"])
def create_employee_info(
    employee_info: EmployeeInfoIn,
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
    repo1: AccountRepo = Depends(),
) -> EmployeeInfoOut:
    not_final = repo1.get(account_id)
    # print(type(not_final))
    return repo.create(employee_info, not_final)

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