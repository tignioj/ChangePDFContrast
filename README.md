# PDF对比度增强器

- 某些扫描版PDF书籍颜色太浅，为了关爱您的眼睛健康，我帮你把它对比度调节一下，看起来舒服一点。
 Some Scanned version of PDF color not well, we decide to enhance their contrast for better reading experience.

- 实现思路是拆解所有的PDF为图片，然后利用Python进行批量图像处理。



# 实现过程(搬砖过程)

目前在StackOverflow找到一个方法可以快速实现我的思路。
具体的原理，鬼知道，反正能跑。自己去看 https://stackoverflow.com/a/50602577/10286351

这个只实现了图片转换，后续会添加PDF拆解与合并。

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


# 另一种奇特思路：利用PS的动作+批处理。





