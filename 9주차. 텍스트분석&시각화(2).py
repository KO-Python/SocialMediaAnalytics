import re






#분석텍스트생성 (디시인사이드글)
text = """
인간적으로 금관구 자리가 더 밸런스 좋지 않냐? 강남도 편하고 인천도 편하고 경기 남부 가기도 편하고, 수원 수지 판교 동탄
중랑 금관구보단 주민 민도, 이것저것 따지면 노원 도봉이 훨 나음
은평구 중랑구가 더 욕먹더라 ㅇㅇ 노도강 금관구보다 민주당 강세 성향이 더 쎈가 봐... 부동산 카페 조차도 노원구 성북구 성동구는 국힘의 공천 실수에 성동구는 민주당의 조은희라고까지 인정하는데, 은평구...
노도강 금관구는 대학병원 가는데 30~50분 정도 걸림 신도시는 2시간 잡아야 하고.
찐서울 아니잖아 노도강금관구 마포서대문은평종로중구 광진성북동대문중랑 영등포동작강서 강남송파강동 빼고 다 오르는중인데 누가 서울이 떨어진대 ㅋㅋㅋㅋㅋㅋㅋ 여긴 서울아니고 그랜드서울 혹은 서울권임...
이게 분당의 현실이다. 노도강보다는 재건축 사업성 안나오고 금관구보다는 나오고. 분당애들이 똥서울이라고 구로 금천 무시하는건 ㅇㅈ 근데 노도강보다도 분당이 밀리는게 팩트
금관구 노도강 은중강 구 중에 구로 따지면 10쓰레기인데 그 구안에 그나마 쓸만한 동 있냐?
대선 강남3구 몰표 노도강 금관구로 커버친거 보면 ㅇㅇ
강서 강남 강북 이동하기 편함 금관구살아라 최고다 후시대에 제2의 강남이다 강남은 꺼져
그게 불가능하니까 금관구임 ㅋㅋㅋㅋㅋㅋ
노도강 아파트 많아서 생활환경은 좋지만 출퇴근 거리 멂 금관구 출퇴근 거리는 가깝지만 목숨 내놓고 살아야 함
여기도 민주당 지지율 높은동네이긴 하지만 조선족이랑 짱깨새끼들 죄다 금관구쪽에 몰려있고 재개발도 들어가고 학군도 강북에서 제일 괜찮은 편이라 노도강 금관구 중에서는 제일 나아보임
금관구가 삼국지 간손미급은 되는 태명품도시인데
신도림쪽 아파트 단지들이 세금 존나 쳐맞아서 그런가 대선 때도 금관구에서 신도림-개봉-오류동 라인 아파트들만 유일하게 빨갛던데 이번엔 존나 오랜만에 구청장까지 이겼네
금관구=외노자 득실 득실 짱깨판 집값 ㅎㅌㅊ 김치인으로 태어나 금관구에 사는것만은 피해야 한다 노도강=그저 유사 서울 서울인척 하는 서울중 가장 아래 그리고 이 안에도 안껴주는 삽랑구도 잊지 마시긔
강남 접근성 때문이라는데 사실 강남 접근성은 관악보다는 동작이 더 좋음. 더군다나 금관구는 난개발에 인프라도 꼬였고 항공로 영향때문에 재개발해도 꼬일 수 밖에 없는데 뭔 생각인지 모르겠음. 심지어 서울...
근데 노도강금관구가 아직도 좆기도보다 저가임 여기서 하방이 막힌거임 그러니 서울집값이 호구가 아니야
금관구도 소위 아파트단지 모여있는동은 죄다 보수화되서 보수 찍던데 노도강은 아파트단지 금관구대비 훨씬많은데 진보뽑더라구요 근데 하늘궁 찍은새끼들은뭔지 ㅈㅅㅂ
금관구 장점:서울 동북부에 비하면 교통 괜찮음 단점:동네마다 다르지만 조선족이 많은편 서울에서 제일 중국어 간판이 많음 노도강 장점:조선족 청정지역임 아파트가 금관구에 비해 많음 단점:교통 불편
"""
print(text)









#문자열 불러오기
re.findall("금관구\w", text) #특정단어와 조사로 된 문자열 불러오기
re.findall("노도강\W", text) #특정단어와 특수부호(띄어쓰기포함)로 된 문자열 불러오기
re.findall("\d", text) #한 음절로 된 숫자 불러오기
re.findall("\D", text) #숫자 아닌 한 음절 불러오기
re.findall("\d구", text) #숫자와 구 가 쓰여진 문자열 불러오기
re.findall("\s", text) #공백문자(스페이스, 탭, 줄바꿈) 불러오기
re.findall("\S", text) #공백문자(스페이스, 탭, 줄바꿈) 아닌 한 음절 불러오기
re.findall("보수[화]", text)  # '경찰'에 '서' 또는 '은'이 붙는 문자열 불러오기
re.findall("[가-힣]", text)  # 한글로 된 음절 불러오기
re.findall("[a-zA-Z]", text)  # 영어로 된 음절 불러오기
re.findall("[0-9]", text)  # 숫자로 된 음절 불러오기
re.findall("[^가-힣a-zA-Z0-9]", text) #한글, 영어, 숫자 아닌 음절 불러오기









#함수적용수정
re.findall("노도강", text)  #text라는 문자열 전체에서 '노도강' 모두 불러오기
re.search("노도강", text)  #text라는 문자열 전체에서 첫번째 '노도강'이 어디에 있는지 확인
re.split(" ", text)  #  mytext라는 문자열 전체를 " "(공백) 기준으로 분리
re.sub("노도강", "노원구.도봉구.강북구", text)  #  mytext라는 문자열 전체에서 '운전자'를 '소나타 운전자'로 교체
text.replace("금관구", "금천구.관악구")
