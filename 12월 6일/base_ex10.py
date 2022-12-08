'''
팽창 두번이상 적용위해 : 반복횟수라는 매개변수 사용
매개변수를 10으로 설정할 수 있다.
이는 확장 프로세스가 연속적으로 10번 반복됨을 의미함
결과 이미지에서 훨씬 더 많은 검은색 영역이 이미지에서 사라진 반면 흰색 영역은 확장된 것을 볼 수 있다

흰색 영역의 확대를 높이려면 더 큰 커널을 사용할 수 있다
ex) 5x5 크기의 커널을 사용하면 확장된 이미지에서 흰색 영역이 훨씬 더 확장됨
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img_gray = cv2.imread('./Billiards.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img_gray, 230, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3, 3), np.uint8)
dliation = cv2.dilate(mask, kernel, iterations=5)

titles = ['image', 'mask', 'dliation']
images = [img_gray, mask, dliation]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
