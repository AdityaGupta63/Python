marks = int(input('Enter your marks here : '))

if marks >= 90:
    print('Congrats you got A++ grade')
elif marks >= 80:
    print('Congrats you got A+ grade')
elif marks >= 70:
    print('You got B+ grade')
elif marks >= 60:
    print('You got B grade')
elif marks >= 50:
    print('You got C grade')
elif marks >= 40:
    print('You got D grade')
elif marks >= 30:
    print('You got E grade')
elif marks > 20:
    print('oops you are not qualified :()')
else:
    print('Invalid Input')