
name = input("Имя: ").capitalize()
surname = input("Фамилия: ").capitalize()
age = input("Возраст: ")
city = input("Город: ").capitalize()
kol = input("Колледж: ").title()
language = input("Язык: ").capitalize()
text = input("Предложение: ")
print("Имя: ", name)
print("Фамилия: ", surname)
print("Возраст: ", age)
print("Город: ", city)
print("Колледж: ", kol)
print("Язык: ", language)
print("Предложение: ", text)
res = "Имя введено правильно" if name.isalpha() else "Ошибка в имени"
res2 = "Возраст введено правильно" if age.isdigit() else "Ошибка в возрасте"
print(res)
print(res2)
print("Исходный текст: ", text)
print("Маленькими буквами: ", text.lower())
print("Большими буквами: ", text.upper())
print("Позиция Python: ", text.find("Python"))
print("После замены: ", text.replace("Python", "Django"))
text1 = text.split()
print("Список слов: ", text1)
print("Количество слов: ", len(text1))
res = "Python найден" if text == "Python" else "Python не найден"
print(res)


nom1 = int(input("Введите оценку 1: "))
nom2 = int(input("Введите оценку 2: "))
nom3 = int(input("Введите оценку 3: "))
nom4 = int(input("Введите оценку 4: "))
nom5 = int(input("Введите оценку 5: "))
grades = [nom1, nom2, nom3, nom4, nom5]
print("Все оценки: ",grades)
print("Количество: ", len(grades))
print("Самая высокая: ", max(grades))
print("Самая низкая: ", min(grades))
print("Сумма: ", sum(grades))
print("Средний балл: ", sum(grades) // len(grades))
print("По возрастанию: ", sorted(grades))
grades = sum(grades) // len(grades)
if grades >= 4.5:
    print("Отлично")
elif grades >= 3.5:
    print("Хорошо")
elif grades >= 2.5:
    print("Удовлетворительно")
else:
    print("Нужно учиться лучше")

skills = ["Python", "HTML", "CSS"]
skills.append("Django")
print(skills)
skills.insert(1, "JavaScript")
print(skills)
skills.append("Python")
print(skills.count("Python"))
skills.remove("CSS")
print(skills)
res = skills.pop(-1)
print(res)
skills.sort()
print(skills)
skills.reverse()
print(skills)

other_skills = ["Git", "SQL"]
res = skills + other_skills
print(res)
print(other_skills * 2)
print("Python есть в списке: ", "Python" in res)
print("Java есть в списке:" , "Java" in res)
del res[1]
print(res)
print(res[0])
print(res[-1])
print(res[0:3])
print(res[-3:])
print(res[::-1])

words = ["код", "программа", "Python", "программирование", "IT"]
#
print("Самое длинное слово: ", max(words))
print("Самое короткое слово: ", min(words))
print("Длина самого длинного: ", len(max(words)))
print("Длина самого короткое: ", len(min(words)))
print("По длине: ", len(words))

students = [
    ["Эрлан", 25, "Бишкек"],
    ["Айбек", 22, "Ош"],
    ["Нурбек", 24, "Талас"]
]
students[1][0] = "Азамат"
students[2][-1] = "Нарын"
print(students[-1][::-1], students[-2][::-1],students[-3][::-1])

age = int(input("Введите возраст: "))
bil = input("Есть ли у вас билет? (да/нет): ").lower()
vip = input("Есть ли у вас VIP? (да/нет): ").lower()
if age < 18 and bil == "да":
    print("Запрещено по возрасту")
elif bil == "нет":
    print("Нет билета")
elif age >= 18 and bil == "да" or vip == "да":
    print("Вход разрешен")
else:
    print("Неверные данные")

age = int(input("Введите возраст: "))
tes = int(input("Введите число: "))
city = input("Годод: ")
tes2 = input("День недели: ")
res = "Совершеннолетний" if age >= 18 else "Несовершеннолетний"
print(res)
res = "Четное" if tes % 2 == 0 else "Нечетное"
print(res)
res = "Столица" if city == "Бишкек" else "Другой годор"
print(res)
res = "Выходной" if tes2 == "Суббота" or tes2 == "Воскресенье" else "Рабочий день"
print(res)



print("Меня зовут {} {}, мне {} лет".format(name, surname, age))
print("Я живу в городе {} и изучаю {}.".format(city, language))
print(f"Меня зовут {name} {surname}, мне {age} лет")
print(f"Я живу в городе {city} и изучаю {language}.")
print(f"Мои данные: {{{name}, {surname}, {age}, {city}}}")

print("Имя:\t\t",name)
print("Возраст:\t",age)
print("Город:\t\t",city)
print(f"Он сказал: \"{text}\"")
print(f"Мой годод: '{city}'")

print("Путь:\nC:\\Python\\Projects\\student.py")

print("Python",end=" ")
print("Student")

print("Навыки после очистки:",skills.clear())

