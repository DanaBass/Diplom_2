import allure

from data.data import User
from methods.order_methods import OrderMethods


class TestOrderGetting:

    @allure.title("Получение заказов для нового авторизованного пользователя")
    def test_get_order_by_authorized_new_user_returns_zero_orders(self, existing_user: User):
        status_code, json = OrderMethods.get_orders(existing_user.access_token)

        assert status_code == 200 and json['success'] and len(json['orders']) == 0

    @allure.title("Получение заказов для неавторизованного пользователя")
    def test_get_order_by_not_authorized_user_returns_not_authourized_error(self):
        status_code, json = OrderMethods.get_orders()
        assert status_code == 401