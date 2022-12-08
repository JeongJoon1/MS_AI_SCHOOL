import cv2
import matplotlib.pyplot as plt

# image loading and input image -> gray
img = cv2.imread('./Billiards.png', cv2.IMREAD_GRAYSCALE)

# 230보다 작은 모든 값은 흰색 처리 / 230보다 큰 모든 값은 검은색이 된다
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)  
# _, : 필요없는 값이므로 비워둔다 / 230보다 큰값은 255로 저장된다

titles = ['image', 'mask']
images = [img, mask]

for i in range(2):
    plt.subplot(1, 2, i+1),
    plt.imshow(images[i], 'gray'),
    plt.title(titles[i]),
    plt.xticks([]),
    plt.yticks([]),
plt.show()

