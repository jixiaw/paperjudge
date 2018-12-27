# 自动批卷系统，lhw 2018-11-25
# latest revise 2018-12-1
# 得到四个列定位点的横坐标
import cv2
import numpy as np
import const
import copy


def getloc_co(img):
    wide = const.wide
    high = const.high
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('column.py', img)
    # 图像二值化
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    # cv2.imshow('column.py', img)
    # 黑白反向
    # print(img)
    for i in range(high):
        for j in range(wide):
            img[i][j] = 255-img[i][j]
    # cv2.imshow('column.py', img)
    # 试卷处理，把框外的图去除,区域剖分
    for i in range(high):
        for j in range(int(wide/12)):
            img[i][j] = 0

    for i in range(high):
        for j in range(int(wide/12)):
            img[i][wide-1-j] = 0
    
    for i in range(0, int(high/25)):
        for j in range(wide):
            img[i][j] = 0 

    for i in range(int(high/10), high):
        for j in range(wide):
            img[i][j] = 0 
    # cv2.imshow('column.py', img)
    # 腐蚀
    kernel = np.ones((3, 3), np.uint8)  
    img = cv2.erode(img, kernel, iterations=1)
    # cv2.imshow('column.py', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows() 
    # 连通域分析
    _, labels, stats, centroids = cv2.connectedComponentsWithStats(img)
    # print(labels)
    # print(stats)
    # print(centroids)
    x = [0, 0, 0, 0]
    y = [0, 0, 0, 0]
    s = [0, 0, 0, 0]
    for i in range(1, 5):
        for j in range(i+1, len(stats)):
            if(stats[j][4] > stats[i][4]):
                temp = copy.deepcopy(stats[j])
                stats[j] = copy.deepcopy(stats[i]) 
                stats[i] = copy.deepcopy(temp)
                
    # print(stats)
    for i in range(0, 4):
        x[i] = stats[i+1][0]
        y[i] = stats[i+1][1]
        s[i] = stats[i+1][4]

    for i in range(0, 3):
        for j in range(i+1, 4):
            if(x[j] < x[i]):
                temp = copy.deepcopy(x[j])
                x[j] = copy.deepcopy(x[i]) 
                x[i] = copy.deepcopy(temp) 
                temp = copy.deepcopy(y[j])
                y[j] = copy.deepcopy(y[i]) 
                y[i] = copy.deepcopy(temp)  
                temp = copy.deepcopy(s[j])
                s[j] = copy.deepcopy(s[i]) 
                s[i] = copy.deepcopy(temp)        
    # print("四个垂直的定位横坐标为：")
    # print(x)
    # print("四个垂直的定位纵坐标为：")
    # print(y)
    # print("四个垂直的定位面积为：")
    # print(s)
    # cv2.imshow('origin photo', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()   
    return x, y


def getloc_column(img):
    wide = const.wide
    high = const.high
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 图像二值化
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    # cv2.imshow('column.py', img)
    # 黑白反向
    # print(img)
    for i in range(high):
        for j in range(wide):
            img[i][j] = 255-img[i][j]
    # 试卷处理，把框外的图去除,区域剖分
    for i in range(high):
        for j in range(int(wide/12)):
            img[i][j] = 0

    for i in range(high):
        for j in range(int(wide/12)):
            img[i][wide-1-j] = 0
    
    for i in range(0, int(high/25)):
        for j in range(wide):
            img[i][j] = 0 

    for i in range(int(high/10), high):
        for j in range(wide):
            img[i][j] = 0 

    # 腐蚀
    kernel = np.ones((2, 3), np.uint8)  
    img = cv2.erode(img, kernel, iterations=1)
    # cv2.imshow('column.py', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows() 
    # 连通域分析
    _, labels, stats, centroids = cv2.connectedComponentsWithStats(img)
    # print(labels)
    # print(stats)
    # print(centroids)
    x = [0, 0, 0, 0]
    y = [0, 0, 0, 0]
    s = [0, 0, 0, 0]
    for i in range(1, 5):
        for j in range(i+1, len(stats)):
            if(stats[j][4] > stats[i][4]):
                temp = copy.deepcopy(stats[j])
                stats[j] = copy.deepcopy(stats[i]) 
                stats[i] = copy.deepcopy(temp)
                
    # print(stats)
    for i in range(0, 4):
        x[i] = stats[i+1][0]
        y[i] = stats[i+1][1]
        s[i] = stats[i+1][4]

    for i in range(0, 3):
        for j in range(i+1, 4):
            if(x[j] < x[i]):
                temp = copy.deepcopy(x[j])
                x[j] = copy.deepcopy(x[i]) 
                x[i] = copy.deepcopy(temp) 
                temp = copy.deepcopy(y[j])
                y[j] = copy.deepcopy(y[i]) 
                y[i] = copy.deepcopy(temp)  
                temp = copy.deepcopy(s[j])
                s[j] = copy.deepcopy(s[i]) 
                s[i] = copy.deepcopy(temp)        
    # print("四个垂直的定位横坐标为：")
    # print(x)
    # print("四个垂直的定位纵坐标为：")
    # print(y)
    # print("四个垂直的定位面积为：")
    # print(s)
    # cv2.imshow('origin photo', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()   
    return x, y


