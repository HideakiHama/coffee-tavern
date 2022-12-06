# from pydantic import BaseModel, ValidationError
# from typing import Optional, List, Union
# from queries.pool import pool

# class Error(BaseModel):
#     message : str

# class Tags(BaseModel):
#     id: int
#     tag: str

# class TagIn(BaseModel):
#     id: int
#     tag: str

# class TagOut(BaseModel):
#     id: int
#     tag: str


# class TagRepository:
#     #get
#     def tag_get(self, Tag_id: int) -> Optional[TagOut]:
#         try:
#             with pool.connections() as conn:
#                 with conn.cursor() as db:
#                     result = db.execute(
#                         """
#                         SELECT
#                         id,
#                         tags
#                         """,
#                         [
#                             Tag_id,
#                         ]    
#                     )
#                     record = result.fetchone()
#                     if record is None:
#                         return None
#                     return self.record_to_tag_out(record)
#         except Exception as e:
#             return {"message": "No tags available"}