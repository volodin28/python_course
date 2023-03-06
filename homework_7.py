# 1. Дано ціле число (int). Визначити скільки нулів у цьому числі.

value = 1200
print(str(value).count("0"))

# 2. Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі

# value = 1002000
# value_rev = str(value)[::-1]
# print(value_rev)
# count = 0
# for i in value_rev:
#     if i == "0":
#         count += 1
#     else:
#         break
# print(count)


# 3. Дано списки my_list_1 та my_list_2.
# Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.

# my_list_1 = [1, 2, 3, 4]
# my_list_2 = [5, 6, 7, 8]
# my_result = my_list_1[1::2] + my_list_2[1::2]
# print(my_result)


# 4. Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
# стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]

# my_list = [1, 2, 3, 4,]
# new_list = my_list[1:] + my_list[:1]
# print(new_list)

# 5. Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
# [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)

# my_list = [1, 2, 3, 4]
# my_list.insert(len(my_list), my_list.pop(0))
# print(my_list)

# 6. Дано рядок у якому є числа (розділяються пробілами).
# Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
# Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)

# value = "43 більше ніж 34, але менше ніж 56"
# value_list = value.replace(",", "").split(" ")
# print(value_list)
# new_val_list = [int(x) for x in value_list if x.isdigit()]
# print(new_val_list)
# print(sum(new_val_list))


# 7. Наведено список чисел. Визначте, скільки в цьому списку елементів,
# які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
# Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.

# value = [2, 4, 1, 5, 3, 9, 0, 7]
# count = 0
# for i in range(1, len(value) - 1):
#     if value[i] > value[i - 1] + value[i + 1]:
#         count += 1
# print(count)


# 8. Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
# Наприклад [1, 2, 3, "11", "22", 33]
# Створити новий список у який помістити лише рядки з my_list.

# my_list = [1, 2, 3, "11", "22", 33]
# new_list = [x for x in my_list if type(x) == str]
# print(new_list)

# 9. Дано рядок my_str. Створити список в який помістити символи з my_str,
# які зустрічаються в рядку ТІЛЬКИ ОДИН раз.

# my_str = "122sdfsdfs/../3456"
# my_list = [x for x in my_str if my_str.count(x) == 1]
# print(my_list)

# 10. Дано два рядки. Створити список, у якому помістити ті символи,
# які є в обох рядках хоча б один раз.

# my_str_1 = 'sdfsdf1'
# my_str_2 = 'sdfsdf1'
# set_1 = set(my_str_1)
# set_2 = set(my_str_2)
# set_3 = set_1.intersection(set_2)
# my_list = list(set_3)
# print(my_list)

# 11. Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
# але в кожній ТІЛЬКИ З одного разу.
# Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному разу

# my_str_1 = 'aaaasdf1'
# my_str_2 = 'asdfff2'
# my_list_1 = [x for x in my_str_1 if my_str_1.count(x) == 1]
# my_list_2 = [x for x in my_str_2 if my_str_2.count(x) == 1]
# print(my_list_1)
# print(my_list_2)
# set_3 = set(my_list_1).intersection(set(my_list_2))
# print(list(set_3))