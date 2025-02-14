def is_prime(num):
    # 1은 소수가 아님
    if num <= 1:
        return False
    # 2는 소수
    if num == 2:
        return True
    # 짝수는 소수가 아님
    if num % 2 == 0:
        return False
    # 3 이상 홀수의 경우
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# 함수 호출
number = int(input("Enter a number: "))
print(is_prime(number))