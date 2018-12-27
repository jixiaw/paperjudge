# 自动批卷系统，lhw 2018-11-25
from calculate import calculate
from calculate import calculate2
from locate_row import getloc_row
from locate_row import getloc_row2
from locate_column import getloc_co
from locate_column import getloc_column
from getred import getred
# from check import check
# from check import check2
from OCR import GetNo
from rotate import rotate
from const import imgread
from Datebase.datebase import DBHelper


def judge(imgpath1, imgpath2):
    # 假设填空满分
    sum = 60
    # 学号ocr   
    no = GetNo(imgpath1)
    print("学号为：")
    print(no)
    # 批改试卷正面
    # 图片旋转处理
    # 得到旋转后的图片img
    img = imgread(imgpath1)
    x, y = getloc_co(img)
    img = rotate(img, x, y)
    # 获取四个列坐标点
    x, y = getloc_column(img)
    print(x)
    print(y)
    # 获取14个横坐标点
    xx, yy = getloc_row(img, x, y)
    print(xx)
    print(yy)
    # 获得红笔标记的位置
    redx, redy = getred(img)
    print("红笔位置redx为：")
    print(redx)
    print("红笔位置redy为：")
    print(redy)
    # check(yy, x, img)
    front = calculate(yy, x, redx, redy)
    print('正面的分数为', front)
    sum = sum + front
    # 批改试卷背面
    # 图片旋转处理
    # 得到旋转后的图片img
    img = imgread(imgpath2)
    x, y = getloc_co(img)
    img = rotate(img, x, y)
    # 获取四个列坐标点
    x, y = getloc_column(img)
    print(x)
    print(y)
    # 获取6个横坐标点
    xx, yy = getloc_row2(img, x, y)
    print(xx)
    print(yy)
    # 获得红笔标记的位置
    redx, redy = getred(img)
    print("红笔位置redx为：")
    print(redx)
    print("红笔位置redy为：")
    print(redy)
    # check2(yy, x, img)
    back = calculate2(yy, x, redx, redy)
    print('背面的分数为', back)
    sum = sum + back
    print('试卷的总分为', sum)
    dbhelper = DBHelper()
    dbhelper.add_data(no, sum, imgpath1, imgpath2)
    return sum

