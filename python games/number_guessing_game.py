import random

def guess_number():
    number_to_guess = random.randint(1,50)
    attempts = 0
    guessed = False

    print('welcomne to the number guessing game !')
    print("T'm thinking a number between 1 to 50 can you guess it ?")

    while not guessed:
        user_guess = int(input('Enter your num here : '))
        attempts += 1

        if user_guess < number_to_guess:
            print('Too low guess higher !')
        elif user_guess > number_to_guess:
            print('Too high guess lower !')
        else:
            guessed = True
            print(f'congratulation ! you guessed the number {number_to_guess} in {attempts} attempts ')


guess_number()