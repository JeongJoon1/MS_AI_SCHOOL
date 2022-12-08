# 기본적인 이미지 처리기술 이용한 이미지 선명하게 해보기_필터값 설정해 다양한종류 필터링할수있다
# custom 필터 만들기

import cv2
import numpy as np
from utils import image_show

image = cv2.imread('./car.jpg')

filter = np.array([[3, -2, -3], [-4, 8, -6], [5, -1, -0]])
custom_image_filter = cv2.filter2D(image, -1, filter)

image_show(custom_image_filter)
