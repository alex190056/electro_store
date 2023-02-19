class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, product_name, price_per_unit, quantity_in_store):
        self.product_name = product_name
        self.price_per_unit = price_per_unit
        self.quantity_in_store = quantity_in_store
        self.all.append(self)

    def get_total_price(self):
        return self.quantity_in_store * self.price_per_unit

    def apply_discount(self):
        return self.get_total_price() * self.pay_rate


item1 = Item('Смартфон', 10000, 20)
item2 = Item('Ноутбук', 20000, 5)

print(item1.get_total_price())
print(item2.get_total_price())

Item.pay_rate = 0.8
item1.apply_discount()
print(item1.price_per_unit)
print(item2.price_per_unit)
print(Item.all)
