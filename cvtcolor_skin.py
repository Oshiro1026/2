# cvtcolor_skin.py
import numpy as np
import cv2 as cv

# 手などの肌が写った画像（※アジア系のオレンジに近いもの）
FN_INPUT = 'Hold_my_hand.jpg'

# 画像を読み込む
image = cv.imread(FN_INPUT)

# HSV 変換
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
image_h = image_hsv[:, :, 0]
assert image_h.min() >= 0 and image_h.max() < 180

# H チャンネルのなかでオレンジ色に近い部分を選ぶ
mask_h_orange = (image_h < 20) | (image_h > 160)

image_h_orange = image.copy()  # 加工用にコピーを作る
image_h_orange[mask_h_orange] = (0, 0, 0)  # 指定範囲以外を黒で埋める
# image_h_orange[~mask_h_orange] = (0, 0, 0)  # 条件（mask_h_orange）を満たさない範囲を黒で埋める
cv.imwrite(FN_INPUT + '_h_notorange.png', image_h_orange)


"""
Note:
    条件を満たす範囲を抽出する式では、Numpy の仕様で、
    必ず各不等式をカッコで囲んで、それらを & または | でつなぐ必要がある。
    & は「かつ」、 | は「または」、 ~ は条件の否定（反転）を表す。
"""
