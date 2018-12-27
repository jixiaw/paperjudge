# 自动批卷系统，lhw 2018-11-25
# 得到四个列定位点的横坐标
import cv2
import numpy as np
import const
import copy


def getloc_row(img, x, y):
    wide = const.wide
    high = const.high
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 图像二值化
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    # cv2.imshow('origin photo', img)
    # 黑白反向
    # print(img)
    for i in range(high):
        for j in range(wide):
            img[i][j] = 255-img[i][j]
    # 试卷处理，把框外的图去除
    for i in range(high):
        for j in range(int(wide/12)):
            img[i][j] = 0

    for i in range(high):
        for j in range(int(wide/12)):
            img[i][wide-1-j] = 0

    for i in range(0, int(high/10)):
        for j in range(wide):
            img[i][j] = 0 
    
    for i in range(int(high*4/5), high):
        for j in range(wide):
            img[i][j] = 0 

    
    # 试卷处理，把竖直定位内的像素点去掉

    offset = 7
    for i in range(high):
        for j in range(x[0]-offset, x[1]+offset):
            img[i][j] = 0
    for i in range(high):
        for j in range(x[2]-offset, x[3]+offset*2):
            img[i][j] = 0
    for i in range(0, y[0]+5):
        for j in range(x[2], x[3]):
            img[i][j] = 0

    # cv2.imshow('origin photo', img)
    # 直方图均衡化
    img = cv2.equalizeHist(img)
    # 腐蚀
    kernel = np.ones((3, 3), np.uint8)  
    img = cv2.erode(img, kernel, iterations=1)
    # cv2.imshow('11', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # 连通域分析
    _, labels, stats, centroids = cv2.connectedComponentsWithStats(img)
    

    x = [0] * 14
    y = [0] * 14
    s = [0] * 14
    for i in range(1, 15):
        for j in range(i+1, len(stats)):
            if(stats[j][4] > stats[i][4]):
                temp = copy.deepcopy(stats[j])
                stats[j] = copy.deepcopy(stats[i]) 
                stats[i] = copy.deepcopy(temp)
    # print(stats)

    for i in range(0, 14):
        x[i] = stats[i+1][0]
        y[i] = stats[i+1][1]
        s[i] = stats[i+1][4]
  
    for i in range(0, 13):
        for j in range(i+1, 14):
            if(y[j] < y[i]):
                temp = copy.deepcopy(x[j])
                x[j] = copy.deepcopy(x[i]) 
                x[i] = copy.deepcopy(temp) 
                temp = copy.deepcopy(y[j])
                y[j] = copy.deepcopy(y[i]) 
                y[i] = copy.deepcopy(temp)  
                temp = copy.deepcopy(s[j])
                s[j] = copy.deepcopy(s[i]) 
                s[i] = copy.deepcopy(temp) 
    # print(x)
    # print(y)
    # print(s) 

    # print("5个水平的定位横坐标为：")
    # print(xx)
    # xx = [0]*7
    # yy = [0]*7
    # for i in range(0, 14, 2):
    #     xx[i//2] = x[i]
    #     yy[i//2] = y[i]
    # print(xx)
    # print(yy)
    # cv2.imshow('origin photo', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()   
    xxx = [0]*7
    yyy = [0]*7
    for i in range(0, 14, 2):
        xxx[i//2] = copy.deepcopy(x[i])
        yyy[i//2] = copy.deepcopy(y[i])
    xxxx = [0]*5
    yyyy = [0]*5
    for i in range(3, 7):
        xxxx[i-2] = copy.deepcopy(xxx[i])
        yyyy[i-2] = copy.deepcopy(yyy[i])
    xxxx[0] = copy.deepcopy(xxx[0])
    yyyy[0] = copy.deepcopy(yyy[0])
    return xxxx, yyyy


def getloc_row2(img, x, y):
    wide = const.wide
    high = const.high
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 图像二值化
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    # cv2.imshow('origin photo', img)
    # 黑白反向
    # print(img)
    for i in range(high):
        for j in range(wide):
            img[i][j] = 255-img[i][j]
    # 试卷处理，把框外的图去除
    for i in range(high):
        for j in range(int(wide/20)):
            img[i][j] = 0

    for i in range(high):
        for j in range(int(wide/12)):
            img[i][wide-1-j] = 0

    for i in range(0, int(high/20)):
        for j in range(wide):
            img[i][j] = 0 
    
    for i in range(int(high*4/5), high):
        for j in range(wide):
            img[i][j] = 0 

    # cv2.imshow('origin photo', img)
    # 试卷处理，把竖直定位内的像素点去掉
    img = cv2.equalizeHist(img)
    # cv2.imshow('11', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    offset = 7
    for i in range(high):
        for j in range(x[0]-offset, x[1]+offset*3):
            img[i][j] = 0
    for i in range(high):
        for j in range(x[2]-offset, x[3]+offset*3):
            img[i][j] = 0
    for i in range(0, y[0]+5):
        for j in range(x[0], x[3]):
            img[i][j] = 0

    # 直方图均衡化
    img = cv2.equalizeHist(img)
    # cv2.imshow('11', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # 腐蚀
    kernel = np.ones((3, 3), np.uint8)  
    img = cv2.erode(img, kernel, iterations=1)
   
    # 连通域分析
    _, labels, stats, centroids = cv2.connectedComponentsWithStats(img)
    
    x = [0] * 6
    y = [0] * 6
    s = [0] * 6
    for i in range(1, 7):
        for j in range(i+1, len(stats)):
            if(stats[j][4] > stats[i][4]):
                temp = copy.deepcopy(stats[j])
                stats[j] = copy.deepcopy(stats[i]) 
                stats[i] = copy.deepcopy(temp)
    # print(stats)

    for i in range(0, 6):
        x[i] = stats[i+1][0]
        y[i] = stats[i+1][1]
        s[i] = stats[i+1][4]
  
    for i in range(0, 5):
        for j in range(i+1, 6):
            if(y[j] < y[i]):
                temp = copy.deepcopy(x[j])
                x[j] = copy.deepcopy(x[i]) 
                x[i] = copy.deepcopy(temp) 
                temp = copy.deepcopy(y[j])
                y[j] = copy.deepcopy(y[i]) 
                y[i] = copy.deepcopy(temp)  
                temp = copy.deepcopy(s[j])
                s[j] = copy.deepcopy(s[i]) 
                s[i] = copy.deepcopy(temp) 
    # print(x)
    # print(y)
    # print(s) 

    # print("5个水平的定位横坐标为：")
    # print(xx)
    # xx = [0]*7
    # yy = [0]*7
    # for i in range(0, 14, 2):
    #     xx[i//2] = x[i]
    #     yy[i//2] = y[i]
    # print(xx)
    # print(yy)
    # cv2.imshow('origin photo', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    xxx = [0]*3
    yyy = [0]*3
    for i in range(0, 6, 2):
        xxx[i//2] = copy.deepcopy(x[i])
        yyy[i//2] = copy.deepcopy(y[i])   
    return xxx, yyy