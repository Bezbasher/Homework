'''
Модуль, выполнения программы сортировок разными способами сортировки
'''
# Импорт необходимых библиотек
import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from tkinter import messagebox
import sys

lst_sort = ('Сортировка пузырьком', 'Сортировка подсчетом',
            'Сортировка слиянием', 'Пирамидальная сортировка',
            'Быстрая сортировка', 'Поразрядная сортирока')


def main():
    '''
    Основная функция прогрраммы. Осуществляет считывание ввода или генерацию случааных чисел
    Выбор сортировки осуществляется пользователем, а функция запсукает необходимые подфункции
    для выполнения вычислений и вывода результата для пользователя.
    :return:
    '''
    try:
        if inpt_entr.get() == '':
            lst = gen_rand()
        else:
            lst = [int(i) for i in inpt_entr.get().split(',')]
        for i in lst_sort_box.curselection():
            match i:
                case 0:
                    values = [buble_sort(lst)[0], buble_sort(lst)[1], 'Пузырьковая сортировка']
                    tree.insert('', END, values=values)
                case 1:
                    values = [count_sort(lst)[0], count_sort(lst)[1], 'Сортировка подсчетом']
                    tree.insert('', END, values=values)
                case 2:
                    values = [merge_sort(lst)[0], merge_sort(lst)[1], 'Сортировка слиянием']
                    tree.insert('', END, values=values)
                case 3:
                    values = [heap_sort(lst)[0], heap_sort(lst)[1], 'Пирамидальная сортировка']
                    tree.insert('', END, values=values)
                case 4:
                    start_time = datetime.now()
                    values = [quick_sort(lst), datetime.now()-start_time, 'Быстрая сортировка']
                    tree.insert('', END, values=values)
                case 5:
                    values = [radix_sort(lst)[0], radix_sort(lst)[1], 'Поразрядная сортировка']
                    tree.insert('', END, values=values)
    except ValueError:
        messagebox.showerror(title='ОШИБКА!!',message='Некорректные значения поля ввода')


def buble_sort(lst):
    '''
    Функция "пузырьковой" сортировки.
    Выполняет алгоритм сортировки пузырьком.
    :param lst: list
    :return: list,datetime
    '''
    start_time = datetime.now()
    last_elem_index = len(lst) - 1
    for i in range(last_elem_index, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    total = datetime.now() - start_time
    return lst, total


def count_sort(lst):
    '''
    Функция сортировки подсчетом
    Выполняет алгоритм сортировки подсчетом.
    :param lst: list
    :return: list,datetime
    '''
    start_time = datetime.now()
    large = max(lst)
    c = [0] * (large+1)
    for i in range(len(lst)):
        c[(lst[i])] = c[lst[i]]+1
    c[0] -= 1
    for i in range(1, (large+1)):
        c[i] = c[i] + c[i - 1]
    result = [None] * len(lst)
    for x in reversed(lst):
        result[c[x]] = x
        c[x] -= 1
    total = datetime.now() - start_time
    return result, total


def merge_sort(lst):
    '''
    Функция  сортировки слиянием.
    Выполняет алгоритм сортировки слиянием.
    :param lst: list
    :return: list,datetime
    '''
    start_time = datetime.now()
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)
        a, b, c = 0, 0, 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                lst[c] = left[a]
                a += 1
            else:
                lst[c] = right[b]
                b += 1
            c+=1
        while a < len(left):
            lst[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            lst[c] = right[b]
            b += 1
            c += 1
    total = datetime.now() - start_time
    return lst, total


def heap_sort(lst):
    '''
    Функция  сортировки двоиччной кучей.
    Выполняет алгоритм сортировки двоиччной кучей.
    :param lst: list
    :return: list,datetime
    '''
    start_time = datetime.now()
    n = len(lst)
    for i in range(n, -1, -1):
        heapify(lst,n,i)
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst,i,0)
    total = datetime.now() - start_time
    return lst,total


def quick_sort(lst):
    '''
    Функция  быстрой сортировки.
    Выполняет алгоритм быстрой сортировки.
    :param lst: list
    :return: list
    '''
    sys.setrecursionlimit(100000)
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst if i < pivot]
        greater = [i for i in lst if i > pivot]
        return quick_sort(less) + [pivot]+ quick_sort(greater)


def radix_sort(lst):
    '''
    Функция  поразрядной  сортировки.
    Выполняет алгоритм поразрядной сортировки.
    :param lst: list
    :return: list,datetime
    '''
    start_time = datetime.now()
    max_digit = max([len(str(i)) for i in lst])
    radix = 10
    lists = [[] for i in range(radix)]
    for i in range(0,max_digit):
        for x in lst:
            digit = (x // radix ** i) % radix
            lists[digit].append(x)
        lst=[x for queue in lists for x in queue]
        lists=[[] for i in range(radix)]
    total = datetime.now() - start_time
    return lst,total

def heapify(lst,n,i):
    '''
    Функция  преобразования списка в двоичную кучу.
    Выполняет преобразование входного списка
    двоичную кучу для алгоритма сортироввки
    двоиччной кучей. Рекурсивная
    :param lst:
    :param n: int
    :param i: int
    :return: list
    '''
    large = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and lst[i] < lst[left]:
        large = left
    if right < n and lst[large] < lst[right]:
        large = right
    if large != i:
        lst[i], lst[large] = lst[large], lst[i]
        heapify(lst, n, large)

def clear():
    '''
    Функция очистки поля вывода
    :return: None
    '''
    tree.delete(*tree.get_children())
def clear_btn_entry():
    '''
    Функция очистки поля ввода
    :return: None
    '''
    inpt_entr.delete(0,'end')
def gen_rand():
    '''
    Функция генерации случайных чисел от 0 до 10000.
    Перемешивает числа в случайномм порядке в
    соответсвии с методом shuffle библиотеки random
    :return: list
    '''
    lst = [i for i in range(0,10000)]
    random.shuffle(lst)
    return lst
# Основное окно работы программы. Отображает кнопки для управления
# программой пользователем
root = Tk()
root.geometry('900x900')
root.title('Итоговая атестация')
# Поле для ввода данных
inpt_entr = Entry(width=30)
inpt_entr_label = tk.Label(text='''Ввведите последовательность 
        чисел через запятую, для 
        случайной генерации оставьте поле 
        пустым и нажмите Старт''',
                           width=30)
inpt_entr_label.grid(row=2, column=1)
inpt_entr.grid(row=3, column=1)
# Список доступных сортировок
lst_sort_box = tk.Listbox(root, selectmode=MULTIPLE, width=30, height=6)
lst_sort_box.grid(row=5, column=1)
lst_sort_label = tk.Label(text='Выберите тип/ы сортировок', width=30)
lst_sort_label.grid(row=4, column=1)
for i in lst_sort:
    lst_sort_box.insert(END, i)
# кнопка запуска приложения
start_btn = tk.Button(root, text='Старт', width=30, command=main)
start_btn.grid(row=2, column=2)
# Поле вывода результата
tree = ttk.Treeview(root, columns=('Number_count', 'Time', 'Sort'), show='headings')
tree.heading('Number_count', text='Последовательность')
tree.heading('Time', text='Время')
tree.heading('Sort', text='Сортировка')
tree.grid(row=1, column=1, columnspan=3)
# Кнопка очистки результата
clear_btn = tk.Button(root, text='Очистить таблицу', command=clear, width=30,height=1)
clear_btn.grid(row=4, column=2)
# кнопка очистки поля ввода
clr_btn_entry=tk.Button(root,text='Очистить поле вввода',command=clear_btn_entry,width=30)
clr_btn_entry.grid(row=3,column=2)
# Кнопка выхода из приложения
exit_btn = tk.Button(root, text='Выход', command=root.destroy, width=30,height=6)
exit_btn.grid(row=5, column=2)
root.mainloop()
