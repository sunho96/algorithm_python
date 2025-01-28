def check_number(number):
    number = int(number)
    if number % 2 == 0 :
        return "짝수입니다."
    else: return "홀수입니다."


num = input("숫자를 입력하세요:")
print(check_number(num))
