import os

import pdf2image as p2i
from pdf2image import convert_from_path
from pdf_enhance import pdfenhance
import time
import img2pdf as i2p
import tempfile

# ==== param list ===

pdf_file_path = 'origin.pdf'

# PDF quality,(0~100, A larger number consumes more memory)
pdf_output_quality = 50

# PDF contrast, (0~100, which decide color range, large number means more contrast)
contrast_level = 80

# ==== END ===

START_TIME = time.time()
prev = time.time()
def calTime(cal_all_ime=False):
    global prev
    cost = time.time() - prev
    if cal_all_ime:
        cost = time.time() - START_TIME

    m = int(cost / 60)
    rest = cost % 60

    if m >= 1:
        result = str(m) + "分" + str(round(rest, 2)) + "秒"
    else:
        result = str(round(cost, 2)) + "秒"
    prev = time.time()
    return result


print("======第一步：分解=====")
print("正在调用PDF转PIL数组的库函数，如果你电脑内存太小且PDF太大，有可能内存崩掉，那跟我没关系，自己找pdf2img的作者哭去，反正我32G不慌...")
print("耐心等一会儿...")
# filePath = 'origin.pdf'
if not os.path.isfile(pdf_file_path):
    raise "你pdf路径搞错了，检查一下是不是真的有这个东西'" + pdf_file_path +  "'"


with tempfile.TemporaryDirectory() as path:
    images = convert_from_path(pdf_file_path, output_folder=path)

    print("分解完成,用时" + calTime())
    print("======第二步：图片处理=====")
    i = 0
    imagesPath = []
    try:
        for img in images:
            print("正在处理第" + str(i + 1) + "张图片...")
            resImg = pdfenhance(img, contrast_level)
            i = i + 1
            if not os.path.isdir("temp"):
                os.mkdir("temp")
            imgPath = "temp/" + str(i) + ".jpg"
            imagesPath.append(imgPath)
            resImg.save(imgPath, quality=pdf_output_quality)
        print("处理完成, 用时" + calTime())
    except PermissionError:
        print("检查一下是不是temp里面有文件被打开了，没有的话删掉temp目录重来")
        exit(1)


print("======第三步, 合并=====")
print("正在调用img2pdf库以合并" + str(i) + "张图片为PDF")
with open('result_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".pdf", 'wb') as f:
    f.write(i2p.convert(imagesPath))
    print("处理完成, 文件名称：'" + f.name + "', 总共用时" + calTime(True))

