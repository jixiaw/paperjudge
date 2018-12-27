import cv2
import numpy as np


def getred(img):
    redx = []
    redy = []
    # 红色蒙版过滤
    lower_red = np.array([65, 65, 120])
    upper_red = np.array([100, 120, 255])
    mask = cv2.inRange(img, lower_red, upper_red)
    img = cv2.bitwise_and(img, img, mask=mask)
    # 二值化处理
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
    # 腐蚀
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)
    # 膨胀操作
    kernel = np.ones((7, 7), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
#     cv2.imshow('processed photo', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    # 连通域分析
    _, labels, stats, centroids = cv2.connectedComponentsWithStats(img)
    # print(centroids)
    # print(stats)
    # print(img)
    for i in range(len(stats)):
        if(stats[i][4] > 20):
            redx.append(centroids[i][0])
            redy.append(centroids[i][1])
    # print(redx)
    # print(redy)
    # cv2.imshow('processed photo', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return redx, redy
