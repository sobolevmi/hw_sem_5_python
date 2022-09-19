# Программа по реализации игры с конфетами

def candies(count, player):
    """Функция по уменьшению числа конфет после хода пользователя
    Аргументы: count - общее количество конфет; player - имя игрока"""
    player_candies = int(input(f"Количество конфет: {count}. Сколько конфет вы хотите взять, {player}? "))
    while player_candies < 1 or player_candies > 28:
        player_candies = int(input(f"Нельзя брать больше 28 конфет. Попробуйте снова, {player}: "))
    if count >= 28:
        count = count - player_candies
    else:
        while player_candies > count:
            player_candies = int(input("Осталось меньше конфет, чем вы хотите взять. Попробуйте снова: "))
        count = count - player_candies
    return count

input("Игра с конфетами. Для продолжения нажмите Enter")
mode = int(input("Выберите пользовательский режим - нажмите 1 для игры с другим пользователем "
                 "или нажмите 2 для игры с компьютером: "))
if mode == 1:
    player_1 = str(input("Введите имя первого игрока: "))
    player_2 = str(input("Введите имя второго игрока: "))
    count_candies = 2021
    from random import randint
    choice = randint(1, 2)
    if choice == 1:
        input(f"{player_1} начинает. Для продолжения нажмите Enter")
        while count_candies != 0:
            count_candies = candies(count_candies, player_1)
            if count_candies == 0:
                print(f"{player_2} победил(а)!")
                break
            count_candies = candies(count_candies, player_2)
            if count_candies == 0:
                print(f"{player_1} победил(а)!")
                break
    if choice == 2:
        input(f"{player_2} начинает. Для продолжения нажмите Enter")
        while count_candies != 0:
            count_candies = candies(count_candies, player_2)
            if count_candies == 0:
                print(f"{player_1} победил(а)!")
                break
            count_candies = candies(count_candies, player_1)
            if count_candies == 0:
                print(f"{player_2} победил(а)!")
                break
elif mode == 2:
    player = str(input("Введите ваше имя: "))
    count_candies = 2021
    from random import randint
    cpu_choice = randint(1, 28)
    complication = int(input(f"{player}, выберите уровень сложности: нажмите 1 для низкого уровня сложности "
                             "или нажмите 2 для высокого уровня сложности: "))
    while complication < 1 or complication > 2:
        complication = int(input(f"{player}, вы ввели неправильное число, попробуйте снова: "))
    choice = randint(1, 2)
    if choice == 1:
        input(f"{player} начинает. Для продолжения нажмите Enter")
        while count_candies != 0:
            if complication == 2:
                cpu_choice = count_candies
            count_candies = candies(count_candies, player)
            if count_candies == 0:
                print(f"Компьютер победил!")
                break
            if complication == 2:
                cpu_choice = 29 - (cpu_choice - count_candies)
            if count_candies <= 28:
                cpu_choice = count_candies
            count_candies = count_candies - cpu_choice
            print(f"Компьютер взял {cpu_choice} конфет(ы)")
            if count_candies == 0:
                print(f"{player}, вы победили!")
                break
    if choice == 2:
        input(f"Компьютер начинает. Для продолжения нажмите Enter")
        n = 10
        while count_candies != 0:
            if complication == 2:
                cpu_choice = 29 - n
            if count_candies <= 28:
                cpu_choice = count_candies
            if count_candies == 57:
                cpu_choice = 28
            count_candies = count_candies - cpu_choice
            print(f"Компьютер взял {cpu_choice} конфет(ы)")
            if count_candies == 0:
                print(f"{player}, вы победили!")
                break
            if complication == 2:
                n = count_candies
            count_candies = candies(count_candies, player)
            if count_candies == 0:
                print(f"Компьютер победил!")
                break
            if complication == 2:
                n = n - count_candies
else:
    mode = int(input("Вы ввели неверное число. Попробуйте еще раз: "))