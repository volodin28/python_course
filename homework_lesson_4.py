# 1) У вас є змінна величина, тип - int. Напишіть тернарний оператор для змінної new_value за таким правилом: якщо
#     значення менше 100, то new_value дорівнює половині значення, у протилежному випадку - протиположне
#     значенню число

while True:
    try:
        value = int(input("Input integer:"))
        break
    except ValueError:
        print("Wrong input")
new_value = value / 2 if value < 100 else value * -1
print(new_value)

#########################################################
#
# 2) У вас є змінна величина, тип - int. Написати тернарний оператор для змінної new_value за таким правилом: якщо
#     значення менше 100, то new_value дорівнює 1, у протилежному випадку - 0

# while True:
#     try:
#         value = int(input("Input integer:"))
#         break
#     except ValueError:
#         print("Wrong input")
# new_value = 1 if value < 100 else 0
# print(new_value)

########################################################
# 3) У вас є змінна величина, тип - int. Напишіть тернарний оператор для змінного new_value за таким правилом: якщо
#     значення менше 100, то new_value дорівнює True, у протилежному випадку - False

# while True:
#     try:
#         value = int(input("Input integer:"))
#         break
#     except ValueError:
#         print("Wrong input")
# new_value = True if value < 100 else False
# print(new_value)

########################################################
# 4) У вас є змінна my_str, тип - str. Якщо її довше менше 5, то допишіть в кінці строки її ж.
#     Приклад: було - "qwer", стало - "qwerqwer". Якщо довжина не менше 5, то залишити строку як є.

# value = input("Input text:")
# new_value = value * 2 if len(value) < 5 else value
# print(new_value)

########################################################
# 5) У вас є змінна my_str, тип - str. Якщо її довжина менше 5, то допишіть в кінці рядка перевернуту її ж.
#     Приклад: було - "qwer", стало - "qwerrewq". Якщо довжина не менше 5, то залишити строку як є.

# value = input("Input text:")
# new_value = value + value[::-1] if len(value) < 5 else value
# print(new_value)

########################################################

# 6) Допрацювати завдання з калькулятором, щоб в кінці вичислення у користувача запитало, чи потрібен  калькулятор ще.
#   Якщо так, то запустити програму з початку.

# print('Welcome to the Talking Calculator!')
# calc_again = "YES"
# while calc_again == "YES":
#     while True:
#         try:
#             print("What would you like to do?")
#             print("1. Add")
#             print("2. Sub")
#             print("3. Multiply")
#             print("4. Divide")
#             operator = int(input("So, what are we going to do? Choose your destiny: "))
#             break
#         except ValueError:
#             print("Nice try, but next time try to choose something between 1 and 4")
#
#     if operator in (1, 2, 3, 4):
#         try:
#             value_1 = float(input("Your first number: "))
#             value_2 = float(input("Your second number: "))
#         except ValueError:
#             print("Do you know what NUMBER is? Calculation is over. Next time don't touch any letters of symbols:)")
#     else:
#         print("Nice try, but next time try to choose something between 1 and 4")
#     if operator == 1:
#         print(value_1, "+", value_2, "=", value_1 + value_2)
#
#     elif operator == 2:
#         print(value_1, "-", value_2, "=", value_1 - value_2)
#
#     elif operator == 3:
#         print(value_1, "*", value_2, "=", value_1 * value_2)
#
#     elif operator == 4 and value_2 == 0:
#         print("No way you want to divide by zero. The universe is gonna explode. \nSO please, do smth else next time")
#
#     elif operator == 4:
#         print(value_1, "/", value_2, "=", value_1 / value_2)
#     question = input("Would you like to use calcylator again? \nType YES:")
#     calc_again = question.upper()
# print("This is the end. Thanks for using Talking Calculator. See u later")
