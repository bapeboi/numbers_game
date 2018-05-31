print ("hello, and welcome to my game")
print (input(str("what is your name:")))
print ("nice to meet you!")

import random

print("========================================")

random_num = random.randrange(1, 101)

guess = -1

while random_num != guess:
    guess = int(input("say a number and i'll tell you if its close or not:"))
    if random_num == guess:
        print ("you got it! thanks for playing and good job, see you next time.")
    elif guess > random_num:
        print ("your guess is too high. guess again")
    else:
        print ("your guess is too low. guess again")













