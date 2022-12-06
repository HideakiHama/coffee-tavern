from fastapi import APIRouter, Depends, Response
from queries.TagQueries import TagOut, TagIn, TagRepository, Error
from typing import List, Union

router = APIRouter()

## POST ##
# creating a new tag #
@router.post("/create_tag_form", tags=["TagForm"], response_model=TagOut)
def create_tag(new_form: TagOut, repo: TagRepository = Depends()):
    return repo.create(new_form)


## GET ##
# getting detail feedback from employer
@router.get(
    "/get-tag/{Tag_id}",
    tags=["TagForm"],
    response_model=Union[TagOut, Error],
)
def get_one_employer_feedback_form(
    Tag_id: int,
    response: Response,
    repo: TagRepository = Depends(),
) -> TagOut:
    Tag = repo.get_one(Tag_id)
    if Tag is None:
        response.status_code = 404
    return Tag


## GET ##
# getting list of tags
@router.get(
    "/get_all_tags", tags=["TagForm"], response_model=Union[List[TagOut], Error]
)
def get_all(repo: TagRepository = Depends()):
    return repo.get_all()


## DELETE ##
# Delete tag #
@router.delete("/delete_tag/{Tag_id}", tags=["TagForm"], response_model=bool)
def delete_tag(Tag_id: int, repo: TagRepository = Depends()):
<<<<<<< HEAD
    return repo.delete(Tag_id)
=======
    return repo.delete(Tag_id)
>>>>>>> 812776103fc5131fbea437ce046eab0026790aad
