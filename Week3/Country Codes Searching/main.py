from json_reader import JsonReader
from ui import UI

ui = UI(['1...Get Country Information', '2...Find Country by Phone Code', '3...Count Countries on the Continent', '4...Find Country by Currency', '5...Quit'])
reader = JsonReader()
phones = reader.read_json_file("json_files/phone.json")
names = reader.read_json_file("json_files/names.json")
continents = reader.read_json_file("json_files/continent.json")
currencies = reader.read_json_file("json_files/currency.json")
iso3s = reader.read_json_file("json_files/iso3.json")


def get_country_information():
    while True:
        val = input("Please enter several letters for the country (at least three letters): ").lower()
        countries = []
        if len(val) >= 3:
            for key, value in names.items():
                if val in value.lower():
                    countries.append(f"*** Country Name: {names.get(value)}, Abbreviation: {names.get(key)}, Phone Code: {phones.get(key)}, Continent: {continents.get(key)}, Currency Unit: {currencies.get(key)}, ISO3: {iso3s.get(key)}")
            if len(countries) > 0:
                for value in countries:
                    print(value)
            else:
                print("No country was found.")
            break
        else:
            print("Please enter at least 3 letters.")


def find_country_from_phone_code():
    val = input("Please enter a phone code: ").lower()
    countries = []
    for key, value in phones.items():
        if value.lower() == val:
            countries.append(names.get(key))
    if len(countries) > 0:
        for value in countries:
            print(value)
    else:
        print("No value was found.")


def continent_number():
    count = 0
    val = input("Please enter a continent code: ").lower()
    for value in continents.values():
        if value.lower == val:
            count += 1
    print(f"{count} country/countries found.")


def find_country_from_money_unit():
    val = input("Please enter a currency: ").lower()
    countries = []
    for key, value in currencies.items():
        if value.lower == val:
            countries.append(names.get(key))
    if len(countries) > 0:
        for value in countries:
            print(value)
    else:
        print("No value was found.")


def menu():
    print("Welcome our project. Let's get started.")
    while True:
        option = ui.create_menu()
        if option == "1":
            get_country_information()
        elif option == "2":
            find_country_from_phone_code()
        elif option == "3":
            continent_number()
        elif option == "4":
            find_country_from_money_unit()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Please enter a valid value.")


if __name__ == "__main__":
    menu()
