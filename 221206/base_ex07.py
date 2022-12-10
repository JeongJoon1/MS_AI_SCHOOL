# 필터의 방향에 따라 사용할 수 있는 여러 필터가 있습니다.
# 이 필터의 수직, 수평 또는 대각선 버전을 가질 수 있다.
# 예제의 경우 수직 이미지를 사용하고 일단 이미지를 필터링하면 매우 낮은 차이를 얻게 된다. 
# -> 즉, 출력 이미지가 다소 검은색이 된다 -> 각 픽셀에 상수 128을 추가 -> 결과이미지 : 회색

import cv2
import numpy as np

from utils import image_show

image_path = './car.jpg'
img = cv2.imread(image_path)

#엠보싱 효과
filter1 = np.array([[0, 1, 0], [0, 0, 0], [0, -1, 0]])
filter2 = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])
emboss_img = cv2.filter2D(img, -1, filter2)
emboss_img = emboss_img + 128
image_show(emboss_img)
