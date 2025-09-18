import csv
import os
import locale




def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    products = []
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products
   


def numererad_lista(products):
    for i, product in enumerate(products, 1):
        print(f"{i}. {product['name']} - {format_currency(product['price'])} - {product['quantity']} st")


def get_product_by_id(products, products_id):
    for product in products:
        if product["id"] == products_id:
            return print(f"Produkt: {product['name']} Beskrivning: {product['desc']} Pris: {product['price']} Antal i lager: {product['quantity']} st")
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id

os.system('cls')
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')
    
numererad_lista(products)

get_product_by_id(products, int(input("Ange produktens id: ")))


