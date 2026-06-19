from users import *
from products import *


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
        print(f"Hello : {self.customer.describe()}")
        print(f"Was attended by : {self.cashier.describe()}")
        for product in self.products:
            print(product.describe())
        print(f"Total price : {self.calculateTotal()}")
