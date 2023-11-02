class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        for cart_item in self.items:
            if cart_item['name'] == item['name']:
                cart_item['quantity'] += quantity
                return
        item['quantity'] = quantity
        self.items.append(item)

    def remove_item(self, item_name, quantity=1):
        for item in self.items:
            if item['name'] == item_name:
                if item['quantity'] > quantity:
                    item['quantity'] -= quantity
                else:
                    self.items.remove(item)
                return

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.items)
        return total

    def apply_discount(self, discount_percentage):
        if discount_percentage > 0 and discount_percentage <= 100:
            discount_factor = 1 - discount_percentage / 100
            for item in self.items:
                item['price'] *= discount_factor

    def clear_cart(self):
        self.items = [] 

class cart_test:
    def test_add_item_to_cart(self):  
        cart = Cart()
        initial_item_count = len(cart.items)
        item1 = {'name': 'Product A', 'price': 10}
        item2 = {'name': 'Product B', 'price': 15}

        cart.add_item(item1, quantity=1)
        cart.add_item(item2, quantity=2)

        new_item_count = len(cart.items)
        assert new_item_count == initial_item_count + 2
        assert cart.calculate_total() == 40

    def test_remove_item(self):  
        cart = Cart()
        initial_item_count = len(cart.items)
        item1 = {'name': 'Product A', 'price': 10}
        item2 = {'name': 'Product B', 'price': 15}
        cart.add_item(item1, quantity=3)
        cart.add_item(item2, quantity=2)
        new_item_count = len(cart.items)

        cart.remove_item('Product A', quantity=2)

        assert new_item_count == 2
        assert new_item_count - initial_item_count == 2
        assert sum(item['quantity'] for item in cart.items) == 3

    def test_calculate_total(self):  
        cart = Cart()
        item1 = {'name': 'Product A', 'price': 10}
        item2 = {'name': 'Product B', 'price': 15}
        cart.add_item(item1, quantity=3)
        cart.add_item(item2, quantity=2)
        assert cart.calculate_total() == 60

    def test_apply_discount(self):  
        cart = Cart()
        item1 = {'name': 'Product A', 'price': 10}
        item2 = {'name': 'Product B', 'price': 15}
        cart.add_item(item1, quantity=3)
        cart.add_item(item2, quantity=2)

        cart.apply_discount(10)

        assert cart.calculate_total() == 54

    def test_clear_cart(self):  
        cart = Cart()
        item1 = {'name': 'Product A', 'price': 10}
        item2 = {'name': 'Product B', 'price': 15}
        cart.add_item(item1, quantity=3)
        cart.add_item(item2, quantity=2)

        cart.clear_cart()

        assert len(cart.items) == 0
        assert cart.calculate_total() == 0

# tester = cart_test()

# tester.test_add_item_to_cart()
# tester.test_remove_item()
# tester.test_calculate_total()
# tester.test_apply_discount()
# tester.test_clear_cart()
  