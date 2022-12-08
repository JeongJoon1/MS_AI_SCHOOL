# 배경 제거
# 전경이 들어있는 영역주사위를 사각형으로 표시하고, 
# grabcut은 사각형밖에있는 모든것이 배경이라 가정하고 
# 이 정보를 사용하여 사각형안에있는 배경을 찾는다
import cv2
from utils import image_show
import numpy as np

# 배경 제거
image_path = './test.jpg'

# 이미지 읽어오기
image = cv2.imread(image_path)
print(image.shape) # 이미지 잘 불러와졌나 확인

# 사각형 좌표 : 시작점 : x, y, 넓이, 높이
rectangle = (0,0,400,400)

# 초기 마스크 생성
mask = np.zeros(image.shape[:2], np.uint8)

# grabCut에 사용할 임시배열 생성
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)


# grabcut 실행 
# (원본이미지, mask, background model, 전경model, 반복횟수, cv2) 순서로 넣기
# image -> 원본이미지, bdgModel -> 배경을위한 임시배열, fgdModel -> 전경배경, 
# 5-> 반복횟수, cv2.GC_INIT_WITH_RECT -> 사각형 초기화
cv2.grabCut(image, mask, rectangle, bgdModel,
fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# 배경인곳은0, 그외 1로 설정
mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

# 이미지에 새로운 마스크 곱해서 -> 배경제외
image_rgb_nobg = image * mask_2[:,:,np.newaxis]
image_show(image_rgb_nobg)