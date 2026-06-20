from util import CSVFileManager, CashierConverter, CustomerConverter, ProductConverter
from orders import Order
from users import Cashier, Customer
from products import Product
import pandas as pd


class PrepareOrder:

    def __init__(self):
        self.cashiers = []
        self.customers = []
        self.products = []

    def load_data(self):
        # DataFrame + convert Cashiers
        df_cashiers = CSVFileManager("data/cashiers.csv").read()
        self.cashiers = CashierConverter().convert(df_cashiers)

        #D ataframe + convert Customers
        df_customers = CSVFileManager("data/customers.csv").read()
        self.customers = CustomerConverter().convert(df_customers)

        # Dataframe + converts products/hamburgers
        df_hamburgers = CSVFileManager("data/hamburgers.csv").read()
        hamburgers = ProductConverter().convert(df_hamburgers, "Hamburger")
       
        # Dataframe + converts products/sodas
        df_sodas = CSVFileManager("data/sodas.csv").read()
        sodas = ProductConverter().convert(df_sodas, "Soda")
        
        # Dataframe + converts products/drinks
        df_drinks = CSVFileManager("data/drinks.csv").read()
        drinks = ProductConverter().convert(df_drinks, "Drink")
        
        # Dataframe + converts products/happymeals
        df_happymeals = CSVFileManager("data/happyMeal.csv").read()
        happymeals = ProductConverter().convert(df_happymeals, "HappyMeal")
        
        # Unim els products en una mateixa llista
        self.products = hamburgers + sodas + drinks + happymeals

    def find_cashier(self, dni: str) -> Cashier | None:
        for cashier in self.cashiers:
            if cashier.dni == dni:
                return cashier
        return None
    
    def find_customer(self, dni: str) -> Customer | None:
        for customer in self.customers:
            if customer.dni == dni:
                return customer
        return None
    
    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def run(self):
        self.load_data()  # Carreguem la info

        #Mostro els caixers disponibles segons he entès en l'enunciat
        #En cas de no voler nomes esborrar
        print("\n--- CAIXERS DISPONIBLES ---\n")
        for c in self.cashiers:
            print(c.describe())
        print()
        
        # Cashier té 5 intents, si cap és correcte s'atura programa.
        max_attempts = 5
        attempts = 0
        cashier = None

        while attempts < max_attempts:
            cashier_dni = input("Introdueixi el DNI del caixer: ")
            cashier = self.find_cashier(cashier_dni)
            if cashier is not None:
                break
            print("DNI del caixer no trobat...")
            attempts += 1
        if cashier is None:
            print("Massa intents. Reinicia el programa.")
            return  # Parem execució si no s'ha trobat dni
        print()
        print(cashier.describe())

        # Mostrem els clients disponibles
        print("\n--- CLIENTS DISPONIBLES ---\n")
        for c in self.customers:
            print(c.describe())
        print()

        # Customer té 5 intents, si cap és correcte s'atura programa.
        attempts = 0
        customer = None

        while attempts < max_attempts:
            customer_dni = input("Introdueixi el DNI del client: ")
            customer = self.find_customer(customer_dni)
            if customer is not None:
                break
            print("DNI del client no trobat...")
            attempts += 1
        if customer is None:
            print("Massa intents. Reinicia el programa.")
            return  # Parem execució si no s'ha trobat dni
        print()
        print(customer.describe())

        # Instanciem la clase Order()
        order = Order(cashier, customer)

        # Mostrem llista de productes a vendre
        print("\n--- MENÚ DISPONIBLE ---\n")
        for p in self.products:
            print(p.describe())
        # Demanem i afegim productes a la comanda
        while True:
            product_id = input("\nIntrodueixi ID del producte: ").upper()
            product = self.find_product(product_id)
            if product is None:
                print("Producte no trobat...")
                continue
            print(f"\nAdded product: {product.describe()}")  # Mostrem descripcio producte.
            order.add(product)  # Afegim producte al order.
            # Preguntem si es volen afegir més productes.
            while True:
                seguir = input("Vols afegir un altre producte a la comanda? (Si/No): ").lower()
                if seguir in ("si", "no"):
                    break
                print("Resposta no vàlida: Introdueix (Si/No): ")
            if seguir == "no":
                break
        # Mostrem la comanda completa.
        order.show()

        data = [order.to_dict()]  # Creem dict
        df_export = pd.DataFrame(data)  # Guardem el DataFrame
        CSVFileManager("data/orders.csv").write(df_export)


if __name__ == "__main__":
    app = PrepareOrder()
    app.run()
