import allure
import pytest

from data.data import Ingredient
from methods.order_methods import OrderMethods


class TestCreateOrder:
    @pytest.mark.parametrize(
        'is_authorized,expected_status_code',
        [
            (True, 200),
            (False, 200)
        ]
    )
    @allure.title("Создание заказа в зависимости от статуса авторизации")
    def test_create_new_order_by_authorized_status(self, existing_user, ingredients, is_authorized, expected_status_code):
        """
        Ожидаем что в независимости от авторизации заказ можно создать.
        """
        status_code, json = OrderMethods.create_order(ingredients[:1], existing_user.access_token if is_authorized else None)

        assert  status_code == expected_status_code

    @pytest.mark.parametrize(
        'ingredients_count,expected_status_code',
        [
            (5, 200),
            (0, 400),
            (8, 200),
            (1, 200)
        ]
    )
    @allure.title("Создание заказов при разном количестве ингридиентов")
    def test_create_order_by_ingredients(self, ingredients, ingredients_count, expected_status_code):
        status_code, json = OrderMethods.create_order(ingredients[:ingredients_count])

        assert status_code == expected_status_code, f'Info: status code: {status_code}, json: {json}'

    @allure.title("Попытка создать заказ при заведомо неверном значении хеша ингридента")
    def test_create_order_with_invalid_ingredient_hash_returns_error(self, existing_user):
        incorrect_ingredients = [Ingredient('INVALID_ingredientHASH75172', 'invalid_ingredient')]
        status_code, json = OrderMethods.create_order(incorrect_ingredients)

        assert status_code == 500, f'Info: status code: {status_code}, json: {json}'