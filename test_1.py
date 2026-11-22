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




