import cv2
import numpy as np
from skimage.util import random_noise
from random import seed
from random import random

seed(1)

#image will be displayed for 1 second 

img = cv2.imread('lena.jpg')
cv2.imshow('Lena_image',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

img_gray = cv2.imread('lena.jpg',0)
cv2.imshow('Lena_Gray',img_gray)
cv2.waitKey(1000)
cv2.destroyAllWindows()

for x in range(6):
    temp = 0
    for y in range(5 * (x + 1)):
        noise_img = random_noise(img_gray,mode='gaussian',mean=random(),var= random())
        temp += noise_img
    cv2.imshow('Lena_Gray Gaussian' + str(x),temp/(5*(x + 1)))
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

for x in range(6):
    temp = 0
    for y in range(5 * (x + 1)):
        noise_img = random_noise(img_gray,mode='s&p',amount = random())
        temp += noise_img
    cv2.imshow('Lena_Gray Salt and Pepper' + str(x),temp/(5*(x + 1)))
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

for x in range(6):
    temp = 0
    for y in range(5 * (x + 1)):
        noise_img = random_noise(img_gray,mode='speckle',mean=0,var=random())
        temp += noise_img 
    cv2.imshow('Lena_Gray Speckle ' + str(x),temp/(5*(x + 1)))
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
