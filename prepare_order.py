"""
Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación 
que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. 
La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad 
de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para 
finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
from util import CSVFileManager, CashierConverter, CustomerConverter, ProductConverter
from orders import Order
from users import Cashier, Customer
from products import Product


class PrepareOrder:

    def __init__(self):
        self.cashiers = []
        self.customers = []
        self.products = []

    def load_data(self):
        #DataFrame + convert Cashiers
        df_cashiers = CSVFileManager("data/cashiers.csv").read()
        self.cashiers = CashierConverter().convert(df_cashiers)

        #Dataframe + convert Customers
        df_customers = CSVFileManager("data/customers.csv").read()
        self.customers = CustomerConverter().convert(df_customers)

        #Dataframe + converts products/hamburgers
        df_hamburgers = CSVFileManager("data/hamburgers.csv").read()
        hamburgers = ProductConverter().convert(df_hamburgers, "Hamburger")
       
        #Dataframe + converts products/sodas
        df_sodas = CSVFileManager("data/sodas.csv").read()
        sodas = ProductConverter().convert(df_sodas, "Soda")
        
        #Dataframe + converts products/drinks
        df_drinks = CSVFileManager("data/drinks.csv").read()
        drinks = ProductConverter().convert(df_drinks, "Drink")
        
        #Dataframe + converts products/happymeals
        df_happymeals = CSVFileManager("data/happyMeal.csv").read()
        happymeals = ProductConverter().convert(df_happymeals, "HappyMeal")
        
        #Unim els products en una mateixa llista
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
        self.load_data()

        cashier_dni = input("Introdueixi el DNI del caixer:")
        cashier = self.find_cashier(cashier_dni)
        if cashier is None:
            print("DNI no trobat...")
            return
        
        customer_dni = input("Introdueixi el DNI del client:")
        customer = self.find_customer(customer_dni)
        if customer is None:
            print("Client no trobat")
            return
        