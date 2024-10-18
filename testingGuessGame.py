import random

number = random.randint(0,10)
player = int(input("nanme?"))
while True:
    if player < number:
        print("low")
        player = int(input("low"))
    elif player > number:
        print("high")
        player = int(input("high"))
    else:
        print("you win")
        break    

