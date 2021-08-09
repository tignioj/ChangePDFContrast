import numpy as  np
from PIL import Image
def pdfenhance(originImg):
    # Get brightness range - i.e. darkest and lightest pixels
    limg = originImg.convert("L")

    min=np.min(limg)+50
    max=np.max(limg)

    LUT=np.zeros(256,dtype=np.uint8)
    LUT[min:max+1]=np.linspace(start=0,stop=255,num=(max-min)+1,endpoint=True,dtype=np.uint8)
    # Apply LUT and save resulting image
    imgRes = Image.fromarray(LUT[originImg])
    npimg = np.array(imgRes)

    return npimg
