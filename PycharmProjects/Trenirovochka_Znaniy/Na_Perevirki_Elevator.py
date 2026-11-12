import random

attempt = 1
max_attempt = 6

bot_choice = random.randint(1, 30)
print(bot_choice,"\n\n\n")
player = int(input("Write a number\n"))
difference = abs(player - bot_choice)

while (attempt < max_attempt):
    if difference == 0:
        print("You win")
        break
    elif 1 <= difference <=5:
        print("Hot")
    elif 6 <= difference <=10:
        print("Warm")
    elif 11 <= difference <=20:
        print("Cool")
    else:
        print("Cold")
    attempt +=1
    player = int(input("Write a number\n"))
    difference = abs(player - bot_choice)
    if attempt <= max_attempt:
        print("You lose secret number is ", bot_choice)


