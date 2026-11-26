# 1 задание
# a = 1
# while a <= 10:
#     print(a)
#     a = a + 1

# 2 задание
# a = 10
# while a > 0:
#     print(a)
#     a = a - 1

# 3 задание
# a = 1
# while a <= 30:
#     if a % 2 == 0:
#         print(a)
#     a += 1


# 4 задание
# a = 1
# while a <= 30:
#     if a % 2 == 1:
#         print(a)
#     a += 1


# 5 задание
# a = 1
# while a <= 50:
#     if a % 5 == 0:
#         print(a)
#     a = a + 1


# 6 задание
# a = 1
# b = 0
# while a <= 50:
#     b += a
#     a += 1
# print(b)


# 7 задание
# a = 1
# b = 0
# while a <= 50:
#     if a % 2 == 0:
#         b += a
#     a += 1
#
# print(b)


# 8 задание
# a = 1
# b = 0
# while a <= 50:
#     if a % 2 == 1:
#         b += a
#     a += 1
#
# print(b)

# 8 задание
# a = 1
# while a <= 10:
#    print(a ** 2)
#    a += 1


# 9 задание
# a = 1
# n = int(input("Введите число: "))
# while a <= n:
#     print(a)
#     a += 1

# 10 задание
# a = 1
# b = 0
# n = int(input("Введите чмсло: "))
# while a <= n:
#     b += a
#     a += 1
# print(b)

# 11 задание
# while True:
#     a = int(input("Введите число: "))
#     if a == 0:
#         print("Цикл остановлен")
#         break
#     else:
#         continue
# print(a)

# 12 задание
# while True:
#     a = int(input("Введите чмсло: "))
#     if a < 0:
#         print("Цикл остановлен")
#         break
#     else:
#         continue
# print(a)

# 13 задание
# while True:
#     password = input("Введите пароль: ")
#     if password == "python123":
#         print("Пароль правильный")
#         break
#     else:
#         print("Неправильный пароль")
#         continue

# 14 задание
# while True:
#     a = int(input("Введите число: "))
#     if 1 <= a <= 10:
#         print("Цикл остановлен")
#         break
#     else:
#         continue

# 15 задание
# a = 0
# b = 0
# while a < 5:
#     n = int(input("Введите число: "))
#     b += n
#     a += 1
# print("Сумма: ",b)

# 16 задание
# a = 0
# b = 0
# while True:
#     count = int(input("Введите число: "))
#     if count == 0:
#         print("Цикл остановлен")
#         break
#     b +=count
#     a +=1
# print("Сумма: ", b)

# 17 задание
# a = 0
#
# while True:
#     nom = int(input("Введите число: "))
#     if nom != 0:
#         if nom % 2 == 0:
#             a += 1
#     print("Сумма всех введенных чисел: ", a)
#     print("Введите 0 чтоб закончить цикл")

# 18 задание
# a = 0
# print("Для окончание 0")
# while True:
#     number = int(input("Вводите числа: "))
#     if number == 0:
#         break
#     elif number > 0:
#         a += 1
#     print("Для окончание 0")
# print("Сумма положительных чисел: ", a)

# 19 задание
# num = 1
# number = int(input("Введите число: "))
# while number <= 10:
#     print(f"{number} * {num} = {number * num}")
#     num += 1
#     if num == 11:
#         break


# 20 задание
# while True:
#     number = int(input("Ваше число: "))
#     if number == 7:
#         print("Число угадано")
#         break
#     else:
#         print("Пока не угадал правильное")
#         continue

# a = []
# total = 0
# for i in range(1, 6):
#     user = int(input("Введите число: "))
#     a.append(user)
#
# for i in a:
#     if i % 2 == 0:
#         total += i
#         print(i)
#
# print(total)


# numbers = [4, 7, 2, 9, 6]
# a = []
#
# for num in numbers:
#     if num % 2 == 0:
#         a += [num]
# print(f"Четные числа: {a}")
# print(f"Сумма: {sum(a)}")


# a = []
# b = []
# v = []
# for i in range(1, 9):
#     user = int(input("Введите число: "))
#     if user > 0:
#         a.append(user)
#     elif user < 0:
#         b.append(user)
#     else:
#         v.append(user)
# print(len(f"Положительные числа: {len(a)}"))
# print(len(f"Отрицательные числа: {len(b)}"))
# print(len(f"Нули: {len(v)}"))

# ===== МЕНЕДЖЕР РАСХОДОВ =====
#
# 1. Добавить расход
# 2. Показать все расходы
# 3. Найти расход
# 4. Показать общую сумму
# 5. Статистика по категориям
# 6. Удалить расход
# 7. Сохранить данные
# 8. Выход
def expense_manager():
    list_consumption = []
    while True:
        print("===== МЕНЕДЖЕР РАСХОДОВ =====")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Найти расход")
        print("4. Показать общую сумму")
        print("5. Статистика по категориям")
        print("6. Удалить расход")
        print("7. Сохранить данные")
        print("8. Выход")
        user_num = int(input("Выберите действие: "))

        if user_num == 1:
            name = input("Название: ")
            summ = int(input("Сумма: "))
            category = input("Категория: ")
            list_consumption.append({
                "Название": name,
                "Сумма": summ,
                "Категория": category
            })
            print("Расход усспешно добавлен!")
        elif user_num == 2:
            if not list_consumption:
                print("Расходов нет")
            else:
                print("===== ВСЕ РАСХОДЫ =====")
                for index, item in enumerate(list_consumption, start=1):
                    print(f"{index}. {item['Название']} | {item['Сумма']} сом | {item['Категория']}")

        elif user_num == 3:
            for index, item in enumerate(list_consumption, start=1):
                user_po = input("Введите название: ").lower()
                if user_po == item["Название"].lower():
                    print("Найдено:")
                    print(f"{index}. {item['Название']} | {item['Сумма']} сом | {item['Категория']}")
                else:
                    print("Расход не найден")
        elif user_num == 4:
            total = 0
            for sumi in list_consumption:
                if not sumi:
                    print("Расходов нет")
                elif sumi["Сумма"] > 0:
                    total += sumi["Сумма"]
            print(f"Всего расходов: {total}")

        elif user_num == 5:
            if not list_consumption:
                print("Расходов нет")
            else:
                statistics = {}
                for item in list_consumption:
                    category = item["Категория"]
                    summ = item["Сумма"]
                    if category in statistics:
                        statistics[category] += summ
                    else:
                        statistics[category] = summ
                print("===== СТАТИСТИКА =====")
                for category, summ in statistics.items():
                    print(f"{category}: {summ} сом")


expense_manager()
