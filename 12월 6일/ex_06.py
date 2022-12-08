# 이미지 회전
# rotate (이미지, 각도 )
# : rotate함수의 첫번째 매개변수 : 회전시킬 이미지 / 두번째변수 : 회전각도
import cv2

# 이미지 경로
image_path = './cat.jpg'

# 이미지 읽기
image = cv2.imread(image_path)

# 이미지 좌우및 상하반전
# 1 좌우 반전 0 상하 반전
dst_tmep1 = cv2.flip(image, 1)
dst_tmep2 = cv2.flip(image, 0)

cv2.imshow("dst_tmep1", dst_tmep1)
cv2.imshow("dst_tmep2", dst_tmep2)
cv2.waitKey(0)


# 읽은 이미지 각도 90도 돌리기
image90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)  # 반시계 = COUNTERCLOCKWISE 
image180 = cv2.rotate(image, cv2.ROTATE_180) # 180도 회전
image270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE) # 270도 회전

cv2.imshow('original image', image)
cv2.imshow('ratate_90', image90)
cv2.imshow('ratate_180', image180)
cv2.imshow('ratate_270', image270)

cv2.waitKey(0)


