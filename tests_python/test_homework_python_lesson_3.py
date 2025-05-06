"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from tests_python.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product2():
    return Product("book2", 200, "This is a book", 1000)


@pytest.fixture
def cart(product):
    cart = Cart()
    cart.add_product(product, 5)
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1000)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_new_product(self, cart, product):
        assert product in cart.products
        assert cart.products[product] == 5

    def test_increase_product_quantity(self, cart, product):
        cart.add_product(product, 5)
        assert product in cart.products
        assert cart.products[product] == 10

    def test_decrease_product_quantity(self, cart, product):
        cart.remove_product(product, 1)
        assert product in cart.products
        assert cart.products[product] == 4

    def test_remove_product_by_quantity(self, cart, product):
        cart.remove_product(product, 5)
        assert product not in cart.products

    def test_remove_product(self, cart, product):
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear(self, cart):
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, cart, product2):
        cart.add_product(product2, 5)
        assert cart.get_total_price() == 1500

    def test_successful_buy(self, cart, product):
        cart.buy()
        assert product.quantity == 995

    def test_failure_buy(self, cart, product2):
        cart.add_product(product2, 1001)
        with pytest.raises(ValueError):
            cart.buy()
