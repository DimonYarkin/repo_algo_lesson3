"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
import os


class Dicturl:
    def __init__(self):
        self.my_dict = {}

    def checking_existence_url(self, url):
        return self.my_dict.get(url) != None

    def add_url(self, url):
        print('Url не был найден и добавлен в Кэш')
        salt = os.urandom(32)  # Новая соль для url
        key = hashlib.pbkdf2_hmac('sha256', url.encode('utf-8'), salt, 100000)
        self.my_dict[url] = {  # Хранение ключа и соли
            'salt': salt,
            'key': key
        }


if __name__ == '__main__':
    my_obj_url = Dicturl()
    while True:
        user_url = input('Введите url (для выхода 0)')
        if user_url == '0':
            print(my_obj_url.my_dict)
            print('Работа завершена')
            break
        if not my_obj_url.checking_existence_url(user_url):
            my_obj_url.add_url(user_url)
        else:
            print('URL уже имеется в Кэше введите бругой')
