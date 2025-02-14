def calculate_love_score(name1, name2):
    # 모든 입력값을 소문자로 변환
    name1 = name1.lower()
    name2 = name2.lower()

    # 목표 문자 정의
    targets_true = ['t', 'r', 'u', 'e']
    targets_love = ['l', 'o', 'v', 'e']

    # 'TRUE' 글자의 총 개수 계산
    count_true = sum(name1.count(target) + name2.count(target) for target in targets_true)

    # 'LOVE' 글자의 총 개수 계산
    count_love = sum(name1.count(target) + name2.count(target) for target in targets_love)

    # LOVE SCORE 계산 및 출력
    love_score = int(str(count_true) + str(count_love))
    print(f"Your love score is: {love_score}")
    return love_score


# 함수 실행
calculate_love_score("Angela Yu", "Jack Bauer")