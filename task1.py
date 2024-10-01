import requests

def get_products_price_20():
    products = requests.get("https://fakestoreapi.com/products").json()
    sorted_products = [x for x in products if x.get("price") < 20]
    print(sorted_products)


def get_all_categories():
    categories = requests.get("https://fakestoreapi.com/products/categories").json()
    print(categories)


def get_jewelery_products():
    products = requests.get("https://fakestoreapi.com/products/category/jewelery").json()
    print(products)


def get_all_users():
    users = requests.get("https://fakestoreapi.com/users").json()
    print(users)


def add_my_user():
    data = {
        'username': 'daniilTerentev',
        'name': {
            "fistname": "Daniil",
            "lastname": "Terentev"
        }
    }
    response = requests.post("https://fakestoreapi.com/users", data=data)
    print(response.json())


get_products_price_20()
get_all_categories()
get_jewelery_products()
get_all_users()
add_my_user()