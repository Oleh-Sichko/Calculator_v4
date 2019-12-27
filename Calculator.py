# Calculator v4
# Цей калькулятор буде на англійській мові 
# Цей калькулятор є менш функціональний ніж минула веріся але він є логічніший і його легко освоїти
from colorama import *
init()

print(Back.RED)
print(Fore.YELLOW)
print(Style.DIM)
calc = input('Write which calculator you want to use: Rounded (+) or Exact (-): ')
for i in range(999999999999999999999999999999999999999999):
    def round_calc():
        print(Back.CYAN)
        a = float(input('Write first number, please: '))
        what = input('Write action that you want do(+, -, /, *, ^, %): ')
        b = float(input('Write second number, please: '))
        
        if what == '+':
            c = a + b
            print(Back.MAGENTA)
            print(round(c, 1))
        elif what == '-':
            c = a - b
            print(Back.YELLOW)
            print(round(c, 1))
        elif what == '/':
            c = a / b
            print(Back.WHITE)
            print(round(c, 1))
        elif what == '*':
            c = a * b
            print(Back.GREEN)
            print(round(c, 1))
        elif what == '^':
            c = a ** b
            print(Back.BLUE)
            print(round(c, 1))
        elif what == '%':
            c = a % b
            print(Back.CYAN)
            print(round(c, 1))
        else:
            print('Error, try again...')
    if calc == '+':
        print(round_calc())

    def exact_calc():
        print(Back.CYAN)
        a = float(input('Write first number, please: '))
        assert a != ''
        what = input('Write action that you want do(+, -, /, *, ^, %): ')
        b = float(input('Write second number, please: '))
        assert b != ''
        
        if what == '+':
            c = a + b
            print(Back.MAGENTA)
            print(c)
        elif what == '-':
            c = a - b
            print(Back.YELLOW)
            print(c)
        elif what == '/':
            c = a / b
            print(Back.WHITE)
            print(c)
        elif what == '*':
            c = a * b
            print(Back.GREEN)
            print(c)
        elif what == '^':
            c = a ** b
            print(Back.BLUE)
            print(c)
        elif what == '%':
            c = a % b
            print(Back.CYAN)
            print(c)
        else:
            print('Error, try again...')
    
    if calc == '-':
        print(exact_calc())