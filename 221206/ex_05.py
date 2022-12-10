# 이미지 이진화
# : 어떤 값보다 큰 값을 가진 픽셀을 흰색으로 만들고 작은값은 검은색으로 만드는과정
# gray scale에서 이진화 해야됨
# 외곽선 따기위해 자주 사용

import cv2
from utils import image_show

# 이미지 경로 지정
image_path = './cat.jpg'

# 이미지 이진화
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 픽셀사이에서 표현할수있는갯수 : 255
max_output_value = 255  # color가 0부터 255까지 있으므로
# 출력픽셀의 강도 : 0, 255
neighborhood_size = 99
subtract_from_mean = 5  # 이값이 커지면 흰색이 많아짐을 볼수있다(=많이 날라간다)
# 평균값, 수치값 , 변경하면서 봐보기

image_binary = cv2.adaptiveThreshold(image_gray, max_output_value,
cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, neighborhood_size,
subtract_from_mean)
# THRESH_BINARY_INV 으로 하면 : 흑백 컬러 반전됨

image_show(image_binary)