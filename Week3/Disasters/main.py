from ui import UI
from csv_reader import CsvReader

ui = UI(["1...List Disasters in Countries", "2...List Disasters in a Specific Interval",
         "3...List Disasters of Specified Type", "4...List Disasters on Specified Continents", "5...Quit"])

reader = CsvReader()
disasters = reader.read_csv_file("csv_files/1900_2021_DISASTERS.xlsx - emdat data.csv")


def list_disasters_in_specific_country():
    disasters_list = []
    while True:
        country = input("Enter a country (at least 3 characters): ").lower()
        if len(country) >= 3:
            disasters_in_specific_interval = list_disasters_in_specific_interval()
            for disaster in disasters_in_specific_interval:
                if country in disaster["Country"].lower():
                    disasters_list.append(disaster)
            break
        else:
            print("Please enter a country at least 3 characters.")
            continue
    return disasters_list


def list_disasters_in_specific_interval():
    disasters_in_specific_interval = []
    try:
        interval = input("Enter an interval (1900-2021): ")
        min_year = int(interval.split("-")[0])
        max_year = int(interval.split("-")[1])
        for disaster in disasters:
            if min_year <= int(disaster["Year"]) <= max_year:
                disasters_in_specific_interval.append(disaster)
    except ValueError:
        print("Invalid input. Please try again.")
    except TypeError:
        print("Invalid input. Please try again.")
    else:
        return disasters_in_specific_interval


def list_disasters_with_specific_type():
    disasters_with_specific_type = []
    type_of_disasters = input("Enter a type of disasters: ").lower()
    disasters_in_specific_interval = list_disasters_in_specific_interval()
    for disaster in disasters_in_specific_interval:
        if type_of_disasters in disaster["Disaster Type"].lower():
            disasters_with_specific_type.append(disaster)
    return disasters_with_specific_type


def list_disasters_with_specific_continent():
    disasters_with_specific_continent = []
    continent = input("Enter a continent: ").lower()
    disasters_in_specific_interval = list_disasters_in_specific_interval()
    for disaster in disasters_in_specific_interval:
        if continent in disaster["Continent"].lower():
            disasters_with_specific_continent.append(disaster)
    return disasters_with_specific_continent


def display_disasters(_disasters):
    try:
        for disaster in _disasters:
            print("*" * 50)
            print(f"Year: {disaster['Year']}\nType: {disaster['Disaster Type']}\nCountry: {disaster['Country']}\n"
                  f"Location: {disaster['Location']}\nMagnitude: {disaster['Dis Mag Value']} {disaster['Dis Mag Scale']}\n"
                  f"Datetime: {disaster['Local Time']} {disaster['Start Day']}.{disaster['Start Month']}."
                  f"{disaster['Start Year']}\nTotal Deaths: {disaster['Total Deaths']}")
    except:
        print("No disasters found.")


def menu():
    while True:
        choice = ui.create_menu()
        if choice == "1":
            display_disasters(list_disasters_in_specific_country())
        elif choice == "2":
            display_disasters(list_disasters_in_specific_interval())
        elif choice == "3":
            display_disasters(list_disasters_with_specific_type())
        elif choice == "4":
            display_disasters(list_disasters_with_specific_continent())
        elif choice == "5":
            print("Goodbye!")
            break


if __name__ == "__main__":
    menu()
