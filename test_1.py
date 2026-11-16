# Имя:
# Фамилия:
# Возраст:
# Город:
# Колледж:
# Язык программирования:
# Короткое предложение:
# Первая оценка:
# Вторая оценка:
# Третья оценка:
# Четвертая оценка:
# Пятая оценка:

name = input('Имя: ')
surname = input('Фамилия: ')
age = input('Возраст: ')
city = input('Город: ')
kol = input('Колледж: ')
language = input('Язык програмирование: ')
text = input('Короткое предложение: ')
#
name = name.capitalize()
surname = surname.capitalize()
city = city.title()
language = language.capitalize()

print("Город:", city.capitalize())
print("Город маленькими буквами:", city.lower())
print("Город большими буквами:", city.upper())
kol = kol.title()
# Имя состоит только из букв: True
# Возраст состоит только из цифр: True
print("Имя состоит только из букв: ", name.isalpha())
print("Возраст состоит только из цифр: ",age.isdigit())


text1 = text
print(f"Исходный текст: ",text1)
print("Маленькими буквами:\n",text1.lower())
print("Большими буквами::\n",text1.upper())
print("Python находится на позиции:",text1.find("Python"))
print("После замены:\n",text1.replace("Python",'Django'))
text2 = text1.split()
print("Список слов: ",text2)
print("Количество слов: ",len(text2))

nom1 = int(input('Первая оценка: '))
nom2 = int(input('Вторая оценка: '))
nom3 = int(input('Третья оценка: '))
nom4 = int(input('Четвертая оценка: '))
nom5 = int(input('Пятая оценка: '))

numbers = [nom1, nom2, nom3, nom4, nom5]
print("Оценки: ",numbers)
print("Количество оценок: ",len(numbers))
print("Самая высокая: ",max(numbers))
print("Самая низкая: ",min(numbers))
print("Сумма: ",sum(numbers))
print("По возрастанию: ",sorted(numbers))
print("Средний балл: ",sum(numbers) / len(numbers))

print("----format()----\n\n")
print("Меня зовут {} {}.".format(name, surname))
print("Мне {} лет.".format(age))
print("Я живу в городе {}.".format(city))
print("Я учусь в {} и изучаю {}.".format(kol, language))
print("\n\n----f-строка----\n\n")
print(f"Меня зовут {name} {surname}.")
print(f"Мне {age} лет.")
print(f"Я живу в городе {city}.")
print(f"Я учусь в {kol} и изучаю {language}.")



print(f"Имя:\t\t{name}")
print(f"Возраст:\t{age}")
print(f"Город:\t\t{city}")

print(f"Он сказал: \"{text}\"")
print(f"Мой город: '{city}'")

a = r"C:\Python\Projects\student.py"
print(f"Путь:\n{a}")
print(f"Мои данные: {{{name}, {surname}, {age}, {city}}}")
