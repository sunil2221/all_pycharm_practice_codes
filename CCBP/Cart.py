class Cart:
    def __init__(self):
        self.items = {}
        self.price_details = {"book": 10, "laptop": 30000}


    def add_item(self, item_name, quantity):
        self.items[item_name] = quantity

    def get_items(self):
        items_list = []
        items_list = list(self.items.keys())
        print(items_list)

    def remove_item(self, item_name):
        del self.items[item_name]

    def update_quantity(self, item_name, quantity):
        self.items[item_name] = quantity
    def get_total_price(self):
        total_price = 0
        for item_name, quantity in self.items.items():
            total_price += self.price_details[item_name] * quantity
        return total_price

cart_obj = Cart()
cart_obj.add_item("book", 10)
cart_obj.get_items()
cart_obj.add_item("laptop", 1)
# cart_obj.remove_item("book")
cart_obj.get_items()
print(cart_obj.get_total_price())