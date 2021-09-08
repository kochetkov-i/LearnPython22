from pprint import pprint


#
#examples
#

product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1
}

print(f"count of elements: {len(product)}")

product["memory"] = 64

print(f"product: {product}")

product["name"] = "iPhone 12 Pro"

print(f"product: {product}")
print(f"product price: {product['price']}")
print(f"product stock: {product['stock']}")
print(f"product name: {product.get('name')}")
print(f"product discount: {product.get('discount')}")

print(f"product discount: {product.get('discount', 0)}")
print(f"product country: {product.get('country', 'CN')}")

del product["stock"]
print(f"product: {product}")

try:
    del product["stock"]
except KeyError as e:
    print(f"{e} - {e.__doc__}")

phones = ["Samsung Galaxy S21", "iPhone 12"]
product["recomended"] = phones
pprint(f"{product}")

print(f"recomended products: {product['recomended']}")
product["recomended"].append("Nokia 3310")
print(f"count of recomended products: {len(product['recomended'])}")
print(f"first recomended product: {product['recomended'][0]}")

stock = [
    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
       'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
]

print(f"third stock element: {stock[2]}")
stock[2]["price"] = stock[2]["price"] - 8000
print(f"third stock element price: {stock[2]['price']}")
print(f"second recomended in first stock: {stock[0]['recomended'][1]}")

print(f"type of stock: {type(stock)}")
print(f"type of stock element: {type(stock[0])}")

#
# Tasks
#

wether = {"city": "Moscow", "temperature": "20"}
print(f"city: {wether['city']}")
wether["temperature"] = str(int(wether["temperature"])-5)
print(f"wether in cities: {wether}")

print(f"check key: {wether.get('country')}")
print(f"check key and set default: {wether.get('country', 'Russia')}")
wether["date"] = "27.05.2021"
print(f"count of dict elements: {len(wether)}")
