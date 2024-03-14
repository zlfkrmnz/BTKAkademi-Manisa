class Person:
    def __init__(self, id_number, name, surname, gender, age, phone_number, email, address):
        self.__id_number = id_number
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.__phone_number = phone_number
        self.__email = email
        self.__address = address

    def get_id_number(self):
        return self.__id_number

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_phone_number(self):
        return self

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_details(self):
        return f"""ID: {self.__id_number}
Name: {self.name}
Surname: {self.surname}
Gender: {self.gender}
Age: {self.age}
Phone Number: {self.__phone_number}
Email: {self.__email}
Address: {self.__address}
"""


class Vendor(Person):
    def __init__(self, id_number, name, surname, gender, age, phone_number, email, address, vendor_id):
        super().__init__(id_number, name, surname, gender, age, phone_number, email, address)
        self.__vendor_id = vendor_id

    def get_vendor_id(self):
        return self.__vendor_id

    def set_vendor_id(self, vendor_id):
        self.__vendor_id = vendor_id

    def get_details(self):
        return f"{super().get_details()}Vendor ID: {self.__vendor_id}"


class Customer(Person):
    def __init__(self, id_number, name, surname, gender, age, phone_number, email, address, customer_id):
        super().__init__(id_number, name, surname, gender, age, phone_number, email, address)
        self.__customer_id = customer_id

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_details(self):
        return f"{super().get_details()}Customer ID: {self.__customer_id}"
