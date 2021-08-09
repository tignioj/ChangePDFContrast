import numpy as np
import matplotlib.pyplot as plt
import imutils
import cv2 as cv
from PIL import Image

# img = cv.imread("SrcFolderTest/1.jpg")
# img = imutils.resize(img, 300)

# Process
def cvShow(img, title=""):
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    img = imutils.resize(img, 800)
    cv.imshow(title,img)



# npImage = np.array(Image.open("SrcFolderTest/1.jpg").convert("L"))
npImage = np.array(Image.open("SrcFolderTest/1.jpg"))

cvShow(npImage, "before")

# Get brightness range - i.e. darkest and lightest pixels
min=np.min(npImage)+50        # result=144
max=np.max(npImage)        # result=216


LUT=np.zeros(256,dtype=np.uint8)
LUT[min:max+1]=np.linspace(start=0,stop=255,num=(max-min)+1,endpoint=True,dtype=np.uint8)
# Apply LUT and save resulting image
imgRes = Image.fromarray(LUT[npImage])
npimg = np.array(imgRes.convert("RGB"))


cvShow(npimg, "after")
cv.waitKey(0)
cv.destroyAllWindows()
Image.fromarray(LUT[npImage]).save('result.jpg')


# End
