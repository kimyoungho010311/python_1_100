import random
import art
from game_data import data
from art import logo
from colorama import Fore, Style

# 초기값 설정
score = 0
repeat = True

# 함수 정의
def extract_info(account):
    """데이터에서 필요한 정보를 추출합니다."""
    return account['name'], account['follower_count'], account['description'], account['country']

def compare_A_and_B(user_input, a_follower_count, b_follower_count):
    """사용자 입력과 A, B의 팔로워 수를 비교합니다."""
    if (user_input == 'a' and a_follower_count > b_follower_count) or \
       (user_input == 'b' and b_follower_count > a_follower_count):
        print("You got it!")
        return True
    else:
        print("You Lose...")
        return False

def realLocate_A_and_B(a, b):
    """정답을 맞춘 경우 A를 갱신하고 새로운 B를 생성합니다."""
    a = b
    b = random.choice(data)
    while a == b:  # 중복 방지
        b = random.choice(data)
    return a, b

# 게임 루프
a = random.choice(data)
b = random.choice(data)
while a == b:  # 중복 방지
    b = random.choice(data)

while repeat:
    # 데이터 추출
    a_name, a_follower_count, a_description, a_country = extract_info(a)
    b_name, b_follower_count, b_description, b_country = extract_info(b)

    # 출력
    print(Fore.CYAN + Style.BRIGHT + logo)
    print('==================================\n')
    print(f"Compare A : {a_name}, a {a_description}, from {a_country}")
    print(art.vs)
    print(f"Against B : {b_name}, a {b_description}, from {b_country}")

    # 사용자 입력
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    # 정답 확인
    if not compare_A_and_B(user_input, a_follower_count, b_follower_count):
        repeat = False  # 게임 종료
    else:
        score += 1
        a, b = realLocate_A_and_B(a, b)  # 정답에 따라 A와 B 갱신

    print(f"\nCurrent Score: {score}")

print("Game Over")