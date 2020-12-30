"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

import hashlib
import os


def add_user(my_users, username, password):
    print('Пользователь не был найден и добавлен в базу пройдите авторизацию заново')
    salt = os.urandom(32)  # Новая соль для данного пользователя
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    my_users[username] = {  # Хранение ключа и соли
        'salt': salt,
        'key': key
    }


def verification_user(my_users, username, password):
    salt = users[username]['salt']  # Получение соли
    key = users[username]['key']  # Получение правильного ключа
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key == new_key


def checking_existence_user(my_users, username):
    return my_users.get(username)


if __name__ == '__main__':
    users = {}  # Простое демо хранилище

    username = input('Введите логин: ')
    password = input('Введите пароль: ')

    if checking_existence_user(users, username) == None:
        add_user(users, username, password)
        username = input('Введите логин: ')
        password = input('Введите пароль: ')
        if verification_user(users, username, password):
            print('Авторизация прошла успешно !!!')
        else:
            print('Авторизация не прошла !!!')

    else:

        if verification_user(users, username, password):
            print('Авторизация прошла успешно !!!')
        else:
            print('Авторизация не прошла !!!')
    print(users)
