# 기본적인 이미지처리기술을 이용한 이미지 선명하게 해보기
# 일반적으로 이미지의 가장자리를 향상시키는데 사용
# cv2.filter2D() 임의의필터로 이미지를 처리하는 기능을 사용

import cv2
import numpy as np 
from utils import image_show

image = cv2.imread('./car.jpg')

# creating out sharpening filter 
'''
-1 -1 -1
-1 9 -1
-1 -1 -1
만들기
'''
filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

sharpen_img = cv2.filter2D(image, -1, filter)  # -1은 기본값
cv2.imshow('org image', image)
cv2.waitKey(0)

image_show(sharpen_img)