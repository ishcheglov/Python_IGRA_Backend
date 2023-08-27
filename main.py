import json
import time
from time import sleep
import random

horse_list = []
bet_list = []


def main(horse_num=None, bet_num=None):
    print()
    print("🏇" * 27)
    print("  Боб хочет собрать всех своих друзей-предпринимателей вместе.\n"
          "Но для того, чтобы заставить занятых друзей прийти к нему,\n"
          "следует сделать что-то необычное. У Боба есть ферма, на которой\n"
          "живут 10 лошадей. Он хочет провести скачки со ставками.\n"
          "Лошади пронумерованы от 1 до 10. На одну и ту же лошадь нельзя\n"
          "сделать ставку дважды. Также нельзя делать нулевую ставку.")
    print("🏇" * 25)
    print("\t\t\t*** Делайте ставки господа! ***")
    print(time.strftime("\t\t\t\t %m/%d/%Y, %H:%M:%S\n"))
    get_horse(horse_num, bet_num)


def get_horse(horse_num, bet_num):  # Функция отвечает за номер лошади, на которую делают ставку.
    """
    Функция отвечает за номер лошади, на которую делают ставку,
    учтены ошибки при вводе пользователя.
    """
    if len(horse_list) == 10:
        get_igra()
    else:
        try:
            while len(horse_list) != 10 and len(horse_list) == len(bet_list):
                horse_num = int(input("На какую лошадь будем ставить? "))
                if horse_num < 1 or horse_num > 10:
                    print("Введите число от 1 до 10")
                    get_horse(horse_num, bet_num)
                elif 0 < horse_num < 11:
                    horse_list.append(horse_num)
                    print("Поставили на лошадь:", horse_list)
                    get_bet(horse_num, bet_num)
        except ValueError:
            print("Нужно ввести число от 1 до 10")
            get_horse(horse_num, bet_num)


def get_bet(horse_num, bet_num):
    """
    Функция отвечает за ставку  на лошадь, учтены ошибки
    при вводе пользователя.
    """
    bet_num = int(input("Сколько делаем ставку? "))
    try:
        if bet_num <= 0:
            print("Введите сумму больше нуля")
            get_bet(horse_num, bet_num)
        elif bet_num > 0:
            bet_list.append(bet_num)
            print(f"Ваша ставка в размере {bet_num} рублей на лошадь {horse_num} принята!\n")
            get_horse(horse_num, bet_num)
    except ValueError:
        print("Нужно ввести целое число больше нуля")
        get_bet(horse_num, bet_num)


def get_igra():
    """
    Функция симулирует шкалу, которая двигается по времени
    с интервалом 2 секунды.
    """
    print("Скачки начались, господа!\n")
    print("🏇", end="", flush=True)
    sleep(2)
    print(">>🏇", end="", flush=True)
    sleep(2)
    print(">>🏇", end="", flush=True)
    sleep(2)
    print(">>🏇", end="", flush=True)
    sleep(2)
    print(">>🏇", end="", flush=True)
    sleep(2)
    print(">>🏇", end="", flush=True)
    sleep(2)
    print(">>🏇", end="", flush=True)
    sleep(2)
    print(">>🏇", end="", flush=True)
    sleep(2)
    print(">>🏇", end="", flush=True)
    sleep(2)
    print(">>🏇", end="", flush=True)
    sleep(2)
    print(">>🏇", end="", flush=True)
    sleep(2)
    print("\n")

    get_result()


def get_result():
    """
    Функция выдает результат скачек, какая лошать пришла первой,
    кто победитель и какую сумму он выиграл. Используется модуль
    random и time. Словарь создан для контроля игры, запись в
    файл.json.
    """
    print("\t Ура! Есть победитель!")

    horse = random.choice(horse_list)
    bet = 0

    for i in bet_list:
        bet += i
    time_now = time.strftime("%m/%d/%Y, %H:%M:%S\n")
    print(f"\t В скачках {time_now} победила лошадь под номером {horse}!")
    print(f"Кто поставил на лошадь {horse} получает вознаграждение в размере {bet} рублей.\n"
          "\t\t\t\t *** Поздравляем победителя! ***")
    print("\t\t\t\t\t  ", "💰" * 10, end="")

    time_data = time.strftime("%m/%d/%Y, %H:%M:%S")
    bet_data = {"Итоги скачек": time_data, "Победила": horse, "Выигрыш": bet}
    bet_result = dict(zip(horse_list, bet_list))
    bet_data.update(bet_result)

    with open("bet_data.json", "w", encoding="utf=8") as file:
        json.dump(bet_data, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
