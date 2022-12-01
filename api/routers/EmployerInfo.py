from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
from queries.EmployerInfo_queries import EmployerInfoRepo, EmployerInfoIn, EmployerInfoOut, Error

router = APIRouter()

@router.post("/users/{account_id}/create_employer_info", tags=["User Info"])
def create_employer_info(
    employer_info: EmployerInfoIn,
    account_id: int,
    repo: EmployerInfoRepo = Depends(),
) -> EmployerInfoOut:
    return repo.create(employer_info, account_id)

@router.get('/users/{account_id}/get_employer_info', tags=["User Info"], response_model=Union[EmployerInfoOut, Error])
def get_employer_info_by_id(
    account_id: int, 
    response: Response, 
    repo: EmployerInfoRepo = Depends()
    ) -> EmployerInfoOut:
    EmployerInfo = repo.get_one(account_id)
    if EmployerInfo is None:
        response.status_code = 404
    return EmployerInfo

@router.put("/users/{account_id}/update_employer_info", tags=["User Info"])
def update_employer_info(
    employer_info: EmployerInfoIn,
    account_id: int,
    repo: EmployerInfoRepo = Depends(),
) -> EmployerInfoOut:
    return repo.update(employer_info, account_id)