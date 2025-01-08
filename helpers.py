import random
import string

from data.data import User

def generate_new_user_data():
    email = generate_random_string(10) + '@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    return User(email, password, name)

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string