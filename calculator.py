num1 = int(input(('Enter num 1 here : ')))
opt = input('Enter operator here : ')
num2 = int(input('Enter num2 here : '))

if opt == '+':
    print(f'{num1} + {num2} : {num1 + num2}')
elif opt == '-':
    print(f'{num1} - {num2} : {num1 - num2}')
elif opt == '*':
    print(f'{num1} - {num2} : {num1 * num2}')
elif opt == '/':
    print(f'{num1} * {num2} : {num1 * num2}')
else:
    print('Invalid input')
