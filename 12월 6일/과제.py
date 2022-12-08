import cv2
import numpy as np

# 1. 얼굴 및 눈 감지 위해 OpenCV Hear 캐스케이드 구성
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# 2. 얼굴이미지 데이터읽기
img = cv2.imread('face.jpg')
cv2.imshow('image show', img)
cv2.waitKey(0)

# 2.2 얼굴이미지 바운딩박스 _ 그레이스케일 only
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)  
# detectMultiScale : 바운딩박스 좌표 획득 가능

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

cv2.imshow('face', img)
cv2.waitKey(0)

# 3. 눈 감지 : 사각형안에 위치할 두개의 관심영역 만들기
# roi = 관심영역
# face 전체에서 관심영역만 빼옴

# creating 2 regions of interest
roi_gray = gray[y:y+h, x:x+w] #이뒤에 .copy[] 해주지 않으면 원본이미지에 영향을 끼침
roi_color = img[y:y+h, x:x+w] 

# creating variable eyes
eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
index= 0

# creating for loop in order to divide one eye from another
# 첫번째눈과 두번째눈의 좌표를 각각 eye_1변수와 eye_2변수에 저장
for(ex, ey, ew, eh) in eyes:
    if index == 0:
        eye_1 = (ex, ey, ew, eh)
    elif index ==1:
        eye_2 = (ex, ey, ew, eh)

# Drawing rectangles around the eyes
    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0,0,255), 3)
    index = index + 1

cv2.imshow('face', img)
cv2.waitKey(0)


# 4. left_eye , right_ eye
if eye_1[0] < eye_2[0]:
    left_eye = eye_1
    right_eye = eye_2
else:
    left_eye = eye_2
    right_eye = eye_1


# 5. 두 눈의 중심점 사이에 선 긋기, 그전에 직사각형 중심점 좌표 계산하기
# calculating coordinates of a central points of the rectangles
left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
left_eye_x = left_eye_center[0]
left_eye_y = left_eye_center[1]
# 인덱스 0 : x좌표
# 인덱스 1 : y좌표
# 인덱스 2 : 사각형의 너비

right_eye_center = (int(right_eye[0] + (right_eye[2] / 2)), int(right_eye[1] + (right_eye[3] / 2)))
right_eye_x = right_eye_center[0]
right_eye_y = right_eye_center[1]

cv2.circle(roi_color, left_eye_center, 5, (255, 0, 0), -1)
cv2.circle(roi_color, right_eye_center, 5, (255, 0, 0), -1)
cv2.line(roi_color, right_eye_center, left_eye_center, (0, 200, 200), 3)

cv2.imshow('face', img)
cv2.waitKey(0)


# 6. 수평선 그리고 그 선과 눈의 두 중심점을 연결하는 선 사이의 각도 계산 
# # 최종목적 : 각도를 기준으로 이미지 회전시키는것
# 7. 왼쪽눈 y 좌표가 오른쪽는 y좌표보다 크면 이미지를 시계방향으로 회전한다. 반대는 반시계방향
if left_eye_y > right_eye_y:
    A = (right_eye_x, left_eye_y)
    direction = -1  # -1 = image will rotate in the clockwise direction
else:
    A = (left_eye_x, right_eye_y)
    direction = 1  # 1 = image will rotate in the clockwise direction

cv2.circle(roi_color, A, 5, (255, 0, 0), -1)

cv2.line(roi_color, right_eye_center, left_eye_center, (0, 200, 200), 3)
cv2.line(roi_color, left_eye_center, A, (0, 200, 200), 3)
cv2.line(roi_color, right_eye_center, A, (0, 200, 200), 3)

cv2.imshow('face', img)
cv2.waitKey(0)


# 각도 계산 : 직각삼각형의 두변의 길이 찾아야함
# np.arctan 함수는 라디안단위로 각도를 반환한다
# 유의결과를 각도로 변환하려면 : 각도 |(|theta |) * 180 / |(|pi|)
delta_x = right_eye_x - left_eye_x
delta_y = right_eye_y - left_eye_x
angle= np.arctan(delta_y / delta_x)
angle = (angle * 180) / np.pi


# 8. 이미지를 각도 \theta 만큼 회전할수있음
h, w = img.shape[:2]

center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, (angle), 1.0)

rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow('face', rotated)
cv2.waitKey(0)


# 9. 이미지 크기 조정 : 눈 사이의 거리를 참조프레임으로 사용
dist_1 = np.sqrt((delta_x * delta_x) + (delta_y * delta_y))
dist_2 = np.sqrt((delta_x_1 * delta_x_1) + (delta_y_1 * delta_y_1))

ratio = dist_1 / dist_2

h = 476
w = 488

dim = (int(w * ratio), int(h*ratio))

resized = cv2.resize(rotated, dim)

cv2.imshow('face', resized)
cv2.waitKey(0)