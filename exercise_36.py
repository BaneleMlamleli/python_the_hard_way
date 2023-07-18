def addition(firstNumber, secNumber):
    sum = firstNumber + secNumber
    print(f"{firstNumber} + {secNumber} = {sum}")


def multiplication(firstNumber, secNumber):
    mult = firstNumber * secNumber
    print(f"{firstNumber} x {secNumber} = {mult}")


def subtraction(firstNumber, secNumber):
    sub = firstNumber - secNumber
    print(f"{firstNumber} - {secNumber} = {sub}")


def division(firstNumber, secNumber):
    if secNumber == 0:
        print("ERROR!! cannot divie be zero")
        while secNumber == 0:
            secNumber = input("Enter second number: ")
            secNumber = float(secNumber)
    else:
        div = firstNumber / secNumber
        print(f"{firstNumber} / {secNumber} = {div}")


print("\nCalculator program!!\n===================\n")
options = input(
    "A - Addition\nM - Multiplication\nS - Subtraction\nD - Division\nEnter option: "
)
options = options.upper()

if options == "A":
    num = input("First number: ")
    num = float(num)
    num1 = input("Second number: ")
    num1 = float(num1)
    addition(num, num1)
elif options == "M":
    num = input("First number: ")
    num = float(num)
    num1 = input("Second number: ")
    num1 = float(num1)
    multiplication(num, num1)
elif options == "D":
    num = input("First number: ")
    num = float(num)
    num1 = input("Second number: ")
    num1 = float(num1)
    division(num, num1)
elif options == "S":
    num = input("First number: ")
    num = float(num)
    num1 = input("Second number: ")
    num1 = float(num1)
    subtraction(num, num1)
else:
    print("Error! select within the provided options")
