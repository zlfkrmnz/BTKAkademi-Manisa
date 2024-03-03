"""
In this project, there is a program that reads the 1000 movies with the highest imdb score from the csv file,
translates it into a dictionary structure and performs search operations.
"""

import csv


def search(films, search_term, key):
    movies = []
    for film in films:
        if search_term.lower() in film[key].lower():
            movies.append(film)
            print(f"---------------------\nDirector: {film['Director']}\nTitle: {film['Series_Title']}\nIMDB Rating: {film['IMDB_Rating']}\nGenre: {film['Genre']}")
    if len(movies) == 0:
        print("No movies matching the value you entered were found.")
    return movies


def search_imdb(films):
    movies = []
    val1 = float(input("Please enter the big IMDB rating: "))
    val2 = float(input("Please enter the small IMDB rating: "))
    for film in films:
        if val1 >= float(film['IMDB_Rating']) >= val2:
            movies.append(film)
            print(f"---------------------\nDirector: {film['Director']}\nTitle: {film['Series_Title']}\nIMDB Rating: {film['IMDB_Rating']}\nGenre: {film['Genre']}")
    if len(movies) == 0:
        print("No movies matching the value you entered were found.")
    return movies


def search_actor(films):
    search_term = input("Insert a word that appears in the names of the movie stars: ")
    movies = []
    for film in films:
        if search_term.lower() in film['Star1'].lower() or search_term.lower() in film['Star2'] or search_term.lower() in film['Star3'] or search_term.lower() in film['Star4']:
            movies.append(film)
            print(f"---------------------\nDirector: {film['Director']}\nTitle: {film['Series_Title']}\nIMDB Rating: {film['IMDB_Rating']}\nGenre: {film['Genre']}\n{film['Star1']},{film['Star2']},{film['Star3']},{film['Star4']}")
    if len(movies) == 0:
        print("No movies matching the value you entered were found.")

    return movies


def menu(data):
    print("""
 ---------------------
|******* MENU ********|
 ---------------------
| 1...Search Movie    |
| 2...Search Director |
| 3...Search IMDB     |
| 4...Search Genre    |
| 5...Search Star     |
| 6...Quit            |
 ---------------------
""")
    choice = input("Please enter your selection: ")
    if choice == "1":
        search_term = input("Please enter the word you want to search for: ")
        search(data, search_term, 'Series_Title')
        return True
    elif choice == "2":
        search_term = input("Please enter the word you want to search for: ")
        search(data, search_term, 'Director')
        return True
    elif choice == "3":
        search_imdb(data)
        return True
    elif choice == "4":
        search_term = input("Please enter the word you want to search for: ")
        search(data, search_term, 'Genre')
        return True
    elif choice == "5":
        search_actor(data)
        return True
    elif choice == "6":
        print("Thank you for choosing us. (:")
        return False
    else:
        print("Please enter a correct value.")
        return True


def main():
    with open('imdb_top_1000.csv', 'r', encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    while menu(data):
        continue


if __name__ == '__main__':
    main()
