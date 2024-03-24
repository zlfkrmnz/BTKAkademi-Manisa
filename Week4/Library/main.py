import re
from datetime import datetime
from library import Library
from ui import UI


def menu(menu_items):
    ui = UI(menu_items)
    option = ui.create_menu()
    return option


def make_process():
    library = Library()
    while True:
        option = menu(["Kitap Ekle", "Kitap Ara", "Kitap Listele", "Kitap Sil", "Kitap Ödünç Al", "Kitap Geri Ver",
                       "Veritabanını Yedekle", "Yedeği Geri Yükle", "Çıkış"])
        if option == "1":
            isbn = input("ISBN: ")
            while not check_isbn(isbn):
                isbn = input("Lütfen ISBN'i 13 rakam olacak şekilde giriniz.\nISBN: ")
            title = input("Kitap Adı: ")
            author = input("Yazar: ")
            p_date = input("Yayın Tarihi (dd.mm.yyyy): ")
            while not check_date(p_date):
                p_date = input("Lütfen tarih formatını doğru bir şekilde giriniz.\nYayın Tarihi (dd.mm.yyyy): ")
            genre = input("Genre: ")
            summary = input("Summary: ")
            library.add_book(int(isbn), title, author, p_date, genre, summary)
        elif option == "2":
            while True:
                option = int(menu(["ISBN ile ara", "Kitap Adı ile ara", "Yazar Adı ile ara", "Üst menüye dön."]))
                if option in range(1, 4):
                    text = input("Search: ")
                    results = library.search_book(str(option), text)
                    if results is not None:
                        print(" BULUNAN KİTAPLAR ".center(174, "*"))
                        for no, value in enumerate(results):
                            print(f"Kitap No: {no + 1}")
                            print(
                                f"ISBN: {value[0]}\nKitap Adı: {value[1]}\nYazar: {value[2]}\nYayın Tarihi: {value[3]}"
                                f"\nTür: {value[4]}\nÖzet: {value[5]}\nKitap Kütüphanede mi?: {'Evet' if (value[6] == 'true') else 'Hayır'}")
                            print("*" * 174)
                    else:
                        print("Lütfen geçerli bir değer giriniz.")
                        continue
                elif option == 4:
                    break
                else:
                    print("Lütfen geçerli bir seçenek giriniz.")
        elif option == "3":
            library.list_book()
        elif option == "4":
            library.delete('books')
        elif option == "5":
            library.borrow_book()
        elif option == "6":
            library.return_book()
        elif option == "7":
            library.backup()
        elif option == "8":
            library.recovery()
        elif option == "9":
            print("Güle güle.")
            del library
            break
        else:
            print("Lütfen geçerli bir seçenek giriniz.")


def check_isbn(isbn):
    pattern = re.compile(r"^\d{13}$")
    if pattern.match(isbn):
        return True
    else:
        return False


def check_date(p_date):
    pattern = "%d.%m.%Y"
    try:
        result = bool(datetime.strptime(p_date, pattern))
    except ValueError:
        result = False
    return result


if __name__ == "__main__":
    make_process()
