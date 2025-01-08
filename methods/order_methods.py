from typing import List

import allure
import requests

from data.data import Ingredient
from data.urls import BASE_URL, ORDERS_URL


class OrderMethods:
    @staticmethod
    @allure.step("Создание нвоого заказа")
    def create_order(ingredients: List[Ingredient], bearer_token=None):
        json = {
            'ingredients': [i.id for i in ingredients]
        }

        headers = {}
        if bearer_token is not None:
            headers['Authorization'] = bearer_token

        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=json, headers=headers)

        return response.status_code, response.json() if response.status_code != 500 else None

    @staticmethod
    @allure.step("Получение заказов")
    def get_orders(bearer_token=None):
        headers = {}
        if bearer_token is not None:
            headers['Authorization'] = bearer_token

        response = requests.get(f'{BASE_URL}{ORDERS_URL}', headers=headers)

        return response.status_code, response.json()

