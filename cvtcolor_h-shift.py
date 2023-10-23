# cvtcolor_h-shift.py
import numpy as np
import cv2 as cv

FN_INPUT = 'space-cat.jpg'

# 画像を読み込む
image = cv.imread(FN_INPUT)

# HSV 変換
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV_FULL)

# H チャンネルをシフトする
image_h = image_hsv[:, :, 0]
h_shift_deg = 90  # degree
image_hsv[:, :, 0] = image_h + (h_shift_deg * 255 / 360)

# BGR 変換
image_shift = cv.cvtColor(image_hsv, cv.COLOR_HSV2BGR_FULL)

# 保存
cv.imwrite(FN_INPUT + '_hshift.png', image_shift)

"""
Note:
    逆変換も cv.COLOR_***2BGR として指定できる。

    cv.COLOR_BGR2HSV は 0..179 なので、色相をずらす計算がしにくい。
    ここでは cv.COLOR_BGR2HSV_FULL で 0..255 の範囲に色相を変換する。
    そうすると、単純に数値を足したり引いたりするだけで、 255 + x は
    x という値になり、 -x は 255-x となるため、
    簡単に色相をずらすことができる。
"""
