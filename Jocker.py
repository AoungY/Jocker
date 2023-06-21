from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np



# 这是你的句频字典
frequencies = {
    "要不放暑假再回呢": 20 * 10,
    "回家过端午": 17 * 10,
    "你们都不回家吗": 16 * 10,
    "我已经好几年没在家过端午节了": 12 * 10,
    "我家多近啊": 16 * 10,
    "明天周三上完课我应该就回去了吧": 13 * 10,
    "那要不然我坐高铁": 12 * 10,
    "端午节这不回家吗": 10 * 10,
    "没事我自己回去": 13 * 10,
    "我是什么小丑啊":17 * 10,
    "我回不去了？":10 * 10,
    "Joker黄":13 * 10,
    "果然最爱的人伤我最深":10 * 10,
    "好像真回不去了":12 * 10,
    "到家了还能不接我":14 * 10,
    "不管 我去坐高铁去":11 * 10,
    "我不过是一个为了母亲考虑的周到的女儿":12 * 10,
}

# 加载图片并转化为NumPy数组
mask_image = Image.open("mask.png")
mask_array = np.array(mask_image)

# 创建词云对象并设定字体路径，词云形状，最大字号和背景颜色
wc = WordCloud(font_path='simhei.ttf', mask=mask_array, max_font_size=100, background_color='white',repeat=True,width=4000, height=4000)

# 生成词云
wc.generate_from_frequencies(frequencies)

# 设置图片的分辨率
dpi = 90000

# 展示词云
plt.figure(figsize=(800/dpi, 800/dpi), dpi=dpi)  # 这里的800是你期望的图片像素，你可以根据需要进行调整
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")  # 关闭坐标轴
plt.savefig("word_cloud.png", dpi=dpi)  # 保存词云图
plt.show()  # 显示词云图