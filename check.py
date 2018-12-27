import cv2
import const


def check(xx, x, img):
    high = const.high
    wide = const.wide
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

    # 根据裁剪的带获得判断的条状带。
    up = 6   # 上下的offset
    down = 10
    offest = 10   # 左右的offset
    for i in range(high):
        for j in range(wide):
            if(not((i > xx[0]-up and i < xx[0]+down and j > x[2]-offest and j < x[3]+offest)  
            or(i > xx[1]-up and i < xx[1]+down and j > x[0]-offest and j < x[1] + offest) 
            or(i > xx[2]-up and i < xx[2]+down and j > x[0]-offest and j < x[1] + offest)
            or(i > xx[3]-up and i < xx[3]+down and j > x[0]-offest and j < x[1] + offest)
            or(i > xx[4]-up and i < xx[4] + down and j > x[2]-offest and j < x[3] + offest))):
                img[i][j] = 0
    cv2.imshow('processed photo', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  

    
def check2(xx, x, img):
    high = const.high
    wide = const.wide
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

    # 根据裁剪的带获得判断的条状带。
    up = 6   # 上下的offset
    down = 10
    offest = 10   # 左右的offset
    for i in range(high):
        for j in range(wide):
            if(not((i > xx[0]-up and i < xx[0]+down and j > x[2]-offest and j < x[3]+offest)  
            or(i > xx[1]-up and i < xx[1]+down and j > x[0]-offest and j < x[1] + offest) 
            or(i > xx[2]-up and i < xx[2]+down and j > x[0]-offest and j < x[1] + offest))):
                img[i][j] = 0
    cv2.imshow('processed photo', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
