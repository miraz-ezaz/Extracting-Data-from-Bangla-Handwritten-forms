import cv2
import numpy as np
def show(img,x):
    h,w= img.shape[:2]
    img = cv2.resize(img,(int(w/x),int(h/x)))
    cv2.imshow("Sample", img)
    cv2.waitKey(0)
def thresholding(img,x,y):
    ret,thresh = cv2.threshold(img, x, y,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return thresh
def dilation(thresh_img,x,y,iterations=1):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (x, y))
    dilated = cv2.dilate(thresh_img,kernel,iterations=iterations)
    return dilated
def erode(thresh_img,x,y,iterations=1):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (x, y))
    erode = cv2.erode(thresh_img,kernel,iterations=iterations)
    return erode
def horizontal_lines(img):
    # length = np.array(img).shape[1] // 100
    # horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (length, 1))
    # horizontal_detect = cv2.erode(img, horizontal_kernel, iterations=5)
    # hor_line = cv2.dilate(horizontal_detect, horizontal_kernel, iterations=5)
    # return hor_line
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
    detected_lines = cv2.morphologyEx(img, cv2.MORPH_OPEN,
                                      horizontal_kernel, iterations=5)
    return detected_lines
def vertical_lines(img):
    # length = np.array(img).shape[1] // 100
    # horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (length, 1))
    # horizontal_detect = cv2.erode(img, horizontal_kernel, iterations=5)
    # hor_line = cv2.dilate(horizontal_detect, horizontal_kernel, iterations=5)
    # return hor_line
    # h,w=img.shape[:2]
    # img = dilation(img,1,2)
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 25))
    detected_lines = cv2.morphologyEx(img, cv2.MORPH_OPEN,
                                      horizontal_kernel, iterations=5)
    return detected_lines
def resize(img,x):
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / x), int(h / x)),interpolation=cv2.INTER_CUBIC)
    return img
