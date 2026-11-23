# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#         print(f"Меня зовут {name} Мне {age} лет")
#
#
# tes = Person("Idiris", 23)
# tes2 = Person("Idiri", 20)


# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Попелнение успешно: {amount}")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print("Снятие успешно")
#
#
# account = BankAccount(1000)
#
# account.deposit(500)
# account.withdraw(200)
#
# print(account.get_balance())


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print("Животное лает")
#
# class Dog(Animal):
#     def bark(self):
#         print("Собака лает")
#
#
# dog = Dog("Ш")
# dog.eat()
# dog.bark()


# class Dog:
#     def sound(self):
#         print("Гав")
#
# class Cat:
#     def sound(self):
#         print("Мяу")
#
# class Cow:
#     def sound(self):
#         print("Муу")
#
#
# animals = [Dog(), Cat(), Cow()]
#
# for animal in animals:
#     animal.sound()


# from abc import abstractmethod, ABC
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# res = Circle(5)
# res2 = Rectangle(5, 5)
# print(res.area())
# print(res2.area())


# from abc import abstractmethod, ABC
#
#
# class Account(ABC):
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#
#     def _change_balance(self, amount):
#         self.__balance += amount
#
#     @abstractmethod
#     def withdraw(self, amount):
#         pass
#
# class DebitAccount(Account):
#     def __init__(self, owner, balance):
#         super().__init__(owner, balance)
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Сумма должна быть больше нуля.")
#         elif amount > self.get_balance():
#             print("Недостаточно средств.")
#         else:
#             self._change_balance(-amount)
#             print("Снятие успешно")
#
#
# class CreditAccount(Account):
#     def __init__(self, owner, balance, credit_limit):
#         super().__init__(owner, balance)
#         self.credit_limit = credit_limit
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Сумма должна быть больше нуля.")
#         elif amount <= self.get_balance() + self.credit_limit:
#             self._change_balance(-amount)
#             print("Снятие успешно")
#         else:
#             print("Нельзя превышать кредитный лимит.")
#
#
# debit = DebitAccount("Ali", 1000)
# credit = CreditAccount("Timur", 1000, 500)
#
# accounts = [debit, credit]
#
# for account in accounts:
#     account.withdraw(1200)
#     print(account.get_balance())


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def get_info(self):
#         return f"Марка: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.year}"
#
#
#         # print(f"Марка: {"Toyota"}\nМодель: {"Camry"}\n Год выпуска: {2020}")
#
# car1 = Car("BMW", "M5", 2020)
# car2 = Car("Toyota", "Camry", 2020)
# print(car1.get_info())
# print(car2.get_info())


# class BankAccount:
#     def __init__(self, amount, balance):
#         self.amount = amount
#         self.__balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"пополнение счёта")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             print(f"снятие денег: {amount}")
#
#
#     def get_balance(self):
#         return self.__balance
#
#
# account = BankAccount("Idiris", 1000)
#
# account.deposit(500)
# account.withdraw(300)
#
# print(account.get_balance())


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grades):
#         if 1 <= grades <= 5:
#             self.grades.append(grades)
#
#     def get_average(self):
#         if not self.grades:
#             print("Список пуст")
#         else:
#             result = sum(self.grades) / len(self.grades)
#             return result
#
#
#
#     def get_info(self):
#         return f"Имя: {self.name}\nСредняя оценка: {self.get_average()}"
#
#
# student = Student("Idiris")
#
# student.add_grade(5)
# student.add_grade(4)
# student.add_grade(5)
# student.add_grade(3)
#
# print(student.get_info())


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if self.books not in sel:
            return 0

        elif len(book) > 0:
            return self.books.append(book)


    def remove_book(self, book):
        if book in self.books:
            return self.books.remove(book)
        else:
            return f"Такой книги нет"

    def show_books(self):
        return self.books


    def search_book(self, book):
        return book in self.books

library = Library("Central Library")

library.add_book("Python")
library.add_book("Java")
library.add_book("C++")

library.remove_book("Java")

library.show_books()
library.search_book("Python")
