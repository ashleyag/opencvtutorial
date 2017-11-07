import cv2
import sys
import numpy

src = cv2.imread('Lenna.png',1)
cv2.namedWindow('Original image', cv2.WINDOW_NORMAL)
cv2.imshow('Original image',src)
gray =cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
cv2.namedWindow('Gray image', cv2.WINDOW_NORMAL)
cv2.imshow('Grayimage',gray)
threshold_value = 128
ret,dst = cv2.threshold(gray,threshold_value, 255, cv2.THRESH_BINARY )
cv2.imshow('Thresholded Image', dst )
#Binary Threshold
current_threshold = 128
max_threshold = 255
ret,thresholded=cv2.threshold(gray,current_threshold, max_threshold, cv2.THRESH_BINARY)
cv2.imshow('Binary threshold',thresholded)
#Band Threshold
threshold1 = 27
threshold2 = 125
ret,binary1=cv2.threshold(gray,threshold1, max_threshold, cv2.THRESH_BINARY)
ret,binary2=cv2.threshold(gray,threshold2, max_threshold, cv2.THRESH_BINARY_INV)
band_thresh=numpy.bitwise_and( binary1, binary2)
cv2.imshow('Band Thresholding', band_thresh)
#Semi Thresholding
ret,semi_thresh=cv2.threshold(gray,current_threshold, max_threshold, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU);
semi_thresh=numpy.bitwise_and( gray, semi_thresh)
cv2.imshow('Semi Thresholding', semi_thresh)
#Adaptive Threshold
adaptive_thresh=cv2.adaptiveThreshold(gray,255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 101, 10 );
cv2.imshow('Adaptive Thresholding', adaptive_thresh);
cv2.waitKey(0)
cv2.destroyAllWindows()
