import os

import pdf2image as p2i
from pdf2image import convert_from_path
from pdf_enhance import pdfenhance
import img2pdf as i2p
import cv2 as cv
import imutils


# images = convert_from_path('origin.pdf')
images = convert_from_path('origin.pdf')

i = 0
imagesPath = []
for img in images:
    resImg = pdfenhance(img)
    npImg = cv.cvtColor(resImg, cv.COLOR_BGR2RGB)
    print(img.size, npImg.size)
    i=i+1
    imgPath = "temp/" + str(i) + ".jpg"
    imagesPath.append(imgPath)
    cv.imwrite(imgPath,npImg)
    # cvShow(resImg, str(i))

with open('res.pdf', 'wb') as f:
    f.write(i2p.convert(imagesPath))




