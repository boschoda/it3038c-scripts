import random

print('Hello, welcome to the guessing game! What is your name?')
userName = input()
print('Enter a number: ')

userNum = int(input())
ansNum = random.randint(0,100)

while userNum != ansNum:
    if  userNum < ansNum:
        print('Your guess is too low!')
        userNum = int(input())
    elif userNum >  ansNum:
         print('Your guess is too high!')
         userNum = int(input())
    else:
        print('You guessed right!')





