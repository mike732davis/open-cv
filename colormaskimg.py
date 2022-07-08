import cv2
import numpy as np
img=cv2.imread('1primary.jpg')
imgrs=cv2.resize(img, (720,720),interpolation=cv2.INTER_NEAREST)
hsv = cv2.cvtColor(imgrs, cv2.COLOR_BGR2HSV)

lower_red = np.array([161,155,84])
upper_red = np.array([179,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(imgrs,imgrs, mask= mask)

cv2.imshow('image original',imgrs)
cv2.imshow('masked Output',mask)
cv2.imshow('Final Output',res)
cv2.waitKey(0)