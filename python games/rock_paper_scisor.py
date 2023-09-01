import random

print('----------------Welcome to Rock, Paper Scisor game :) ------------------')
print('',end='\n')
print('',end='\n')

user_name = str(input('Please enter your name here : '))

print(f'-------Hello {user_name}--------')

cmp_points = 0
user_points = 0

while True:


    items = ['Rock', 'Paper', 'Scisor', 'rock', 'paper', 'scisor']
    random_items = random.choice(items)

    print('',end='\n')


    print('Now you choose something from Rock, paper and scisor.')
    user_input = str(input('Enter here : '))
    print('',end='\n')

    print(f'Computer choice is {random_items}.')
    print(f'Your choice is {user_input}.')

    if user_input == random_items:
        print('Round Tie...')
    elif user_input == 'stop':
           break

    if user_input == 'scisor' and random_items == 'paper':
            print(f'{user_name} win !')
            user_points +=1
            print(f'{user_name} points is {user_points}')
            print(f'Computer points is {cmp_points}')


    elif user_input == 'paper' and random_items == 'scisor':
            print('Computer win !')
            cmp_points +=1
            print(f'{user_name} points is {user_points}')
            print(f'Computer points is {cmp_points}')

    if user_input == 'rock' and random_items == 'scisor':
            print(f'{user_name} win !')
            user_points +=1
            print(f'{user_name} points is {user_points}')
            print(f'Computer points is {cmp_points}')


    elif user_input == 'scisor' and random_items == 'rock':
            print('Computer win !')
            cmp_points +=1
            print(f'{user_name} points is {user_points}')
            print(f'Computer points is {cmp_points}')


    if user_input == 'rock' and random_items == 'paper':
            print('Computer win !')
            cmp_points +=1
            print(f'{user_name} points is {user_points}')
            print(f'Computer points is {cmp_points}')

    elif user_input == 'paper' and random_items == 'rock':
            print(f'{user_name} win !')
            user_points +=1
            print(f'{user_name} points is {user_points}')
            print(f'Computer points is {cmp_points}')
   



    else:
        #  print('Invalid Input :(')
        pass
        print('',end='\n\n')