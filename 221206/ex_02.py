# 가우시안블러 : 조금 더 부드러운 블러표현
# 야간, 저녁 이미지에는 별로임 

import cv2
from utils import image_show

image_path = './cat.jpg'

# 이미지읽기
image = cv2.imread(image_path)
print(image)

image_g_blury = cv2.GaussianBlur(image, (7, 7), 0)  # 여기 숫자를 바꿔가며 blur처리해서 비교해보기
image_show(image_g_blury)

