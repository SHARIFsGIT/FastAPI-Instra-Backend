from fastapi import APIRouter, UploadFile, File
import shutil

router = APIRouter(
    prefix='/file',
    tags=['file']
)


@router.post('/uploadfile')
def get_uploadfile(upload_file: UploadFile = File(...)):  # receiving uploaded file
    path = f"files/{upload_file.filename}"  # received file will save on files
    with open(path, 'w+b') as buffer:   # overwrite/create the file
        shutil.copyfileobj(upload_file.file, buffer)
    return {
        'filename': path,
        'type': upload_file.content_type
    }
