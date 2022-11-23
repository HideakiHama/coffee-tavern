from fastapi import APIRouter, Depends
from queries.EmployeeInfo_queries import EmployeeInfoIn, EmployeeInfoRepo
# from queries.JobForm_queries import (
#     JobPostFormIn,
#     JobPostFormOut,
#     JobFormRepository,
#     Tags,
#     Error,
#     JobPostForm
# )

router = APIRouter()

@router.post("/users/{id}/employee_info")
def create_employee_info(
    employee_info: EmployeeInfoIn,
    repo: EmployeeInfoRepo = Depends()
):
    return repo.create(employee_info)