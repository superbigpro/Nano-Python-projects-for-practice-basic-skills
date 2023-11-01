import random

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"
SPECI = ";!@#$%"

while True:
    print("비밀번호 생성기")
    diff = int(input("비밀번호 강도 선택: 1. 어려움 / 2. 보통 / 3. 쉬움: "))

    if diff == 1:
        password_length = 15
    elif diff == 2:
        password_length = 10
    elif diff == 3:
        password_length = 5
    else:
        print("잘못된 선택입니다. 1, 2, 또는 3 중에서 선택하세요.")
        continue

    rand_password = ""

    for i in range(password_length):
        rand_category = random.randint(0, 2)

        if rand_category == 0:
            rand_password += random.choice(UPPER)
        elif rand_category == 1:
            rand_password += random.choice(LOWER)
        elif rand_category == 2:
            rand_password += random.choice(SPECI)

    print("생성된 비밀번호:", rand_password)
    another = input("다른 비밀번호를 생성하시겠습니까? (예/아니오): ")

    if another != '예':
        break
