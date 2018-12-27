import cv2
import numpy as np
import const


def calculate(xx, x, redx, redy):
    up = 10   # 上下的offset
    down = 15
    sum = 0
    offset = 30   # 左右的offset
    grade = 20
    for i in range(len(redx)):
        if(redx[i] > x[0]-offset and redx[i] < x[1] + offset and 
        redy[i] > xx[1]-up and redy[i] < xx[2] + down):
            grade = grade - 5
        elif(redx[i] > x[0]-offset and redx[i] < x[1] + offset and 
        redy[i] > xx[3]-up and redy[i] < xx[3] + offset):
            score = int(21*(x[1]-redx[i]+offset)/(x[1]-x[0]+2*offset))
            print("第一大题分数为")
            print(score)
            sum=sum+score
        elif(redx[i] > x[2]-offset and redx[i] < x[3] + offset and 
        redy[i] > xx[0]-up and redy[i] < xx[0] + offset):
            score = int(21*(x[3]-redx[i]+offset)/(x[3]-x[2]+2*offset))
            print("第二大题分数为")
            print(score)
            sum=sum+score
        elif(redx[i] > x[2]-offset and redx[i] < x[3] + offset and 
        redy[i] > xx[4]-up and redy[i] < xx[4] + offset):
            score = int(21*(x[3]-redx[i]+offset)/(x[3]-x[2]+2*offset))
            print("第三大题分数为")
            print(score)
            sum=sum+score
    print("填空题分数为")
    print(grade)
    return sum + grade


def calculate2(xx, x, redx, redy):
    up = 10   # 上下的offset
    down = 15
    sum = 0
    offset = 30   # 左右的offset
    for i in range(len(redx)):
        if(redx[i] > x[0]-offset and redx[i] < x[1] + offset and 
        redy[i] > xx[1]-up and redy[i] < xx[1] + offset):
            score = int(21*(x[1]-redx[i]+offset)/(x[1]-x[0]+2*offset))
            print("第一大题分数为")
            print(score)
            sum=sum+score
        elif(redx[i] > x[0]-offset and redx[i] < x[1] + offset and 
        redy[i] > xx[2]-up and redy[i] < xx[2] + offset):
            score = int(21*(x[1]-redx[i]+offset)/(x[1]-x[0]+2*offset))
            print("第二大题分数为")
            print(score)
            sum=sum+score
        elif(redx[i] > x[2]-offset and redx[i] < x[3] + offset and 
        redy[i] > xx[0]-up and redy[i] < xx[0] + offset):
            score = int(21*(x[3]-redx[i]+offset)/(x[3]-x[2]+2*offset))
            print("第三大题分数为")
            print(score)
            sum=sum+score
    return sum 
