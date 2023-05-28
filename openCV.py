import cv2
import numpy as np
from fastapi import UploadFile, File
from pydantic import BaseModel
from main import app


img = cv2.imread('./images/02_Ysecdi.jpg')
cv2.imshow('OpenCV_image', img)
cv2.waitKey()
cv2.destroyWindow()


# class Analyzer(BaseModel):
#     filename: str
#     img_dimensions: str
#     encoded_img: str


#@app.post("/analyze", response_model=Analyzer)
#async def analyze_route(file: UploadFile = File(...)):
#    contents = await file.read()
#    nparr = np.fromstring(contents, np.uint8)
#    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#    img_dimensions = str(img.shape)
#    return_img = processImage(img)

#    encoded_img = cv2.imencode('.PNG', return_img)

#    return {
#        'filename': file.filename,
#        'dimensions': img_dimensions,
#        'encoded_img': endcoded_img,
#    }
