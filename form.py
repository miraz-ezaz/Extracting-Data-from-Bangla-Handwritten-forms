import random

from detection import detect
import cv2
import numpy as np
import utils
import json

def getFields(imgScan,field,imgMask):
    x1y1 = field['points'][0]
    x2y2 = field['points'][1]
    cv2.rectangle(imgMask, x1y1, x2y2, (0, 0, 255), cv2.FILLED)
    field = imgScan[x1y1[1]:x2y2[1], x1y1[0]:x2y2[0]]
    return field,imgMask

def box_segmentation(box,segment):
    thresh = utils.thresholding(box, 0, 255)
    thresh = utils.dilation(thresh, 2, 2)
    row = np.array_split(thresh, segment, 1)
    segments = []
    for r in row:
        hor = utils.horizontal_lines(r)
        ver = utils.vertical_lines(r)
        r = r - ver - hor
        r = r[5:r.shape[0] - 5, 5:r.shape[1] - 5]
        r = utils.erode(r, 3, 3)
        r = utils.dilation(r, 2, 2)
        #utils.show(r,1)
        segments.append(r)
    return segments
def checkBox(img):
    thresh = utils.thresholding(img, 0, 255)
    thresh = utils.dilation(thresh, 2, 2)

    hor = utils.horizontal_lines(thresh)
    ver = utils.vertical_lines(thresh)

    show = thresh - ver - hor
    show = show[5:show.shape[0] - 5, 5:show.shape[1] - 5]
    show = utils.erode(show, 4, 4)
    show = utils.dilation(show, 4, 4)
    #cv2.imwrite(f'test/{random.randint(1,100)}.jpg',show)
    nonZero = np.count_nonzero(show)
    print(nonZero)
    if nonZero<100:
        return 0
    else:
        return 1



def getROI():
    file_hadle = open('roi2.json', 'r')
    dic = json.load(file_hadle)
    file_hadle.close()
    return dic
