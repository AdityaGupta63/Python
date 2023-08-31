import random

print('Welcome to the Number Guessing Game.')

lower = int(input('Enter the lower number you want to select : '))
high = int(input('Enter the higher number you want to select : '))

win_num = random.randint(lower, high)
attempts = 0

print(f'Now you guess a number between {lower} to {high}.')

while True:
    attempts +=1
    user_guess = int(input('Enter your guess here : '))
    if user_guess > win_num:
        print('Your guess is high!')
    elif user_guess < win_num:
        print('Your guess is low!')
    elif user_guess == win_num:
        print(f'Congrats your guess {user_guess} is right...!') 
        print(f'You took {attempts} attempts to guess right number.')
        break   
    else:
        print('Invalid input!')