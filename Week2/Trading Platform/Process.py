import Person
import Product
import os


def __write(text, file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(text)


def __read(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)


def add_person():
    print(create_menu(['1. Add a customer', '2. Add a vendor']))
    choice = input("Please choose a menu option: ")
    id_number = input("Enter person's identification number: ")
    name = input("Enter person's name: ")
    surname = input("Enter person's surname: ")
    gender = input("Enter person's gender: ")
    age = input("Enter person's age: ")
    phone_number = input("Enter person's phone number: ")
    email = input("Enter person's email: ")
    address = input("Enter person's address: ")
    if choice == "1":
        __add_customer(id_number, name, surname, gender, age, phone_number, email, address)
    if choice == "2":
        __add_vendor(id_number, name, surname, gender, age, phone_number, email, address)


def __add_vendor(id_number, name, surname, gender, age, phone_number, email, address):
    vendor_id = input("Enter vendor's id: ")
    vendor = Person.Vendor(id_number, name, surname, gender, age, phone_number, email, address, vendor_id)
    vendor_details = vendor.get_details() + "\n" + "-"*50 + "\n"
    __write(vendor_details, "Lists/person.txt")


def __add_customer(id_number, name, surname, gender, age, phone_number, email, address):
    customer_id = input("Enter customer's id: ")
    customer = Person.Customer(id_number, name, surname, gender, age, phone_number, email, address, customer_id)
    customer_details = customer.get_details() + "\n" + "-"*50 + "\n"
    __write(customer_details, "Lists/person.txt")


def list_persons():
    print("PERSONS".center(50, "-"))
    __read("Lists/person.txt")


def add_product():
    print(create_menu(['1. Add a fridge', '2. Add a oven']))
    choice = input("Please choose a menu option: ")
    product_id = input("Enter product's id: ")
    name = input("Enter product's name: ")
    price = input("Enter product's price: ")
    description = input("Enter product's description: ")
    brand = input("Enter product's brand: ")
    model = input("Enter product's model: ")
    if choice == "1":
        __add_fridge(product_id, name, price, description, brand, model)
    if choice == "2":
        __add_oven(product_id, name, price, description, brand, model)


def __add_fridge(product_id, name, price, description, brand, model):
    capacity = input("Enter fridge's capacity: ")
    energy_rating = input("Enter fridge's energy rating: ")
    has_freezer = input("Enter 'Yes', if fridge has freezer; else enter 'No': ")
    fridge = Product.Fridge(product_id, name, price, description, brand, model, capacity, energy_rating, has_freezer)
    fridge_details = fridge.get_details() + "-"*50
    __write(fridge_details, "Lists/product.txt")


def __add_oven(product_id, name, price, description, brand, model):
    volume = input("Enter oven's volume: ")
    has_self_cleaning = input("Enter 'Yes', if oven has self cleaning; else enter 'No': ")
    oven = Product.Oven(product_id, name, price, description, brand, model, volume, has_self_cleaning)
    oven_details = oven.get_details() + "-"*50
    __write(oven_details, "Lists/product.txt")


def list_products():
    print("PRODUCTS".center(50, "-"))
    __read("Lists/product.txt")


def make_sale():
    os.system("cls")
    list_products()
    product_id = input("Please enter product id for sale: ")
    os.system("cls")
    list_persons()
    vendor_id = input("Please enter vendor id for sale: ")
    customer_id = input("Please enter customer id for sale: ")
    sale = f"\nProduct: {product_id}\nVendor: {vendor_id}\nCustomer: {customer_id}\n" + "-"*50
    __write(sale, "Lists/sales.txt")


def list_sales():
    print("SALES".center(50, "-"))
    __read("Lists/sales.txt")


def line(text=""):
    if text == "":
        return "-" * 50
    else:
        return "|" + text.center(48, " ") + "|"


def create_menu(elements):
    text = line()
    for element in elements:
        text += f"\n{line(element)}"
    text += "\n" + line()
    return text


def menu():
    print("Welcome our project. Let's get started.")
    while True:
        print(line())
        print(line("MAIN MENU"))
        print(create_menu(['1. Person Processes', '2. Product Processes', '3. Sales Processes', '0. Quit']))
        option = input("Please choose a menu option: ")
        if option == "1":
            print(create_menu(['1. Add Person', '2. List Persons']))
            while True:
                option = input("Please choose a menu option: ")
                if option == "1":
                    add_person()
                    print("Person added successfully. Transferring to main menu.")
                    break
                elif option == "2":
                    list_persons()
                    break
                else:
                    print("Invalid entry. Please try again.")
        elif option == "2":
            print("1. Add Product\n2. List Products\n")
            while True:
                option = input("Please choose a menu option: ")
                if option == '1':
                    add_product()
                    break
                elif option == "2":
                    list_products()
                    break
                else:
                    print("Invalid entry. Please try again.")
        elif option == "3":
            print("1. Add Sale\n2. List Sales")
            while True:
                option = input("Please choose a menu option: ")
                if option == '1':
                    make_sale()
                    break
                elif option == "2":
                    list_sales()
                    break
                else:
                    print("invalid entry. Please try again.")
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid entry. Please try again.")


if __name__ == "__main__":
    menu()
