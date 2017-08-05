import cv2
import numpy as np
 
# read sample images
img1 = cv2.imread("ESTEIRA0.jpg")
img2 = cv2.imread("ESTEIRA1.jpg")
img3 = cv2.imread("mask.jpg")
 
# convert the images for gray scale
imgray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
imgray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
imgray3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)
 
#find the diference betwen img1 and img2
diference = cv2.subtract(imgray1, imgray2)
 
#show imagem in a window
cv2.imshow('DETECCAO', diference)
 
#wait any key to close the window
cv2.waitKey(0)
