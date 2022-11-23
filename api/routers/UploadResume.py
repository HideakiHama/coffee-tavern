from fastapi import APIRouter, File, UploadFile
from typing import List
import shutil
# from fastapi.responses import HTMLResponse

router = APIRouter()

# @router.post("/files/")
# async def upload_files(file: UploadFile = File(...)):
#     return {"file_name": file.filename}


@router.post("/upload_resume/")
async def resume_upload(file: UploadFile = File(...)):
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename}


# @router.post("/upload_resume/")
# async def create_upload_resume(file: UploadFile | None = None):
#     if not file:
#         return {"message": "No upload file sent"}
#     else:
#         return {"filename": file.filename}

# @router.post("/files/")
# async def create_file(file: bytes | None = File(default=None)):
#     if not file:
#         return {"message": "No file sent"}
#     else:
#         return {"file_size": len(file)}


# @router.post("/upload_resumes/") #uploading multiple?
# async def upload_resumes(files: List[UploadFile]):
#     return {"filenames": [file.filename for file in files]}

# @router.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type=file" multiple>
# <input type="Submit">
# </form>
# <form action="uploadfiles/" enctype=multipart/form-data" method="post">
# <input name="files" type="files" multiple>
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)