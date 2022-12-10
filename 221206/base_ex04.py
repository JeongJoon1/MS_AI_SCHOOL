# 기본적인 이미지 처리기술 이용한 이미지 선명하게 해보기_샤프인 필터
# 샤프닝필터(멕시칸 햇 or 라폴라시안 필터)
# 출력이미지 : 이미지의 가장자리를 보존했음을 알수있다
import cv2
import numpy as np
from utils import image_show

image = cv2.imread('./car.jpg')

# creating maxican hat filter for
# 5x5
# filter = np.array([[0, 0, -1, 0, 0], [0, -1, -2, -1, 0],
#                   [-1, -2, 16, -2, -1], [0, -1, -2, -1, 0],
#                   [0, 0, -1, 0, 0]])

# 3x3
filter = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
mexican_hat_image = cv2.filter2D(image, -1, filter)
image_show(mexican_hat_image)
cv2.imwrite('./mexican_hat_5x5.png', mexican_hat_image)
