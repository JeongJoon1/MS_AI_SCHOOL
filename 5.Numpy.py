import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))


arr = np.zeros((3,3))
print(arr)

arr = np.empty((3,3))
print(arr)

arr = np.ones((3,3))
print(arr)

arr = np.arange(10)
print(arr)

arr = np.array([[1,2,3],[4,5,6]])
print(arr)

# 배열의 모양을 알려준다
print(arr.shape)   

#단순히 배열의 차원만 확인할수 있음
print(arr.ndim)

# 배열의 데이터타입이 궁금할때
print(arr.dtype)

# 정수형을 실수형으로 바꾸고싶을때
arr_float = arr.astype(np.float64)
print(arr_float.dtype)

arr_str = np.array(['1', '2', '3'])
print(arr_str.dtype) # 결과값 <U1 = 유니코드라는 뜻

arr_int = arr_str.astype(np.int64)
print(arr_int.dtype)

# ndarray, numpy 배열의 연산방법 : 같은차원의 배열끼리 연산이 됨
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

print(arr1 + arr2)
print(np.add(arr1, arr2))
print(arr1 * arr2)
print(np.multiply(arr1, arr2))

# ndarray 배열 슬라이싱 하기
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.ndim)
arr_1 = arr[:2,1:3]
print(arr_1)

print("arr[0,2] : %d" % arr[0,2])

print(arr[[0,1,2],[2,0,1]])

idx = arr > 3
print(idx)

print(arr[idx])

redwine = np.loadtxt(fname='winequality-red.csv', delimiter=';', skiprows=1)
print(redwine)

# 합계
print(redwine.sum())

# 평균
print(redwine.mean())

# 축(axis)
print(redwine.sum(axis=0))

print(redwine.mean(axis=0))

print("첫번째열 평균")
print(redwine[:,0].mean())

print("각 열에서 최대값")
print(redwine.max(axis=0))