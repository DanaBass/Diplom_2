import allure
import pytest

import helpers
from data.messages import USER_ALREADY_EXISTS_MESSAGE, REGISTER_WITHOUT_ALL_REQUIRED_FIELDS
from methods.auth_methods import AuthMethods


class TestUserCreation:
    @allure.title("Успешное создание нового пользователя с использованием всех необходимых полей")
    def test_create_new_user_with_all_fields_returns_successfull(self):
        status_code, json, user = AuthMethods.create_new_user(helpers.generate_new_user_data())

        assert status_code == 200 and json['success'], f'Info: status code: {status_code}, json: {json}, user: {user}'

    @allure.title("Создание пользователя с email, который уже существует в системе")
    def test_create_existing_user_returns_error(self, existing_user):
        status_code, json, user = AuthMethods.create_new_user(existing_user)

        assert status_code == 403 and json['message'] == USER_ALREADY_EXISTS_MESSAGE, f'Info: status code: {status_code}, json: {json}, user: {user}'

    @pytest.mark.parametrize(
        'user_data_for_register',
        [
            { 'email': 'testEmail123@yandex.ru', 'password': 'testP@ss133' },
            {'name': 'testName', 'password': 'testP@ss133'},
            {'name': 'testName', 'email': 'estEmail123@yandex.ru'},
        ]
    )
    @allure.title("Создание пользователя при отсутствии всех необходимых для регистрации полей")
    def test_create_new_user_without_all_fields_returns_error(self, user_data_for_register):
        status_code, json = AuthMethods.create_new_user_by_json(user_data_for_register)

        assert status_code == 403 and json['message'] == REGISTER_WITHOUT_ALL_REQUIRED_FIELDS,  f'Info: status code: {status_code}, json: {json}'


