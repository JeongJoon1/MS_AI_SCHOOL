# 경계선 감지
# canny() 메소드 활용해 경계선 감지할수있다

import numpy as np
import cv2

# 이미지 읽기
image = cv2.imread('./test.jpg')

# 경계선 찾기 : canny() 할때는 무조건 gray scale로 바꿔줘야함
image_gray = cv2.imread('./test.jpg', cv2.IMREAD_GRAYSCALE)
# 중간값 찾기
mdeian_intensity = np.median(image_gray)
print(mdeian_intensity)
