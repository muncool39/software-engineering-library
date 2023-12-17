# 덧셈 함수
def add(x, y):
    return x + y

# 뺄셈 함수
def subtract(x, y):
    return x - y

# 곱셈 함수
def multiply(x, y):
    return x * y

# 나눗셈 함수
def divide(x, y):
    if y == 0:
        return "0으로 나눌 수 없습니다."
    return x / y

while True:
    # 사용자로부터 연산자와 숫자 입력 받기
    operator = input("사칙연산 중 하나를 입력 (+, -, *, /) 또는 'q'를 눌러 종료하세요: ")

    # 종료 조건
    if operator == 'q':
        break

    if operator not in ['+', '-', '*', '/']:
        print("올바른 연산자를 입력하세요.")
        continue

    num1 = float(input("첫 번째 숫자를 입력하세요: ")
    num2 = float(input("두 번째 숫자를 입력하세요: ")

    if operator == '+':
        print("연산결과:", add(num1, num2))
    elif operator == '-':
        print("연산결과:", subtract(num1, num2))
    elif operator == '*':
        print("연산결과:", multiply(num1, num2))
    elif operator == '/':
        print("연산결과:", divide(num1, num2))
