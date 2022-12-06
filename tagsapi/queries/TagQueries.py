from pydantic import BaseModel, ValidationError
from typing import Optional, List, Union
from queries.pool import pool


class Error(BaseModel):
    message: str


# class Tags(BaseModel):
#     id: int
#     tag: str


class TagIn(BaseModel):
    tag: str


class TagOut(BaseModel):
    id: int
    tag: str


class TagRepository:
    ## GET ##
    def get_one(self, Tag_id: int) -> Optional[TagOut]:
        try:
            with pool.connections() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                        , tag
                        FROM tags
                        WHERE id = %s
                        """,
                        [
                            Tag_id,
                        ],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_tag_out(record)
        except Exception as e:
            return {"message": "No tags available"}

    ## GET ##
    def get_all(self) -> Union[List[TagOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, tag
                        FROM tags
                        ORDER BY id
                        """
                    )
                    resultList = list(result)
                return [
                    self.record_to_tag_out(record) for record in resultList
                ]  # refactored
        except Exception as e:
            return {"message": "No tags available"}

    ## POST ##
    def create(self, TagForm: TagIn) -> TagOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO tags
                            (tag)
                        VALUES
                            (%s)
                        RETURNING id;
                        """,
                        [TagForm.tag],
                    )
                    id = result.fetchone()[0]
                    return self.feedback_post_in_to_out(id, TagForm)
        except Exception:
            return {"message": "Couldn't create Tag"}

    ## DELETE ##
    def delete(self, Tag_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM tags
                        WHERE id = %s
                        """,
                        [Tag_id],
                    )
                    return True
        except Exception:
            return False

    def feedback_post_in_to_out(self, id: int, TagForm: TagIn):
        old_data = TagForm.dict()
        return TagOut(id=id, **old_data)

    # refactored function for GET#
    def record_to_tag_out(self, record):
        return TagOut(id=record[0], tag=record[1])