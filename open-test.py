import csv
import os
import locale


products = []           #lista

def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    products_list = []  # Lokal lista istället för global variabel
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products_list.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products_list  # Returnera listan istället för att ha en global variabel
   


#TODO: hur gör man så funktionen load_data returnerar products istället?
def display_products_numbered(products_list):
    print("\nPRODUKTLISTA")
    for i, product in enumerate(products_list, 1):
        print(f"{i}. {product['name']} - {(product['price'])}")
        print(f"   Beskrivning: {product['desc']}")
        print(f"   Antal i lager: {product['quantity']}")
        print()

def get_product_by_id(products_list, product_id):
    for product in products_list:
        if product['id'] == product_id:
            return product

#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')

os.system('cls')

# Visa produkterna i en numrerad lista
display_products_numbered(products)

# Här så hämtar jag en specifik produkt med id, i detta fall id 1. jag behöver bara se till att det är mellan 0-10)
product = get_product_by_id(products, 10)
if product:
    print(f"Hittade produkt: {product['name']}")
else:
    print("Produkten hittades inte")
    




