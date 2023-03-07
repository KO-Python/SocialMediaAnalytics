#코드: 모두의 데이터 분석
#1. matplotlib 홈페이지
""" matplotlib.org 접속 후 tutorials 메뉴 클릭.
numpy tutorial 검색 후 Pyplot tutorial 클릭."""
import random
import numpy as np

#첫 번째 array 리스트 생성
array_1d = np.array([1, 2, 3, 4, 5])

#두 번째 array 리스트 생성
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(array_1d.shape)
print(array_2d.shape)
print(array_1d.size)
print(array_2d.size)

#넘파이 연산
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

#더하기
c = a + b
print(c)

#곱하기
d = a * b
print(d)

#사칙연산
print(np.add(10,100))
print(np.subtract(10,100))
print(np.multiply(10, 100))
print(np.divide(100,10))



"numpy 사용했을 때 코드"
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0., 5.,0.2) # evenly sampled time at 200ms intervals
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') # red dashes, blue squares and green triangles
plt.show()






"numpy 사용하지 않았을 때 코드"
t = []
p2 = []
p3 = []
for i in range(0, 50, 2):
    t.append(i/10)
    p2.append((i/10)**2)
    p3.append((i/10)**3)
plt.plot(t, t, 'r--', t, p2, 'bs', t, p3, 'g^')
plt.show()







#2. numpy 라이브러리 시작하기
print(np.sqrt(2)) #np로 줄여서 사용 가능 import numpy as np
print(np.pi) #파이 값 출력
print(np.sin(0)) #삼각함수 값 출력
print(np.cos(np.pi))

a = np.random.rand(5) #rand() 함수 0~1 사이에 있는 n개의 실수 랜덤 생성
print(a)
print(type(a)) #<class 'numpy.ndarray'>: nd = N-Dimensional. array = 배열.

print(np.random.choice(6, 10)) # 6미만의 숫자에서 10번 랜덤 선택해라
print(np.random.choice(10, 6, replace=False)) #10번 미만의 숫자를 6번 선택하는데 중복되면 선택하지 않는다.
print(np.random.choice(6, 10, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])) #p값(확률)을 지정할 수 있다. 총 6개의 확률이 있어야하며 총합은 1이 되어야 함.






#3. numpy 라이브러리를 활용해 그래프 그리기
"numpy 라이브러리 활용했을 때"
dice = np.random.choice(6, 10)
plt.hist(dice, bins=6)
plt.show()

"random 라이브러리 활용했을 때"
dice = []
for i in range(10):
    dice.append(random.randint(1,6))
plt.hist(dice, bins = 6)
plt.show()

"100만 번 시도했을 때"
dice = np.random.choice(6, 1000000, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])
plt.hist(dice, bins=6) # 0~5 중 랜덤으로 추출한 숫자 히스토그램 표현
plt.show()

"numpy를 사용한 버블 차트 그리기"
x = np.random.randint(10, 100, 200) #10에서 100까지 200번 추출
y = np.random.randint(10, 100, 200)
size = np.random.rand(200) * 100 #0~1 사이에서 n개의 실수를 만들고 100을 곱함. *책 오류

plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()



####################################



#4. numpy array 생성하기
"ndarray = N차원 배열"
a = np.array([1,2,3,4])
print(a) #리스트와 비슷하지만 쉼표(,)가 없다는 차이점이 있다.
print(a[1], a[-1]) #인덱스 가능
print(a[1:]) #슬라이싱 가능
"numpy array 한 가지 타입의 데이터만을 저장할 수 있다. ex) 3개 정수, 1개 문자면 전부 문자열로 변환"

"zeros(), ones(), eye()"
a = np.zeros(10) #10개의 0으로 이루어진 배열 생성
print(a)

a = np.ones(10) #10개의 1로 이루어진 배열 생성
print(a)

a = np.eye(3) # 3행 x 3열의 단위 배열 생성 (0,1)
print(a)

"0과 1이 아닌 다른 숫자 배열"
print(np.arange(3)) #하나 입력하는 경우: 0부터 해당 숫자보다 1 작은 숫자까지
print(np.arange(3,7)) #두개 입력하는 경우: 첫 번째 숫자부터 두 번째 숫자보다 1 작은 숫자까지
print(np.arange(3,7,2)) #세개 입력하는 경우: 첫 번째 숫자부터 두 번째 숫자보다 1 작은 숫자까지 세 번째 숫자만큼 간격 둠.

a = np.arange(1, 2, 0.1) #1이상 2미만 0.1 간격 실수 생성
b = np.linspace(1, 2, 11) #1이상 2이하 11개 구간으로 나눈 실수 생성







#5. numpy array의 다양한 활용
"0과 1이 아닌 다른 숫자 배열 (zeros 응용)"
a = np.zeros(10)+5
print(a)

a = np.linspace(1, 2, 11)
print(np.sqrt(a)) #a값의 제곱근을 출력함

"함수 적용"
a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.show()

a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.plot(a, np.cos(a))
plt.plot(a+np.pi/2, np.sin(a))
plt.show()

"mask = 어떤 조건에 부합하는 데이터만 선별적으로 저장하기 위한 기능"
a = np.arange(-5, 5)
print(a)
print(a<0) #[TRUE or FALSE]
print(a[a<0]) #[부합하는 값 추출]

mask1 = abs(a) > 3 #abs(): 배열에 저장된 원소의 절대값. a배열에 저장된 원소의 절대값이 3보다 크다.
print(a[mask1])

mask1 = abs(a) > 3
mask2 = abs(a) % 2 == 0
print(a[mask1+mask2]) #둘 중 하나의 조건이라도 참일 경우
print(a[mask1*mask2]) #두 조건이 모두 참일 경우

"mask 적용한 버블 차트"
x = np.random.randint(-100, 100, 1000) #1000개의 랜덤 값 추출
y = np.random.randint(-100, 100, 1000)
size = np.random.rand(100) * 100
mask1 = abs(x) > 50 #x에 저장된 값 중 절대값이 50보다 큰 값 추출
mask2 = abs(y) > 50
x = x[mask1+mask2] # mask1, mask2 중 하나라도 만족하는 값 저장
y = y[mask1+mask2]

plt.scatter(x, y, c=x, cmap='jet', alpha=0.7) #size error
plt.colorbar()
plt.show()