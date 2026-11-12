class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = price
        print(f"Товар {name} додано за ціною {price} грн")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"Товар {name} видалено")
        else:
            print("Товар не знайдено")

    def total_price(self):
        total = sum(self.products.values())
        print(f"Загальна вартість {total} грн")
        return total

shop1 = Shop()
shop1.add_product("Молоко", 30)
shop1.add_product("Хліб", 20)
shop1.add_product("Сир", 80)
shop1.remove_product("Хліб")
shop1.total_price()
