import numpy as np 

import cv2 

  

  

def cambio_color(imagen): 

    gris=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) 

    cv2.imshow('ImgGray', gris) 

  

    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) 

    cv2.imshow('ImgHSV', hsv) 

  

    yuv = cv2.cvtColor(imagen, cv2.COLOR_BGR2YUV) 

    cv2.imshow('ImgYUV', yuv) 

  

    Ycrcb = cv2.cvtColor(imagen, cv2.COLOR_BGR2YCrCb) 

    cv2.imshow('ImgYctcb', Ycrcb) 

  

src = cv2.imread('afgana.jpg',1) 

cv2.namedWindow('input image', cv2.WINDOW_AUTOSIZE) 

cv2.imshow('input image', src) 

  

cambio_color(src) 

  

b, g, r = cv2.split(src) 

cv2.imshow('blue', b) 

cv2.imshow('green', g) 

cv2.imshow('red', r) 

  

src = cv2.merge([r,g,b]) 

#src[:,:,0] = 0 #Asignar un solo canal 

cv2.imshow('change image', src) 

  

cv2.waitKey(0) 

cv2.destroyAllWindows() 