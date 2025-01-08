from typing import List

import allure
import requests

from data.data import Ingredient
from data.urls import BASE_URL, INGREDIENTS_URL


class IngredientMethods:
    @staticmethod
    @allure.step("Получение существующих в системе ингридиентов")
    def get_ingredients() -> List[Ingredient]:
        ingredients = []
        response = requests.get(f'{BASE_URL}{INGREDIENTS_URL}')

        for item in response.json()['data']:
            ingredients.append(Ingredient(item['_id'], item['name']))

        return ingredients