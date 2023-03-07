#파이썬 기초점검

"""
파이썬 코드 작성 원리
1. 구성요소: 객체(object), 함수(function), 인자(argument)
2. 객체생성
3. 객체.함수(인자) -> 특정 자료(객체)에 대해 특정 조건(인자)으로 변화를 가함(함수)
4. 변화의 결과를 또 다른 객체로 할당 가능
"""





text = "우리는 파이썬 실습을 하고 있는 중이다. 열심히 하자"
text #출력
text.split(" ")#띄어쓰기 기반 리스트 생성
text1 = text.split(" ") #새로운 객체에 할당
text1 #출력







#파이썬을 통한 사칙연산
print(1+2)
print(50-3)
print(23*3)
print(24/6)
print(divmod(40, 9)) #나눗셈과 나머지를 출력하는 함수





#변수(variable): 임의의 숫자와 문자를 할당하는 대상
watch = 100000
bag = 200000
print(watch+bag)






a = 'school'
b = 'knowledge and human beings'
print(a+b)






#리스트 데이터 생성
#특정 변수가 가지고 있는 리스트 데이터 생성
family = ['mother', 'father', 'brother', 'sister']
len(family)#len()함수는 리스트에 원소가 몇 개 들어있는지 보여줌
family[3]#4번째 원소가 무엇인지 확인 (0부터 시작)
family.remove('brother')#하나의 원소 삭
family#결과확인






#인터프리터(interpreter)와 컴파일러(complier)
"""
컴퓨터에 명령어를 할 때마다 동시통역을 해주는 방식: interpret 방식 (대화식)
컴퓨터가 처음부터 끝까지 듣고 한꺼번에 바꿔주는 것: compile 방식 
파이썬은 intepreter방식 
https://www.youtube.com/watch?v=Dx2tSsd3aFc&ab_channel=%EC%A0%84%EB%87%8C%ED%95%B4%EC%BB%A4
"""






#인터프리터 방식 프로그램 파일 실행
print('직각삼각형 그리기\n') #해당 문장 출력후 아래 한칸 띄우기
leg = int(input('변의 길이: ')) #몇 개의 변을 입력할 것인지 정수 입력형 변수 생성
for i in range(leg): #for문을 활용해 leg 변수를 불러온 후 세로축 변수생성
    print('* ' * (i + 1)) #할당된 변수 숫자에 *를 하나씩 추가
area = (leg ** 2) / 2 #면적 구하기 공식; 입력 정수의 차승 나누기 2
print('넓이:', area) #출력하기






#while문
#1, 2, 3, ..., 98, 99, 100 출력
num = 1 #1이라는 숫자 변수생성
while num <= 100: #해당 변수가 100보다 작거나 같으면
    print(num) #출력
    num = num + 1 #1+1후 다시 while문 조건으로 입력






#조건문
if a > b:
    print('a')
else:
    print('b')







#다중조건
c = 5*5
d = 5 + 5 + 5 + 5 + 5
if c > d:
    print('c는  d보다 크다')
elif c == d:
    print('c는 d와 같다')
elif c < d:
    print('c는 d보다 작다')
else:
    print('잘 모르겠다')
#출력값은?








#조건에 따라 반복문 중단
max = 10
while True:
    num = int(input())
    if num > max:
        print(num, '너무 숫자가 크다')
        break
#위 코드 설명하시오







#for 를 사용하는 반복문
family = ['mother', 'father', 'brother', 'sister'] #변수 생성
for x in family: #해당 변수에서 새로운 원소 생성
    print(x, len(x)) #각 원소 별 숫자 파악 후 출력






#for문 비교
a = [4, 5, 6, 7]
for i in a:
    print(i)





for i in range(4, 8): #range는 주어진 숫자조건에서 있는 정수 출력; 4이상 8 미만
    print(i)







#함수
#함수는 한 줄씩 입력을 줄이기 위해 공식을 사전에 구성함
def my_function(food):
    for x in food:
        print(x)
food = ['apple', 'banana', 'cherry']
my_function(food)








#practice
from turtle import *
shape('turtle')
def polygon(side, n):
    for i in range(n):
        forward(side)
        left(180 - (n -2)* 180 / n)
polygon(100, 3)
reset()
polygon(200,4)
reset()







#return 적용: y = ax+ b함수 생성
def f1(x):
    a = 3
    b = 5
    y = a * x + b
    return y
c = f1(10)
print(c)








#람다 (lambda): 복잡한 함수를 한 줄로 만들경우
def sum(x, y):
    return x + y
sum(3, 4)
(lambda x, y: x + y)(3, 4) #lambda 출력결과비교







"""
데이터 유형 
1. 자료형
2. 문자열 (str)과 리스트(list)
3. 튜플 (tuple)
4. 딕셔너리(dict)
5. 세트(set)
"""







type(6)
type('python')
type(1.45)#부동소수점수
type(3+5j)#복소수
type("Love your Enemies, for they tell you your Faults.")#문자
type(['love', 'enemy', 'fault'])#리스트
type(('love', 'enemy', 'fault'))#튜플
type({'one': 1, 'two': 2, 'three': 3}) #딕셔너리
type(False) #참/거짓을 판별하는 불(bool)형
type(3 >= 1)  #참/거짓을 판별하는 불(bool)형
fruits = {'apple', 'banana', 'orange'}
type(fruits)# 세트형






#모듈
#타 개발자가 만들어놓은 프로그래밍 꾸러미
#import
import math
math.sqrt(3)
math.pi







import calendar
calendar.prmonth(2023, 1)







from tkinter import *
widget = Label(None, text = 'Always be happy')
widget.pack()







"""
기타모듈 (https://wikidocs.net/78) 
1. sys : 파이썬 인터프리터를 제어할 수 있는 모듈
2. os : operating system을 제어할 수 있는 모듈
3. re : 정규표현식 (regular expression) 모듈 
"""






#연습
#https://www.w3schools.com/python/exercise.asp
