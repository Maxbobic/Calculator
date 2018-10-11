calc = input("Addition, Subtraction, Multiply, and Division \n").upper()
dNum1 = float(input("enter the first number \n"))
dNum2 = float(input("enter the second number \n"))
try:
    if calc == "ADD":
        print(dNum1 + dNum2)
    elif calc == "SUBTRACTION":
        print(dNum1 - dNum2)
    elif calc == "MULTIPLY":
        print(dNum1 * dNum2)
    elif calc == "DIVISION":
            print(dNum1 / dNum2)
except ZeroDivisionError:
    print("You cannot divide by zero")
