# 1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.

# my_list = ["qwe", "Slavik", "Katya", "qwe", "Slavik", "Katya"]
# new_list = []
#
# for i, k in enumerate(my_list):
#     if i % 2 == 0:
#         new_list.append(k[::-1])
#     else:
#         new_list.append(k)
#
# print(new_list)

# 2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
# у яких перший символ - буква "a".

# my_list = ["qwe", "aSlavik", "Katya", "Aqwe", "Slavik", "Katya"]
#
# new_list = [x for x in my_list if x.lower().startswith("a")]
#
# print(new_list)


# 3. Наведено список рядків my_list. Створити новий список до якого помістити
# елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

# my_list = ["qwe", "aSlavik", "Katya", "Aqwe", "Slavik", "Katya"]
#
# new_list = [x for x in my_list if "a" in x]
#
# print(new_list)

# 4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]

# my_list = [
#     {"name": "John", "age": 15},
#     {"name": "Slavik", "age": 27},
#     {"name": "Jack", "age": 45},
#     {"name": "Piter", "age": 15},
# ]

# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.

# seq = [x['age'] for x in my_list]
# min_age = min(seq)
# new_list_a = [i['name'] for i in my_list if i['age'] == min_age]
#
# print(new_list_a)

# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.

# seq = [x['name'] for x in my_list]
# longest_name = len(max(seq, key=len))
# new_list_b = [i['name'] for i in my_list if len(i['name']) == longest_name]
#
# print(new_list_b)


# в) Порахувати середній вік усіх людей із початкового списку.

# seq = [x['age'] for x in my_list]
# avg_age = sum(seq) / len(seq)
#
# print(avg_age)


# 5) Дано два словники my_dict_1 і my_dict_2.

my_dict_1 = {
    1: 1,
    2: 2,
    5: 5,
}

my_dict_2 = {
    11: 11,
    2: 22,
}

# а) Створити список із ключів, які є в обох словниках.
# set_1 = set(my_dict_1.keys())
# set_2 = set(my_dict_2.keys())
# list_a = list(set_1.intersection(set_2))
#
# print(list_a)

# б) Створити список із ключів, які є у першому, але немає у другому словнику.
# set_1 = set(my_dict_1.keys())
# set_2 = set(my_dict_2.keys())
# list_b = list(set_1.difference(set_2))
#
# print(list_b)

# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
set_1 = set(my_dict_1.keys())
set_2 = set(my_dict_2.keys())
list_c = list(set_1.difference(set_2))
my_list = []

for i, k in my_dict_1.items():
    if i in list_c:
        my_list.append(i)
        my_list.append(k)
my_dict = {my_list[i]: my_list[i + 1] for i in range(0, len(my_list), 2)}

print(my_dict)

# set_1 = set(my_dict_1.keys())
# set_2 = set(my_dict_2.keys())
# key_difference_list = list(set_1.difference(set_2))
# my_dict = dict()
#
# for i in key_difference_list:
#     my_dict[i] = my_dict_1[i]
#
# print(my_dict)

# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},
#
# #{1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

# new_dict = {}
# for key_1, val_1 in my_dict_1.items():
#     for key_2, val_2 in my_dict_2.items():
#         new_dict.update({key_1: val_1})
#         new_dict.update(({key_2: val_2}))
#
# for key_1, val_1 in my_dict_1.items():
#     for key_2, val_2 in my_dict_2.items():
#         if key_1 == key_2:
#             new_dict.update({key_1: [val_1, val_2]})
# print(new_dict)


set_1 = set(my_dict_1.keys())
set_2 = set(my_dict_2.keys())
key_difference_list = list(set_1.difference(set_2))
my_dict = dict()

for i in key_difference_list:
    my_dict[i] = my_dict_1[i]

print(my_dict)