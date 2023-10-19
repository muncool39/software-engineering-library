import datetime

# 현재 날짜 구하기
current_date = datetime.date.today()

# 사용자의 생년월일 입력 받기
birth_year = int(input("태어난 년도를 입력하세요 (예: 2012): ")
birth_month = int(input("태어난 월을 입력하세요 (1부터 12까지): ")
birth_day = int(input("태어난 일을 입력하세요: ")

# 사용자의 생년월일을 날짜 객체로 변환
birth_date = datetime.date(birth_year, birth_month, birth_day)

# 나이 계산
age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

# 결과 출력
print("당신은 현재 {}세입니다.".format(age))
