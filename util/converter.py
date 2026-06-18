from abc import ABC, abstractmethod
from products import Hamburger, Soda, Drink, HappyMeal
from users import Cashier, Customer


class Converter(ABC):

    @abstractmethod
    def convert(self, dataFrame, *args) -> list:
        pass  
  
    def print(self, objects):
        for item in objects:
            print(item.describe())


class CashierConverter(Converter):

    def convert(self, dataFrame, *args) -> list:    
        result = []

        for _, row in dataFrame.iterrows():
            cashier = Cashier( #creem objectes i els guardem a la llista.
                row["dni"],
                row["name"],
                row["age"],
                row["timetable"],
                row["salary"]
            )
            result.append(cashier)

        return result


class CustomerConverter(Converter):

    def convert(self, dataFrame, *args) -> list:
        result = []

        for _, row in dataFrame.iterrows():
            customer = Customer(
                row["dni"], # Accés per nom de columna (independent de l'ordre del CSV)
                row["name"],
                row["age"],
                row["email"],
                row["postalcode"]
            )
            result.append(customer)

        return result

class ProductConverter(Converter):

    def convert(self, dataFrame, *args) -> list:
        product_type = args[0]
        result = []

        for _, row in dataFrame.iterrows():
            if product_type == "Hamburger":
                product = Hamburger(row["id"], row["name"], row["price"])
            elif product_type == "Soda":
                product = Soda(row["id"], row["name"], row["price"])
            elif product_type == "Drink":
                product = Drink(row["id"], row["name"], row["price"])
            elif product_type == "HappyMeal":
                product = HappyMeal(row["id"], row["name"], row["price"])
            else:
                raise ValueError("Unknown product type")
            
            result.append(product)

        return result
    