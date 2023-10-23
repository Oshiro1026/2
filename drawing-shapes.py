""" 図形の描画 """
import numpy as np
import cv2 as cv


# 作る画像の大きさ（横 W, 縦 H ピクセル）
W, H = (800, 600)

# 黒い画像を作る
image = np.zeros((H, W, 3), np.uint8)

# 線を引く
cv.line(image, (50, 50), (W-50, H-50), color=(0, 0, 255), thickness=20)

# 長方形を描く
cv.rectangle(image, (150, 50), (350, 200), color=(255, 127, 255), thickness=5)

# 塗りつぶされた長方形を描く
cv.rectangle(image, (400, 50), (600, 200), color=(80, 30, 180), thickness=cv.FILLED)

# 円を描く 
cv.circle(image, center=(150, 400), radius=100, color=(255, 100, 0), thickness=40)

# 塗りつぶした円を描く 
cv.circle(image, center=(250, 400), radius=100, color=(255, 220, 30), thickness=cv.FILLED)

# 楕円を描く 
cv.ellipse(image, center=(450, 400), axes=(100, 60), angle=90, startAngle=0, endAngle=360, color=(50, 255, 255), thickness=5)

# 塗りつぶした楕円を描く 
cv.ellipse(image, center=(600, 400), axes=(70, 200), angle=-30, startAngle=0, endAngle=270, color=(30, 100, 240), thickness=cv.FILLED)

# 保存する
cv.imwrite("drawing.png", image)

"""
Note:
    線種（破線や鎖線など）を指定する lineType オプションもある。
    
    このほかに、折れ線・（閉じた）多角形・矢印・文字を描く関数も用意されている。
    cv.FILLED の代わりに適当な負の整数を使ってもよい。
"""

