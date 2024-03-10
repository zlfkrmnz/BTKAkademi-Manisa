class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name


class Employee(Person):

    def __init__(self, name, surname, employee_id, salary):
        super().__init__(name, surname)
        self.employee_id = employee_id
        self.__salary = salary

    def set_salary(self, salary):
        if self.__class__ == Employee:
            print(f"{self.name} {self.surname}'s salary set as {salary}$.")
        else:
            print("You have no authority.")

    def get_employee_info(self):
        print(f"Employee ID: {self.employee_id}\nName: {self.name}\nSurname: {self.surname}\nSalary: {self.__salary}")


class Manager(Employee):
    connected_employees = {}

    def __init__(self, name, surname, employee_id, department, salary):
        super().__init__(name, surname, employee_id, salary)
        self.department = department

    def add_connected_employees(self, connected_employees):
        for connected_employee in connected_employees:
            if connected_employee.employee_id not in self.connected_employees:
                self.connected_employees[connected_employee.employee_id] = connected_employee
                print(
                    f"{connected_employee.name} {connected_employee.surname} is connected to {self.name} {self.surname}")
            else:
                print(
                    f"{connected_employee.name} {connected_employee.surname} is already connected to {self.name} {self.surname}")

    def get_connected_employees(self):
        for connected_employee in self.connected_employees.values():
            print(f"{connected_employee.employee_id} - {connected_employee.name} {connected_employee.surname}")


if __name__ == "__main__":
    employee1 = Employee("Ozan", "Alptekin", 101, 30000)

    employee2 = Employee("Toprak", "Alptekin", 102, 40000)

    manager = Manager("Ahmet", "Mehmet", 201, "Software", 75000)
    manager.add_connected_employees([employee1])
    manager.add_connected_employees([employee2])
    manager.set_salary(100000)
