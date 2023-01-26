import copy
import matplotlib.pyplot as plt
import cv2
import numpy as np
#Use CV2 Functionality to create a Video stream and add some values

with_fingers = cv2.imread('with_fingers.jpg', cv2.IMREAD_COLOR)
without_fingers = cv2.imread('without_fingers.jpg', cv2.IMREAD_COLOR)

hsv = cv2.cvtColor(with_fingers, cv2.COLOR_BGR2HSV)
hsv_bg = cv2.cvtColor(without_fingers, cv2.COLOR_BGR2HSV)


h, s, v = cv2.split(hsv)
h1, s1, v1 = cv2.split(hsv_bg)
#
# threshold = 180
# s[s >= 0] = 0
# v[v <= threshold] = 0
#
# s1[s1 >= 0] = 0
# v1[v1 <= threshold] = 0
#
# final_hsv = cv2.merge((h,s,v))
#
#
hr = h - h1
sr = s - s1
vr = v - v1

print(type(vr))
print(type(vr[vr > 80]))

factor = 2.5
v_thresh = 150


vr_copy_high = vr[vr > v_thresh]
vr_copy_low = vr[vr <= 80]

vr[vr > v_thresh] = vr_copy_high * np.uint8(factor)

vr = vr.astype(np.uint8)

diff = cv2.merge((hr, sr, vr))
rgb = cv2.cvtColor(diff, cv2.COLOR_HSV2RGB)


drawings = np.zeros(diff.shape, np.uint8)

rgb_gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)


size = (35,35)
smooth_img = cv2.GaussianBlur(rgb_gray, size, 1)
_, thresh = cv2.threshold(smooth_img, 160, 255, cv2.THRESH_TOZERO)

cv2.imshow("Diff in HSV", rgb_gray)
cv2.imshow("Threshold", thresh)

cv2.waitKey(0)
# Destroys all the windows created
cv2.destroyAllwindows()

