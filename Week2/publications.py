class Publications():
    def __init__(self, isbn, publication_name, publication_date):
        self.__isbn = isbn
        self.publication_name = publication_name
        self.publication_date = publication_date

    def print(self):
        print(f"ISBN: {self.get_isbn()}\nPublication Name: {self.publication_name}\nPublication Date: {self.publication_date}")

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn


class Books(Publications):
    def __init__(self, isbn, publication_name, publication_date, author, publisher, b_bookshelf):
        super().__init__(isbn, publication_name, publication_date)
        self.author = author
        self.publisher = publisher
        self.__b_bookshelf = b_bookshelf

    def print_b(self):
        print(f"ISBN: {self.get_isbn()}\nPublication Name: {self.publication_name}\nPublication Date: {self.publication_date}"
              f"\nAuthor: {self.author}\nPublisher: {self.publisher}\nBookshelf: {self.get_bookshelf()}")

    def get_bookshelf(self):
        return self.__b_bookshelf

    def set_bookshelf(self, b_bookshelf):
        self.__b_bookshelf = b_bookshelf


class Periodicals(Publications):
    def __init__(self, isbn, publication_name, publication_date, domain, number, p_bookshelf):
        super().__init__(isbn, publication_name, publication_date)
        self.domain = domain
        self.number = number
        self.__p_bookshelf = p_bookshelf

    def print_p(self):
        print(f"ISBN: {self.get_isbn()}\nPublication Name: {self.publication_name}\nPublication Date: {self.publication_date}"
              f"\nDomain: {self.domain}\nNumber: {self.number}\nBookshelf: {self.__p_bookshelf}")

    def get_bookshelf(self):
        return self.__p_bookshelf

    def set_bookshelf(self, p_bookshelf):
        self.__p_bookshelf = p_bookshelf


if __name__ == "__main__":
    book = Books("9786053600138", "Beyaz Diş", "2010", "Jack London", "İş Bankası Kültür Yayınları", "KJ11")
    book.print_b()

    print("-" * 20)

    book.set_isbn("9786053600139")
    book.set_bookshelf("KJ12")
    book.print_b()

    print("-"*20)

    periodical = Periodicals("2717-736X", "19 Mayıs Sosyal Bilimler Dergisi", "2023", "Sosyal Bilimler", "4", "D111")
    periodical.print_p()

    print("-" * 20)

    periodical.set_isbn("2717-736X")
    periodical.set_bookshelf("DP11")
    periodical.print_p()
