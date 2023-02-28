# 1. Дано рядок.
#      a. виведіть третій символ цього рядка.
#      b. виведіть передостанній символ цього рядка.
#      c. виведіть перші п'ять символів цього рядка.
#      d. виведіть весь рядок, крім двох останніх символів.
#      e. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться починаючи)
#      з першого).
#      f. виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
#      g. виведіть усі символи у зворотному порядку.
#      h. виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
#      i. виведіть довжину цього рядка.

value = "qwerty"
length = len(value)

print("a.", value[2:3]) #виведіть третій символ цього рядка.
print("b.", value[-2:-1]) #виведіть передостанній символ цього рядка.
print("c.", value[:6]) #виведіть перші п'ять символів цього рядка.
print("d.", value[:length-2]) #виведіть весь рядок, крім двох останніх символів.
print("e.", value[::2]) #виведіть усі символи з парними індексами
print("f.", value[1::2]) #виведіть усі символи з непарними індексами
print("g.", value[::-1]) #виведіть усі символи у зворотному порядку.
print("h.", value[::-2]) #виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
print("i.", length) #виведіть довжину цього рядка.

#2. Дано рядок, що складається зі слів, розділених пробілами. Визначте, скільки у ній слів. Використовуйте для вирішення
# завдання функцію `count`

# value = "qwerty qwerty qwerty qwerty"
# print(value.count(" ") + 1)

# 3. Користувач вводить окремо рядок `s` та один символ `ch`. Необхідно здійснити пошук у рядку `s` всіх символів `ch`.
# Для вирішення можна використовувати тільки функцію `find` (rfind), оператори `if` та `for` (while).

# s = "qwertqyqqqq"
# ch = "q"
# count = 0
# for i in s:
#     if i == ch:
#         count += 1
# print(count)

# Дано рядок. Замініть у цьому рядку всі появи літери `h` на літеру `H`, крім першого та останнього входження.

# value = "aHasdadhhasdasdhasda"
# first_h = value.find("h")
# last_h = value.rfind("h")
# print(value[:first_h + 1] + value[first_h + 1: last_h].replace("h", "H") + value[last_h:])
