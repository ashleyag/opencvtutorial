import cv2
import sys
import numpy

def add_salt_pepper_noise(src,salt):
      row,col,ch = src.shape
      amount = 0.004
      out = numpy.copy(src)
      # Salt mode
      num_salt = numpy.ceil(amount * src.size * salt)
      coords = [numpy.random.randint(0, i - 1, int(num_salt))
              for i in src.shape]
      out[coords] = 255

      # Pepper mode
      num_pepper = numpy.ceil(amount* src.size * (1.-salt))
      coords = [numpy.random.randint(0, i - 1, int(num_pepper))
              for i in src.shape]
      out[coords] = 0
      return out
    
src = cv2.imread('Lenna.png',1)
cv2.namedWindow('Original image', cv2.WINDOW_NORMAL)
cv2.imshow('Original image',src)
#Add salt and pepper noise			
salt=0.4;			
sp_noise1=add_salt_pepper_noise(src,salt); 
cv2.imshow('Salt and pepper noise',sp_noise1)
sp_noise2=sp_noise1
sp_noise3=sp_noise2
noise_dst4=cv2.blur(sp_noise1,(7,7))
noise_dst5=cv2.GaussianBlur(sp_noise2,(7,7),0)
sp_noise3=sp_noise3.astype(numpy.uint8)
noise_dst6=cv2.medianBlur(sp_noise3,7)
cv2.imshow('Blur for salt and pepper',noise_dst4)
cv2.imshow('Gaussian Blur for salt and pepper',noise_dst5)
cv2.imshow('Median Blur for salt and pepper',noise_dst6)
cv2.waitKey(0)
cv2.destroyAllWindows()
