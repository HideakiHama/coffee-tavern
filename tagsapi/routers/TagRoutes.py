from fastapi import  APIRouter, Depends
from queries import TagOut, Tagin , TagRepository, Tags, Error
from typing import List, Union

router = APIRouter()


@router.post("/create_tag_form/{tag_id}", tags=["TagForm"], response_model=TagOut)
def create_tag(
    tag_id: int, 
    repo: TagRepository = Depends()
):
    return repo.post.post(tag_id)

@router.delete("/delete_tag/{tag_id}", tags=["TagForm"], response_model=bool)
def delete_tag(
    tag_id: int,
    repo: TagRepository = Depends()
):
    return repo.delete(tag_id)

@router.get("/get_all_tags/{tag_id}", tags=["TagForm"], response_model=Union[List[Tags], Error])
def get_all(
    tag_id: int,
    repo: TagRepository = Depends()
): 
    return repo.get_all(tag_id)