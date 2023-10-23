# cvtcolor_hsv.py
import numpy as np
import cv2 as cv

FN_INPUT = 'space-cat.jpg'

# 画像を読み込む
image = cv.imread(FN_INPUT)

# HSV 変換
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
image_h = image_hsv[:, :, 0]
assert image_h.min() >= 0 and image_h.max() < 180
image_s = image_hsv[:, :, 1]
image_v = image_hsv[:, :, 2]

# グレースケール画像として保存
# H チャンネルは画像にしてもあまり意味がない
cv.imwrite(FN_INPUT + '_h.png', image_h)
cv.imwrite(FN_INPUT + '_s.png', image_s)
cv.imwrite(FN_INPUT + '_v.png', image_v)

"""
Note:
    OpenCV では、 H チャンネルを 0..179 の値で表現する。
    これは、通常 H は 0~360度で表すのだが、 
    8bit の最大値 255 に収まらないため、半分にする仕様となっている。
    なお、 cv.COLOR_BGR2HSV_FULL を指定した場合は、
    0..255 の範囲で表現される。

    HSV 以外の主な変換
    * cv.COLOR_BGR2XYZ
    * cv.COLOR_BGR2HSL
    * cv.COLOR_BGR2HLS
    * cv.COLOR_BGR2YCrCb
    * cv.COLOR_BGR2Lab
    * cv.COLOR_BGR2Luv
"""
