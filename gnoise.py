import cv2
import sys
import numpy

def add_gaussian_noise(src,mean,sigma):
    in_arr=src
    h,w,channels =in_arr.shape
    noise_image=numpy.array((w,h,3))
    noise_arr=numpy.random.normal(mean,sigma,in_arr.shape)
    noisey_image=noise_arr+in_arr
    return noisey_image
src = cv2.imread('Lenna.png',1)
cv2.namedWindow('Original image', cv2.WINDOW_NORMAL)
cv2.imshow('Original image',src)
#Add Gaussian Noise
mean=20
sigma=50
g_noise1=add_gaussian_noise(src,mean,sigma)
g_noise2=g_noise1
g_noise3=g_noise1
cv2.imshow('Gaussian Noise',g_noise1)
noise_dst1=cv2.blur(g_noise1,(5,5))
noise_dst2=cv2.GaussianBlur(g_noise2,(5,5),0)
g_noise3=g_noise3.astype(numpy.uint8)
noise_dst3=cv2.medianBlur(g_noise3,5)
cv2.imshow('Blur for Gaussian',noise_dst1)
cv2.imshow('Gaussian Blur for Gaussian',noise_dst2)
cv2.imshow('Median Blur for Gaussian',noise_dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
