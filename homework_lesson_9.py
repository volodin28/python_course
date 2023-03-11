# 1. Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
# елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни.
def my_list_trans(input_list):
    new_list = []
    for i, k in enumerate(input_list):
        if i % 2 == 0:
            new_list.append(k[::-1])
        else:
            new_list.append(k)
    print(new_list)
    return None


my_list = ["qwe", "Slavik", "Katya", "aqwe", "Slavik", "Katya"]
my_list_trans(my_list)


# 2. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".

def list_start_a(input_list):
    new_list = [x for x in input_list if x.lower().startswith("a")]
    print(new_list)

    return None


list_start_a(my_list)


# 3. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

def list_with_a(input_list):
    new_list = [x for x in input_list if "a" in x]
    print(new_list)

    return None


list_with_a(my_list)


# 4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки
# (type str) і цілі числа (type int).
# Функція повертає новий список у якому містяться лише рядки з my_list.

def only_str(input_val):
    new_list = [x for x in input_val if type(x) == str]
    print(new_list)
    return None


my_list = [1, 2, 3, "11", "22", 33]
only_str(my_list)


# 5. Написати функцію яка приймає один параметр – рядок my_str.
# Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.


def one_time_sym(input_str):
    res_list = []
    for symbol in set(input_str):
        if input_str.count(symbol) == 1:
            res_list.append(symbol)
    print(res_list)

    return None


my_str = "rrrrrrhhhhauuuub"
one_time_sym(my_str)


# 6. Написати функцію яка приймає один параметр - два рядки.
# Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.


def symb_intersection(str_1, str_2):
    val_set = set(str_1).intersection(set(str_2))
    res_list = list(val_set)
    print(res_list)

    return None


my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
symb_intersection(my_str_1, my_str_2)

#
# 7. Написати функцію яка приймає два параметри - два рядки.
# Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.


def unique_symb_intersection(str_1, str_2):
    res_list = []
    for symbol in set(str_1).intersection(set(str_2)):
        if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
            res_list.append(symbol)
    print(res_list)

    return None


unique_symb_intersection(my_str_1, my_str_2)


# 8. Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
#     "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
# Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
# Рядок і число генерувати випадковим чином.
#
# Приклад використання функції:
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
#
# Відповідь: miller.249@sgdyyur.com

from random import (randint, choice)
from string import ascii_lowercase


def email_generator():
    names = ["king", "miller", "kean"]
    domains = ["net", "com", "ua"]
    rand_i = ''.join(choice(ascii_lowercase) for _ in range(randint(5, 8)))
    print(f"{choice(names)}{randint(100, 999)}@{rand_i}.{choice(domains)}")

    return None


email_generator()
