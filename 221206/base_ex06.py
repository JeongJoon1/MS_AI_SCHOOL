# instagram 같은 필터 만들기_ 세피아 필터
# 세피아필터 : 노을이미지같은 오렌지빛 이미지 만들때 많이 사용됨
''' 과정
채널분할 -> 빨,녹,파 채널에는 특정계수가 곱해지고, 빨,녹,파 에 대한 새로운값이 만들어짐
-> 빨,녹,파 에 대한 새 채널을 얻는다 
-> 채널을 새로운 빨, 새로운 녹, 새로운 파란색으로 다시 병합하여 최종출력이미지 만든다
-> 이미지 플룻하면 세피아효과 볼수있음
'''
import cv2
import numpy as np
from utils import image_show

img_path = "./car.jpg"
img = cv2.imread(img_path)

# 세피아 효과 필터
filter = np.array([[0.272, 0.534, 0.131],
                   [0.349, 0.686, 0.168],
                   [0.393, 0.769, 0.189]])

sepia_img = cv2.transform(img, filter)
image_show(sepia_img)