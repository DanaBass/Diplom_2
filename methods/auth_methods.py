import allure
import requests

from data.data import User
from data.urls import BASE_URL, AUTH_URL


class AuthMethods:
    @staticmethod
    @allure.step("Создание нового пользователя")
    def create_new_user(new_user: User):
        response = requests.post(f'{BASE_URL}{AUTH_URL}register', json=new_user.get_register_json())

        response_json = response.json()

        if response_json['success']:
            new_user.set_access_token(response_json["accessToken"])

        return response.status_code, response_json, new_user

    @staticmethod
    @allure.step("Создание нового пользователя")
    def create_new_user_by_json(new_user_json):
        response = requests.post(f'{BASE_URL}{AUTH_URL}register', json=new_user_json)
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(user: User):
        response = requests.post(f'{BASE_URL}{AUTH_URL}login', json=user.get_login_json())
        return response.status_code, response.json(), user

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user_by_json(user_login_data_json):
        response = requests.post(f'{BASE_URL}{AUTH_URL}login', json=user_login_data_json)
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(user: User):
        response = requests.delete(f'{BASE_URL}{AUTH_URL}user', json={'accessToken': user.access_token})
        return response.status_code, response.json(), user

    @staticmethod
    @allure.step("Изменение данных пользователя")
    def change_user_data(json_with_changed_fields, bearer_token=None):
        headers = {}
        if bearer_token is not None:
            headers['Authorization'] = bearer_token

        response = requests.patch(f'{BASE_URL}{AUTH_URL}user', json=json_with_changed_fields, headers=headers)
        return response.status_code, response.json()

