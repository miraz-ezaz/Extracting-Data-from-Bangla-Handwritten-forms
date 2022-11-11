import cv2
import numpy as np

import utils
from detection import detect
import ocr
import form
import file

def getData(imgform):
    template = cv2.imread('template/template.jpg', 0)
    imgform = cv2.cvtColor(imgform, cv2.COLOR_BGR2GRAY)
    imgScan = detect(template, imgform)
    # utils.show(imgScan,4)
    imgShow = imgScan.copy()
    imgShow = cv2.cvtColor(imgShow, cv2.COLOR_GRAY2BGR)
    imgMask = np.zeros_like(imgShow)
    roi = form.getROI()
    dict = []
    for x in roi:
        dic = {}
        field = roi[x]
        type = field['type']
        name = field['name']

        imgCrop, imgMask = form.getFields(imgScan, field, imgMask)
        if type == 'sbox':
            dic['type'] = type
            segments = field['segments']
            dic['segments']=segments
            dic['name']=name
            characters = form.box_segmentation(imgCrop, segments)
            character = ''
            for c in characters:
                if (np.count_nonzero(c)) > 200:
                    character += str(ocr.pred(c)).strip()
            dic['value'] = character
            dict.append(dic)
        if type == 'cbox':
            dic['type'] = type
            dic['name'] = name
            dic['value'] = form.checkBox(imgCrop)
            dict.append(dic)

    imgShow = cv2.addWeighted(imgShow, 0.6, imgMask, 0.4, 0)
    # utils.show(imgShow, 3)
    # print(dic)
    # file.insertIntoCSV(dic)
    return imgShow,dict