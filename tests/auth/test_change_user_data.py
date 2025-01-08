import allure
import pytest

import helpers
from data.data import User
from methods.auth_methods import AuthMethods


class TestChangeUserData:

    @pytest.mark.parametrize(
        'changed_field_name,new_field_value,is_authorized,expected_status_code',
        [
            ('email', helpers.generate_random_string(10) + '@yandex.ru', True, 200),
            ('name', helpers.generate_random_string(10), True, 200),
            ('email', helpers.generate_random_string(10), False, 401),
            ('name', helpers.generate_random_string(10), False, 401),
        ]
    )
    @allure.title("Изменение поля пользователя в зависимости от того, авторизован он или нет")
    def test_change_user_field(self, existing_user: User, changed_field_name, new_field_value, is_authorized, expected_status_code):
        """
        Проверяет изменение полей пользователя в зависимости от того, авторизован он или нет.
        Если авторизован - ожидаем успешный ответ и что поле действительно изменилилось.
        Если не авторизован - ожидаем ошибку.
        """
        json_for_change = {
            changed_field_name: new_field_value
        }

        status_code, json = AuthMethods.change_user_data(json_for_change, existing_user.access_token if is_authorized else None)

        assert  status_code == expected_status_code

        if is_authorized:
            assert json['success'] and json['user'][str(changed_field_name)] == new_field_value