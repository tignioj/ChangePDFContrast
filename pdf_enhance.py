import numpy as  np
from PIL import Image


def pdfenhance(originImg, contrast_level):
    # Get brightness range - i.e. darkest and lightest pixels
    limg = originImg.convert("L")

    range_min=np.min(limg)+contrast_level
    range_max=np.max(limg)

    if range_min>range_max:
        range_min = np.min(limg)
    if range_max>255:
        range_max = 255

    LUT=np.zeros(256,dtype=np.uint8)
    LUT[range_min:range_max+1]=np.linspace(start=0,stop=255,num=(range_max-range_min)+1,endpoint=True,dtype=np.uint8)
    # Apply LUT and save resulting image
    imgRes = Image.fromarray(LUT[originImg])
    # npimg = np.array(imgRes)
    return imgRes


