import math
menu='''Что делаем?
1. Сложение
2. Вычитание
3. Умножение
4. Деление
5. Выход
'''

def addition(n1,n2):
    return n1+n2

def subtraction(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    if n2 != 0:
         return n1/n2
    else:
         return 'На 0 делить нельзя'


while True:
    try:
        n1=float(input('Введите первое число'))
        n2=float(input('Введите второе число'))
        print(menu)
        vvod=input('Выберите операцию:  ')
        match vvod:
            case '1':
                print(addition(n1,n2))
            case '2':
                print(subtraction(n1,n2))
            case '3':
                print(multiplication(n1,n2))
            case '4':
                print(division(n1,n2))
            case '5':
                break
    except:
        'Возникла ошибка'
