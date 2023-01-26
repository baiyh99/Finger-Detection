import copy

import cv2
import numpy as np
#Use CV2 Functionality to create a Video stream and add some values
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    size = (35,35)



    smooth_img = cv2.GaussianBlur(gray, size ,0)
    thresh = gray
    #_, thresh = cv2.threshold(smooth_img, 240, 255, cv2.THRESH_BINARY_INV)

    thresh1 = thresh.copy()
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key=lambda x: cv2.contourArea(x))
    #_, thresh = cv2.threshold(thresh, 100, 255, cv2.THRESH_BINARY_INV)

    drawings = np.zeros(img.shape, np.uint8)
    cv2.drawContours(drawings, [cnt], 0, (0,255,255), 10)

    cv2.imshow("Image", img);
    cv2.imshow("Frame", thresh);
    cv2.imshow("Drawings", drawings);
    key = cv2.waitKey(10)
    if key == ord("q"):
        break