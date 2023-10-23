# cvtcolor_gray.py
import numpy as np
import cv2 as cv

FN_INPUT = 'space-cat.jpg'

# 画像を読み込む
image = cv.imread(FN_INPUT)

# グレースケール変換
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imwrite(FN_INPUT + '_gray.png', image_gray)


"""
Note:
    R, G, B チャンネルだけの画像もグレースケールのように見えるが、
    これは、人間の目の特性に基づいて計算されたものになっている。
"""
