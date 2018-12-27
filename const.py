import cv2
global wide 
global high 
global imgpath1
global imgpath2
wide = 900
high = 600
imgpath1 = "photos/Image_00039.jpg"
imgpath2 = "photos/Image_00040.jpg"


def imgread(path):
    rimg = cv2.imread(path)
    # 读取图片
    img = cv2.resize(rimg, (wide, high), interpolation=cv2.INTER_CUBIC)
    # 图片重构大小
    return img