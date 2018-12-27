# 自动批卷系统，lhw 2018-11-25
# latest revise 2018-12-1
# 得到四个列定位点的横坐标
import cv2
import const
import math


def rotate(img, x, y):
    # 计算tan的值
    tan = (y[1] - y[0])/(x[1] - x[0])
    degree = math.atan(tan)
    degree = degree/math.pi*160
    (h, w) = img.shape[:2] 
    center = (w // 2, h // 2) 
    M = cv2.getRotationMatrix2D(center, degree, 1.0) 
    img = cv2.warpAffine(img, M, (w, h)) 
    # cv2.imshow('after rotate', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows() 
    return img
