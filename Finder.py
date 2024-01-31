import os
import shutil
import traceback

menu = f'''Ваша директория {os.getcwd()}
1. Создать файл
2. Удалить файл
3. Перемместить файл
4. Копировать файл
5. Создать папку
6. Удалить папку
7. Переместить папку
8. Копировать папку 
9. Выход'''


def create_file():
    name = input('Введите имя создаваемого файла:  ')
    if os.path.isfile(os.path.abspath(f'{name}.txt')) is True:
        return 'Файл уже существует!'
    else:
        open(f'{name}.txt', 'w')
        return f'Файл создан по адресу: {os.path.abspath(name)}'


def delete_file():
    name = input('Введите имя удаляемого файла:  ')
    if os.path.isfile(os.path.abspath(f'{name}.txt')) is True:
        os.remove(f'{name}.txt')
        return 'Файл удален'
    else:
        return f'Файла  не существует!'


def move_file():
    name = input('Введите имя файла:  ')
    src_path = input('Введите откуда переместить: ')+f'/{name}.txt'
    dst_path = input('Введите куда переместить: ')+f'/{name}.txt'
    shutil.move(src_path, dst_path)
    return f'Файл перемещен сюда {dst_path}'


def copy_file():
    name = input('Введите имя файла:  ')
    src_path = input('Введите откуда копировать: ')+name+'.txt'
    dst_path = input('Введите куда копировать: ')+name+'.txt'
    shutil.copy2(src_path, dst_path)
    return f'Файл скопирован сюда {dst_path}'


def create_dir():
    name = input('Введите имя создаваемой папки:  ')
    if os.path.isdir(os.path.abspath(name)) is True:
        return 'Папка уже существует!'
    else:
        os.mkdir(f'{name}')
        return f'Папка создана по адресу: {os.path.abspath(name)}'


def delete_dir():
    name = input('Введите имя удаляемой папки:  ')
    if os.path.isdir(os.path.abspath(name)) is True:
        os.rmdir(name)
        return 'Папка удалена'
    else:
        return f'Папки  не существует!'


def move_dir():
    name = input('Введите имя папки:  ')
    src_path = input('Введите откуда переместить: ')+f'/{name}'
    dst_path = input('Введите куда переместить: ')+f'/{name}'
    shutil.move(src_path, dst_path)


def copy_dir():
    name = input('Введите имя папки:  ')
    src_path = input('Введите откуда копировать: ')+f'/{name}'
    dst_path = input('Введите куда копировать: ')+f'/{name}'
    return shutil.copytree(src_path, dst_path)


while True:
    try:
        print(menu)
        vvod = input('Что будем делать?')
        match vvod:
            case '1':
                print(create_file())
            case '2':
                print(delete_file())
            case '3':
                print(move_file())
            case '4':
                print(copy_file())
            case '5':
                print(create_dir())
            case '6':
                print(delete_dir())
            case '7':
                print(f'Папка перемещена по адресу {move_dir()}')
            case '8':
                print(f'Папка скопирована, путьк папке {copy_dir()}')
            case '9':
                break
    except OSError as err:
        traceback.print_tb(err.__traceback__)
