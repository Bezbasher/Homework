'''
Модуль операции деления
'''


def division(n1,n2:float) -> float:
    '''
    Функция операции деления
    :param n1: float
    :param n2: float
    :return: float
    Возвращает результат деления
    '''
    if n2 != 0:
        return n1/n2
    else:
        return 'Fail! DivisionZero'
