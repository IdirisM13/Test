import time

while True:
    print("Игра начинается!")
    time.sleep(2)
    print("Тебе нужно выбраться отсюда")
    time.sleep(2)
    print("Выбери одну дверь")
    time.sleep(2)
    print("Первый дверь номер 1")
    time.sleep(2)
    print("Второй дверь номер 2")
    try:
        user_num = int(input("Введите номер двери: "))
    except ValueError:
        print("Ошибка! Введите число.")
        continue
    if user_num == 1:
        time.sleep(2)
        print("В этой двери был маньяк тебя убили!")
        break
    elif user_num == 2:
        print("Ты выжил")
        time.sleep(2)
        print("Заходишь в дверь, а там три двери")
        time.sleep(2)
        print("В одной тигр голодный уже месяц ")
        time.sleep(2)
        print("В другой яма змей")
        time.sleep(2)
        print("И выход")
        try:
            user_num2 = int(input("Выбери одну из трех: 1, 2, 3: "))
        except ValueError:
            print("Ошибка! Введите число.")
            continue

        if user_num2 == 1:
            time.sleep(2)
            print("Ты попал в комнату с тигром")
            time.sleep(2)
            print("Так как тигр уже месяц голодный")
            time.sleep(2)
            print("То он уже умер, ты выжил")
            time.sleep(2)
            print("В конце комнаты дверь")
            print("1)Войдешь внутрь или 2) останешся в комнате ожидая помощи?")
            try:
                user_num3 = int(input("Выберите действие: "))
            except ValueError:
                print("Ошибка! Введите число.")
                continue
            time.sleep(2)
            if user_num3 == 1:
                game_over = False
                while True:
                    print("Внутри длинный темный каридор направа и налево")
                    time.sleep(2)
                    print("Куда пойдешь?\n1)Направа\n2)Налево")
                    try:
                        user_num4 = int(input("Выберите действие: "))
                    except ValueError:
                        print("Ошибка! Введите число.")
                        continue
                    if user_num4 == 1:
                        time.sleep(2)
                        print("В конце каридора темный железный дверь")
                        time.sleep(2)
                        print("Твои действие\n1) Зайти внуть\n2)Вернуться назад")
                        try:
                            user_num5 = int(input("Выберите действие: "))
                        except ValueError:
                            print("Ошибка! Введите число.")
                            continue
                        if user_num5 == 1:
                            time.sleep(2)
                            print("Ты вошел в комнату")
                            time.sleep(2)
                            print("Там ядовитый газ\nТы умер")
                            break
                        elif user_num5 == 2:
                            print("Ты вернулся назад")
                            continue
                        else:
                            print("Такого дейсвие нету")
                            continue
                    elif user_num4 == 2:
                        time.sleep(2)
                        print("В конце каридора деревянный дверь")
                        time.sleep(2)
                        print("Твои действие\n1) Зайти внуть\n2)Вернуться назад")
                        try:
                            user_num6 = int(input("Выберите действие: "))
                        except ValueError:
                            print("Ошибка! Введите число.")
                            continue
                        if user_num6 == 1:
                            time.sleep(2)
                            print("Лесница на верх")
                            time.sleep(2)
                            print("Ты поднимаешься\nСтальная дверь с пятизначным кодом\nУгадай код")
                            try:
                                user_num7 = int(input("Введите код: "))
                            except ValueError:
                                print("Ошибка! Введите число.")
                                continue
                            if user_num7 == 21121:
                                print("Ты угадал\nТы свободен")
                                game_over = True
                                break
                            else:
                                print("Неправильно\nМаньяк нашел тебя\nТы мертв")
                                break
                    else:
                        print("Такого действие нет!")
                        continue
                if game_over:
                    break

            elif user_num3 == 2:
                print("Ты умер от обезвоживание")
                break
            else:
                print("Такого действие нет!")
                continue
        elif user_num2 == 2:
            time.sleep(2)
            print("Ты попал в яму змей и умер")
            break
        elif user_num2 == 3:
            time.sleep(2)
            print("Ты вошел в комнату с маньяком")
            time.sleep(2)
            print("Тебя убили")
            break
        else:
            print("Такой двери нету!")
            continue
    else:
        print("Такой двери нету!")
        continue