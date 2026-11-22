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


from abc import abstractmethod, ABC


class Account(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def _change_balance(self, amount):
        self.__balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

class DebitAccount(Account):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма должна быть больше нуля.")
        elif amount > self.get_balance():
            print("Недостаточно средств.")
        else:
            self._change_balance(-amount)
            print("Снятие успешно")


class CreditAccount(Account):
    def __init__(self, owner, balance, credit_limit):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма должна быть больше нуля.")
        elif amount <= self.get_balance() + self.credit_limit:
            self._change_balance(-amount)
            print("Снятие успешно")
        else:
            print("Нельзя превышать кредитный лимит.")


debit = DebitAccount("Ali", 1000)
credit = CreditAccount("Timur", 1000, 500)

accounts = [debit, credit]

for account in accounts:
    account.withdraw(1200)
    print(account.get_balance())