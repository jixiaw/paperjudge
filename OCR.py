from aip import AipOcr
import cv2
import os
import const

APP_ID = '14951518'
API_KEY = 'ztZOQ5YWtdQco5v7KSmGVbqv'
SECRET_KEY = 'ycipX3vvtpjIMc9wRI4M8QP1Rc3g0n2e'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
fname = 'photos/label.jpg'

def get_file_content(filePath): 
    with open(filePath, 'rb') as fp:       
        return fp.read()

def GetNo(imgpath1):
    # 读取图片
    image = cv2.imread(imgpath1)
    # 裁剪图片
    label = image[250:450, 0:250]
    # cv2.imshow('processed photo', label)
    # 旋转图片
    (h, w) = label.shape[:2] 
    center = (w // 2, h // 2) 
    M = cv2.getRotationMatrix2D(center, 270, 1.0) 
    label = cv2.warpAffine(label, M, (w, h))  
    # cv2.imshow("Rotated by 90 Degrees", label)
    # 保存图片
    cv2.imwrite('photos/label.jpg', label)
    # ocr
    img = get_file_content(fname)  
    # 结果分析
    res = client.general(img)['words_result']
    print(res)
    ss = ''
    for i in range(len(res)):
        ss = ss + res[i]['words']
    sss = ''
    for i in range(len(ss)):
        if('0'<=ss[i] and ss[i]<='9'):
             sss = sss+ss[i]
    m=sss.find('130')
    if(m < 0):
        print("orc error")
        return "999999"
    else:
        sss = sss[m:m+6]
    # 删除图片
    os.remove(fname)
    # print(sss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows() 
    return sss