# 2
# num = int(input("Введите число: "))
#
# if num > 0:
#     print("Положительное")
#
# elif num < 0:
#     print("Отрицательное")
#
# else:
#     print("Ноль")

# num = int(input("Введите число: "))
# num = [num]
# res = ["Положтельное" if i > 0 else "Отрисательное" if i < 0 else "Ноль" for i in num]
# print(res)


# 3
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a == b or a == c:
#     print("a is equal to b")
# elif a == b and a == c:
#     print("a")
# elif a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)


# 4
# a = []
# for i in range(1, 6):
#     num = int(input("Введите оценки: "))
#     a.append(num)
#
#
# b =0
# for i in a:
#     b += i
#
# if b >=90:
#     print("Отлично")
# elif 75 <= b <= 89:
#     print("хорошо")
# elif 60 <= b <= 74:
#     print("Удовлетворительно")
# else:
#     print("Повторить")


# 5
# num = int(input("Введите число: "))
# a = 0
# for i in range(1, num + 1):
#     a += i
# print(a)


# 6
# num = int(input("Введите число: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# 7
# num = int(input("Введите число: "))
# a = 0
# for i in range(1, num + 1):
#     a += 1
# print(a)

# 8
# text = input("Введите текст: ")
# print(text[::-1])

# 9
# a = []
# for i in range(1, 11):
#     user_num = int(input("Введите число: "))
#     a.append(user_num)
#
# b = 0
# c = 0
# summ = 0
# for res in a:
#     if res % 2 == 0:
#         summ += res
#         b += 1
#         print(f"Количество четных чисел: {b}")
#     elif res % 2 == 1:
#         c += 1
#         print(f"Количество нечетных чисел: {c}")
# print(f"Сумма четных чисел: {summ}")


# 10
# num = [1,2,2,3,44,5,6,77,8,9,9]
# n = []
# for i in num:
#     if i not in n:
#         n.append(i)
# print(n)


# 11

# user = int(input("Введите число: "))
#
# if user > 1:
#     for i in range(2, user):
#         if user % i == 0:
#             print(f"Число составное {user}")
#             break
#     else:
#         print("Простое")
# else:
#     print("Число должен быть больше 1")


# 12

# user = int(input("Введите число: "))
#
# res = 1
# while user > 0:
#     ot = user % 10
#     res *= ot
#     user //= 10
# print(res)


# 13
# num = int(input("Введите число: "))
# orig = num
# res =0
#
# while num > 0:
#     o = num % 10
#     res = res * 10 + o
#     num //= 10
#
# if res == orig:
#     print("Полидром")
# else:
#     print("Не полидром")


# num = []
# for i in range(1, 11):
#     user_num = int(input("Введите число: "))
#     num.append(user_num)
#
# a = num[0]
# b = num[0]
#
# for i in num:
#     if i > a:
#         a = i
#     if i < b:
#         b = i
#
# print(f"мах: {a}")
# print(f"min: {b}")
#
# c = 0
# for i in num:
#     c += i
# print(f"Сумма: {c}")
#
# x = 0
# for i in num:
#     if i % 2 == 0:
#         x += 1
# print(f"кол четных чисел: {x}")

# numbers = []
# for i in range(1, 11):
#     user_num = int(input("Введите число: "))
#     numbers.append(user_num)
#
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(f"уникальные числа: {unique}")
# print(f"Количество: {len(unique)}")


# text = input("Введите предложение: ")
#
# text = text.lower()
#
# for symbol in ".,!?":
#     text = text.replace(symbol, "")
#
# words = text.split()
#
# print("Количество слов:", len(words))
#
# longest_word = words[0]
#
# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word
#
# print("Самое длинное слово:", longest_word)


# numbers = [2, 5, 2, 8, 5, 2, 9, 8, 5, 1]
#
# dic ={}
# for number in numbers:
#     if number in dic:
#         dic[number] += 1
#     else:
#         dic[number] = 1
# print(dic)


# def analyze_numbers(numbers):
#     # numbers = [10, 3, 20, 5, 7]
#     maximum = numbers[0]
#     minimum = numbers[0]
#     total = 0
#     even = 0
#     odd = 0
#
#     for num in numbers:
#         if num > maximum:
#             maximum = num
#         if num < minimum:
#             minimum = num
#     for num2 in numbers:
#         if num2 % 2 == 0:
#             even = even + 1
#         else:
#             odd = odd + 1
#     for num3 in numbers:
#         total += num3
#
#     result = {
#         "max": maximum,
#         "min": minimum,
#         "sum": total,
#         "even": even,
#         "odd": odd
#     }
#
#     return result
# print(analyze_numbers([10, 3, 20, 5, 7]))


# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# name = input("Name: ")
# age = int(input("Age: "))
# language = input("Language: ")
# level = input("Level: ")
# student_info(name=name, age=age, language=language, level=level)


# def calculate(*args):
#     maximum = args[0]
#     minimum = args[0]
#     summ = 0
#     for i in args:
#         if i > maximum:
#             maximum = i
#         if i < minimum:
#             minimum = i
#         summ += i
#     res = {
#         "sum": summ,
#         "maximum": maximum,
#         "minimum": minimum
#     }
#     return res
# print(calculate(1, 2, 3, 4, 5))

# def user_profile(*args, **kwargs):
#     print("Иноформация о пользователе:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#     print("Языки программирования:")
#     for i in args:
#         print(f"{i}")
#
#
# name = input("Name: ")
# age = int(input("Age: "))
# level = input("Level: ")
# user_profile(
#     "Python",
#     "Java",
#     "C++",
#     name=name,
#     age=age,
#     level=level
# )


# numbers = [4, 15, 8, 23, 10, 7, 18, 3, 12, 25]
# numbers = filter(lambda x: x > 10, numbers)
# res = list(map(lambda x: x**2, numbers))
# print(res)

# names = ["Ali", "Timur", "Idiris", "Azamat"]
#
# ages = [18, 21, 20, 19]
# res = dict(zip(names, ages))
# print(res)


# products = ["Ноутбук", "Телефон", "Наушники", "Мышь", "Монитор"]
# for index, product in enumerate(products, start=1):
#     print(f"{index}. {product}")


# students = [
#     ("Ali", 85),
#     ("Timur", 92),
#     ("Idiris", 78),
#     ("Azamat", 95),
#     ("Nursultan", 88)
# ]
# print(sorted(students, key=lambda x: x[1], reverse=True))



# numbers = [12, 18, 24, 30, 36]
# res = all(map(lambda n: n > 0, numbers))
# res2 = any(map(lambda n: n > 30, numbers))
# print(f"Все числа положительные: {res}")
# print(f"Есть число больше 30: {res2}")

#
# data = [10, "Python", 3.14, True, [1, 2, 3], (4, 5), {"name": "Ali"}]
# int_count = 0
# str_count = 0
# float_count = 0
# list_count = 0
# tuple_count = 0
# dict_count = 0
#
# for item in data:
#     if isinstance(item, bool):
#         continue
#     elif isinstance(item, int):
#         int_count += 1
#     elif isinstance(item, float):
#         float_count += 1
#     elif isinstance(item, str):
#         str_count += 1
#     elif isinstance(item, tuple):
#         tuple_count += 1
#     elif isinstance(item, dict):
#         dict_count += 1
#     elif isinstance(item, list):
#         list_count += 1
# print("int:", int_count)
# print("str:", str_count)
# print("float:", float_count)
# print("list:", list_count)
# print("tuple:", tuple_count)
# print("dict:", dict_count)






# num1 = int(input('Введите первое число: '))
# operator = input('Выберите оператора (+: -: *: /): ')
# num2 = int(input('Введите второе число: '))
#
# if operator == "+":
#     summ = num1 + num2
#     print(f'{num1} + {num2} = {sum}')
# elif operator == '-':
#     summ = num1 - num2
#     print(f'{num1} - {num2} = {summ}')
# elif operator == '*':
#     summ = num1 * num2
#     print(f"{num1} * {num2} = {summ}")
# elif operator == '/':
#     summ = num1 / num2
#     print(f"{num1} / {num2} = {summ}")



# while True:
#     print("Калкулятор")
#     print("1) плюс")
#     print("2) минус")
#     print("3) умножение")
#     print("4) деление")
#     print("5) выход")
#
#     user_num = int(input("Выберите действие: "))
#     if user_num == 1:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         summ = num1 + num2
#         print(f"вывод: {summ}")
#     elif user_num == 2:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         summ = num1 - num2
#         print(f"вывод: {summ}")
#     elif user_num == 3:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         summ = num1 * num2
#         print(f"вывод: {summ}")
#     elif user_num == 4:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         summ = num1 / num2
#         print(f"вывод: {summ}")
#     elif user_num == 5:
#         print("Выход из калкулятора")
#         break
#     else:
#         print("Такого оператора нету")
#         continue





