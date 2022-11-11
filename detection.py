import cv2
import numpy as np

#orb = cv2.ORB_create(5000)
def detect(imgMain,imgTest):
    orb = cv2.ORB_create(5000)
    h, w = imgMain.shape[:2]
    kp1, des1 = orb.detectAndCompute(imgMain, None)
    kp2, des2 = orb.detectAndCompute(imgTest, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.match(des2, des1)
    matches = sorted(matches,key=lambda x: x.distance)
    good = matches[:int(len(matches) * (25 / 100))]
    srcPoints = np.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dstPoints = np.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    M, _ = cv2.findHomography(srcPoints, dstPoints, cv2.RANSAC, 5.0)
    imgScan = cv2.warpPerspective(imgTest, M, (w, h))
    return imgScan