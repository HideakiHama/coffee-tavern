from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import keepalive_kwargs
import os
from psycopg import connect


class Error(BaseModel):
    message: str


class Tags(BaseModel):
    id: int
    tag: str


class TagIn(BaseModel):
    tag: str


class TagOut(BaseModel):
    id: int
    tag: str


class TagRepository:
    # GET
    def get_one(self, tag: str) -> Optional[Tags]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                        , tag
                        FROM tags
                        WHERE tag = %s
                        """,
                        [tag],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_tag_out(record)
        except Exception:
            return {"message": "No tags available"}

    # GET
    def get_all(self) -> Union[List[TagOut], Error]:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
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
        except Exception:
            return {"message": "No tags available"}

    # POST
    def create(self, TagForm: TagIn) -> Tags:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
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
                    return Tags(id=id, tag=TagForm.tag)
        except Exception:
            return {"message": "Couldn't create Tag"}

    # DELETE
    def delete(self, Tag_id: int) -> bool:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
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
        return Tags(id=record[0], tag=record[1])
