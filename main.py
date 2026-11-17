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


#13
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


user_text = input("Введите текст: ").lower()


