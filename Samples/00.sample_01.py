import random

random_number = random.randint(1, 100)

# print(random_number)

game_count = 0

while True:
    my_number = int(input("1-100 사이의 숫자를 입력하세요 "))
    
    if my_number > random_number:
        print("Down!!")
    elif my_number < random_number:
        print("Up!!")
    else:
        print(f"축하합니다. {game_count} 만에 맞추셨습니다.")
        break
    
    game_count += 1
    