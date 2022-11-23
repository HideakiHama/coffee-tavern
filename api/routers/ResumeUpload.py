from fastapi import APIRouter, UploadFile, File
from typing import List
import shutil
router = APIRouter()

@router.post("/resume/")
async def create_upload_resume(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}

# @router.post("/resume/")
# async def upload_resume(files: UploadFile = File(...)):
#     with open(f'{file.filename}')

## This is for adding multiple files -- maybe use for profile picture
@router.post("/img/")
async def upload_image(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', "wb") as buffer:
            shutil.copyfilobj(img.file, buffer)

    return {"filename": "Good"}

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