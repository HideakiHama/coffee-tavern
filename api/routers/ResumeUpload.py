from fastapi import APIRouter, UploadFile
router = APIRouter()

@router.post("/upload_resume/")
async def create_upload_resume(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}

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