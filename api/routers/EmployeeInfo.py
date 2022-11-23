from fastapi import APIRouter, Depends
from queries.EmployeeInfo_queries import EmployeeInfoIn, EmployeeInfoRepo, EmployeeInfoOut
# from queries.JobForm_queries import (
#     JobPostFormIn,
#     JobPostFormOut,
#     JobFormRepository,
#     Tags,
#     Error,
#     JobPostForm
# )

router = APIRouter()

@router.post("/users/{account_id}/employee_info")
def create_employee_info(
    employee_info: EmployeeInfoIn,
    account_id: int,
    repo: EmployeeInfoRepo = Depends(),
) -> EmployeeInfoOut:
    return repo.create(employee_info, account_id)