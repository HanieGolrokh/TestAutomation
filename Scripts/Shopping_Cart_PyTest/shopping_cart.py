class ShoppingCart:
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
