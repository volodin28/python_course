print('Welcome to the Talking Calculator!')
print("What would you like to do?")
print("1. Add")
print("2. Sub")
print("3. Multiply")
print("4. Divide")
calc_again = "YES"
while calc_again == "YES":
    while True:
        try:
            operator = int(input("So, what are we going to do? Choose your destiny: "))
            break
        except ValueError:
            print("Nice try, but next time try to choose something between 1 and 4")

    if operator in (1, 2, 3, 4):
        try:
            value_1 = float(input("Your first number: "))
            value_2 = float(input("Your second number: "))
        except ValueError:
            print("Do you know what NUMBER is? Calculation is over. Next time don't touch any letters of symbols:)")
    else:
        print("Nice try, but next time try to choose something between 1 and 4")
    if operator == 1:
        print(value_1, "+", value_2, "=", value_1 + value_2)

    elif operator == 2:
        print(value_1, "-", value_2, "=", value_1 - value_2)

    elif operator == 3:
        print(value_1, "*", value_2, "=", value_1 * value_2)

    elif operator == 4 and value_2 == 0:
        print("No way you want to divide by zero. The universe is gonna explode. \nSO please, do smth else next time")

    elif operator == 4:
        print(value_1, "/", value_2, "=", value_1 / value_2)
    question = input("Would you like to use calcylator again? \nType YES:")
    calc_again = question.upper()
print("This is the end. Thanks for using Talking Calculator. See u later")
