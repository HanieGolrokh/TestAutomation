from shopping_cart import ShoppingCart
import pytest

@pytest.fixture
def empty_cart():
    return ShoppingCart()

@pytest.fixture
def cart_with_items():
    cart = ShoppingCart()
    item1 = {'name': 'Product A', 'price': 10}
    item2 = {'name': 'Product B', 'price': 15}
    cart.add_item(item1, quantity=3)
    cart.add_item(item2, quantity=2)
    return cart

def test_add_item_to_cart(empty_cart):
    cart = empty_cart
    initial_item_count = len(cart.items)
    item1 = {'name': 'Product A', 'price': 10}
    item2 = {'name': 'Product B', 'price': 15}

    cart.add_item(item1, quantity=1)
    cart.add_item(item2, quantity=2)

    new_item_count = len(cart.items)
    assert new_item_count == initial_item_count + 2
    assert cart.calculate_total() == 45

def test_remove_item(cart_with_items):
    cart = cart_with_items
    initial_item_count = len(cart.items)

    cart.remove_item('Product A', quantity=2)

    new_item_count = len(cart.items)
    assert new_item_count == 2
    assert new_item_count - initial_item_count == 2
    assert sum(item['quantity'] for item in cart.items) == 3

def test_calculate_total(cart_with_items):
    cart = cart_with_items
    assert cart.calculate_total() == 60

def test_apply_discount(cart_with_items):
    cart = cart_with_items
    cart.apply_discount(10)

    assert cart.calculate_total() == 54

def test_clear_cart(cart_with_items):
    cart = cart_with_items
    cart.clear_cart()

    assert len(cart.items) == 0
    assert cart.calculate_total() == 0
