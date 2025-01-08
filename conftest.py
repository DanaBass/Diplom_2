import pytest

import helpers
from methods.auth_methods import AuthMethods
from methods.ingredient_methods import IngredientMethods


@pytest.fixture
def existing_user():
    status_code, json, created_user = AuthMethods.create_new_user(helpers.generate_new_user_data())
    yield created_user

    AuthMethods.delete_user(created_user) # Удаление пользователя в конце работы тестов.

@pytest.fixture
def ingredients():
    return IngredientMethods.get_ingredients()