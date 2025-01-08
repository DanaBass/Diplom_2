import allure
import pytest

from data.data import User
from data.messages import INCORRECT_EMAIL_OR_PASSWORD
from methods.auth_methods import AuthMethods


class TestUserLogin:
    @allure.title("Успешный вход в систему для существующего пользователя с верными данными")
    def test_login_by_existing_user_with_correct_data_returns_success(self, existing_user: User):
        status_code, json, user = AuthMethods.login_user(existing_user)

        assert status_code == 200 and json['success']

    @pytest.mark.parametrize(
        'field_name,field_value',
        [
            ('email', 'INc0RR3CT_email5125@yandex.ru'),
            ('password', 'INc0RR3CT_P@ssWORD777')
        ]
    )
    @allure.title("Неудачный вход в систему для существующего пользователя с неверными данными")
    def test_login_by_existing_user_with_incorrect_data_returns_error(self, existing_user: User, field_name, field_value):
        login_data_json = existing_user.get_login_json()
        login_data_json[field_name] = field_value # Подменяем данные для входа на некорректные.

        status_code, json = AuthMethods.login_user_by_json(login_data_json)

        assert status_code == 401 and json['message'] == INCORRECT_EMAIL_OR_PASSWORD