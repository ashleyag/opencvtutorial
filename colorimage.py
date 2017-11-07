import cv2
import sys
import matplotlib.pyplot as pl
import numpy
src = cv2.imread('baboon.jpg',1)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',src)
h,w,channels =src.shape
#input_planes=numpy.array(3)
b,g,r = cv2.split (src)
cv2.imshow('Blue Channel',b)
cv2.imshow('Green Channel',g)
cv2.imshow('Red Channel',r)
ycrcb_image=numpy.array((w,h,3))
ycrcb_image=cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)
y,cb,cr = cv2.split (ycrcb_image)
cv2.imshow('Y Channel',y)
cv2.imshow('Cb Channel',cb)
cv2.imshow('Cr Channel',cr)
hsv_image=numpy.array((w,h,3))
hsv_image=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
hue,sat,val = cv2.split (hsv_image)
cv2.imshow('Hue',hue)
cv2.imshow('Saturation',sat)
cv2.imshow('Value',val)
pixel=src[20,25]
print(pixel)
pixel_ycrcb=ycrcb_image[20,25]
print(pixel_ycrcb)
pixel_hsv=hsv_image[20,25]
print(pixel_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

