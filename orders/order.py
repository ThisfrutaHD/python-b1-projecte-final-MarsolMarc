from users import *
from products import *
from datetime import datetime


class Order:

    def __init__(self, cashier: Cashier, customer: Customer):
        self.cashier = cashier
        self.customer = customer
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def calculateTotal(self) -> float:
        total_price = 0

        for product in self.products:
            total_price += product.price
        return total_price
  
    def show(self):
        print("\n===== ORDER =====")
        print(f"\nHello: {self.customer.describe()}")
        print(f"\nWas attended by: {self.cashier.describe()}")
        print("\n--- PRODUCTS ---\n")
        for i, product in enumerate(self.products, start=1):
            print(f"Product {i}: {product.describe()}")
        print("\n------------------")
        print(f"Total price: {self.calculateTotal()}")
        print("==================\n")

    # Servira per implementar la funcio write de CSVFileManager
    def to_dict(self):
        return {
            "cashier_dni": self.cashier.dni,
            "customer_dni": self.customer.dni,
            "datetime": datetime.now(),
            "total": self.calculateTotal()
        }
