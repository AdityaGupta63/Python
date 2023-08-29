print('Welcome to State Bank of India')
pin = int(input('Please Your Bank Account Pin Here : '))
balance = 25000


if pin == 1234:
    print('press 1 for cash withdraw')
    print('press 2 for cash deposit')
    print('press 3 for balance enquiry')

    user = int(input('Please your equiry here : '))

    #To withdraw money
    if user == 1:
        cw1 = int(input('Enter the amount which you like to withdraw : '))
        if cw1>balance:
            print('insufficient balance...')
        elif cw1 <= balance:
            new_balance = balance-cw1
            print(f'{cw1} rupees has been deducted from your account')
            print(f'Your current balance is {new_balance}.')

    #To deposit money
    elif user == 2:
        cd1 = int(input('Enter the amount which you like to deposit : '))
        new_balance = balance + cd1
        print(f'You deposit {cd1} rupees in your account.')
        print(f'Now Your current Balance is {new_balance}.')

    #To check Balance
    elif user == 3:
        print(f'Your current Balance is {balance}')

    else:
        print('Invalid input !')

else:
    print('Sorry Your Atm pin is wrong...please try again !')

