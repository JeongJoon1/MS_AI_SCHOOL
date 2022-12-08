# python에서 확장, 침식 실험 예시

import cv2
import numpy as np
import matplotlib.pyplot as plt

img_gray = cv2.imread('./Billiards.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img_gray, 230, 255, cv2.THRESH_BINARY_INV)  


# 3*3커널 만들기
kernel = np.ones((3, 3), np.uint8)  # uint8 = 부호없는 정수
print(kernel)
''' 아래와같은 행렬 만들어짐. 이걸 이용할것임
[[1 1 1]
 [1 1 1]
 [1 1 1]]
'''

dilation = cv2.dilate(mask, kernel)

titles = ['image', 'mask', 'dilation' ]  # 값이 3개이므로 아래 range(3)
images = [img_gray, mask, dilation]

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.axis('off')
    plt.xticks([])
    plt.yticks([])
plt.show()

# ? 침식image -> 팽창 mask -> 확장 dilation 순서로 노이즈 제거된모습 볼수있음