# PDF对比度增强器

- 某些扫描版PDF书籍颜色太浅，为了关爱您的眼睛健康，我帮你把它对比度调节一下，看起来舒服一点。
 Some Scanned version of PDF color not well, we decide to enhance their contrast for better reading experience.

- 实现思路是拆解所有的PDF为图片，然后利用Python进行批量图像处理。

# 运行
安装依赖库
```bash
pip install -r requirement.txt
```
安装poppler, 把bin文件添加到系统PATH目录，重启后才能用
https://blog.alivate.com.au/poppler-windows/

# 实现过程(搬砖过程)

目前在StackOverflow找到一个方法可以快速实现我的思路。
https://stackoverflow.com/a/50602577/10286351

核心代码如下
```python
npImage=np.array(Image.open("cartoon.png").convert("L"))

# Get brightness range - i.e. darkest and lightest pixels
min=np.min(npImage)        # result=144
max=np.max(npImage)        # result=216

# Make a LUT (Look-Up Table) to translate image values
LUT=np.zeros(256,dtype=np.uint8)
LUT[min:max+1]=np.linspace(start=0,stop=255,num=(max-min)+1,endpoint=True,dtype=np.uint8)
```
小小改一下
```python
# convert is no needed.
npImage = np.array(Image.open("SrcFolderTest/2.jpg")

min=np.min(npImage)+50 
max=np.max(npImage) 
```
这里的50是为了缩小阈值以获得更大的对比度，可以根据情况自己调。
再来看看这段代码。
看起来应该是应用了刚刚设定的阈值
```python
LUT=np.zeros(256,dtype=np.uint8)
LUT[min:max+1]=np.linspace(start=0,stop=255,num=(max-min)+1,endpoint=True,dtype=np.uint8)
# Apply LUT and save resulting image
imgRes = Image.fromarray(LUT[npImage]
```

OK, 最后跑一下，效果还可以。
![效果图1](https://github.com/tignioj/ChangePDFContrast/blob/main/result/res1.png?raw=true)
![效果图2](https://github.com/tignioj/ChangePDFContrast/blob/main/result/res2.png?raw=true)

# 性能(参考)
参数：质量50

原大小74.3M，454页的PDF用时1分钟26秒，导出大小83M
原大小139.6M, 679页的PDF用时4分25秒，导出大小176M


至于为什么文件会变大，可能需要更深层去了解一下了。

另外大部分时间都在花在PDF转数组上面，而不是图像处理上。


# 目录迁移
因为合成的时候仅仅合成里图片，原始PDF的其他任何信息都将丢失，这里提供一个目录迁移的办法。

## 1. 解压FreePic2Pdf.zip

## 2. 导出原始的目录
更改PDF->从PDF取书签

## 3. 写入到新的PDF
更改PDF->往PDF挂书签


# TODO
 - [ ] 标签导入（可以暂时用第三方工具FreePic2Pdf迁移）

# 另一种奇特思路：利用PS的动作+批处理。
