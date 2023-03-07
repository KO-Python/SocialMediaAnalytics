#파이썬 기초(Python Basic)

#파일불러오기
df = open('9주차.constitution.txt')
text = df.read()#df의 내용을 읽어 text라는 객체에 저장
text #확인





#문자열(strings): ""를 반드시 써줘야함
s = "파이썬은 왜 배우는가?"
s
s_long = """파이썬은 왜 배워야 하는가? 파이썬은 무엇에 쓰이는가?
            파이썬이 어떤 분야에 사용되는지 자료조사를 충분히 한 후 
            내가 무엇을 중점적으로 사용할 지 생각하자."""
s_long
len(s)#단어 수 세기
s.startswith("파이썬")#문자열이 파이썬이라는 단어로 시작되는지 확인
s.endswith("?")#문자열이 물음표로 마치는지 확인
s.replace("왜 배우는가", "잘 배우자")
s_long.split(" ")
s_long = s_long.split()




q = '{}과 {}을 더한 값은?'.format(3, 1)






#숫자와연산
i = int("5")#정수
f = float("3.4")#부동소수점
3**2
x=2
x += 1 #x + 1을 x에 입력
x -= 1 #x - 1을 x에 입력






#리스트
l = list()
l = [23, 50, 30, 50]
l[0] #첫 번째 요소
l[-1] #마지막 요소
l[1:4] #두 번째에서 네 번째 요소까지 호출
l[3:] #네 번째 요소부터 마지막 요소까지 호출
len(l)
sum(l)
min(l)
max(l)
l.append(80)
l
l.sort()
l







#딕셔너리
dic = {"한국":"서울", "미국":"워싱턴", "중국":"베이징", "일본":"도쿄"}
dic["한국"]
dic.keys() #딕셔너리의 key 출력
dic.values() #딕셔너리의 value 출력
dic.items()# key와 value 쌍 출력






#모듈
import random # random이라는 이미 만들어진 모듈을 불러옴
from math import sqrt # math라는 모듈에서 sqrt라는 함수를 불러옴







#함수
def add_calculate(x, y, z):
    result = x + y - z
    return result    # x와 y를 더하고 z를 빼준 값을 구해주는 새로운 함수 add_calculate 생성






#논리비교
x=5
x == 5 # X는 5와 같은가?
x != 5 # X는 5와 같지 않은?
x > 5 # X는 5보다 큰가?
x < 5 # X는 5보다 작은가?







name = "홍길동"
x == 4 and name == "홍길동" # X는 4와 같고 이름이 홍길동인가?
x == 4 or name == "홍길동" # X는 4와 같거나 이름이 홍길동인가?






lst = [1,2,3,4,5]
5 in lst # 5가 lst라는 리스트에 있나?






#조건문
x=3
if x > 5:
    print("{}은 5보다 크다".format(x)) # x가 5보다 크면, "X는 5보다 크다"를 출력
elif x < 0:
    print("{}은 음수이다".format(x)) # x가 0보다 작으면, "X는 음수이다"를 출력
else:
    print("{}은 0과 5 사이에 위치한다".format(x)) # 위의 어떤 경우에도 해당되지 않으면, "X는 0과 5 사이에 위치한다"를 출력







#반복문
lst = ['한국', '미국', '중국']
for element in lst:
    print(element)  # lst 안의 '한국', '미국', '중국' 요소들을 순서대로 호출해 각각을 print. for 다음에는 element 이외에 어떤 기호를 써도 좋음.








#무한루프
x=1
while x < 10:
    x += 1  # x가 10보다 작은 동안에는 계속 1을 더해줌. 처음에 1이었던 x는 계속 1씩 증가하다, 10이 되자 while 조건에 걸려 실행 중단.
x










