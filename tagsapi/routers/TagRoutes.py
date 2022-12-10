from fastapi import APIRouter, Depends, Response
from queries.TagQueries import TagOut, TagIn, TagRepository, Error
from token_auth import get_current_user
from typing import Union, List

router = APIRouter()


# POST
# creating a new tag #
# account: dict = Depends(get_current_user)
@router.post("/create_tag_form", tags=["TagForm"], response_model=TagOut)
def create_tag(new_form: TagIn, repo: TagRepository = Depends(), account: dict = Depends(get_current_user)):
    return repo.create(new_form).dict()


# GET
# getting detail feedback from employer
@router.get(
    "/get-tag/{Tag_id}",
    tags=["TagForm"],
    response_model=Union[TagOut, Error],
)
def get_one_tag(
    Tag_id: int,
    response: Response,
    repo: TagRepository = Depends(), account: dict = Depends(get_current_user)
) -> TagOut:
    Tag = repo.get_one(Tag_id)
    if Tag is None:
        response.status_code = 404
    return Tag


# GET
# getting list of tags
@router.get(
    "/get_all_tags", tags=["TagForm"], response_model=Union[List[TagOut], Error]
)
def get_all(repo: TagRepository = Depends(), account: dict = Depends(get_current_user)):
    return repo.get_all()


# DELETE
# Delete tag
@router.delete("/delete_tag/{Tag_id}", tags=["TagForm"], response_model=bool)
def delete_tag(Tag_id: int, repo: TagRepository = Depends(), account: dict = Depends(get_current_user)):
    return repo.delete(Tag_id)
