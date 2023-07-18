def listFunction(maxValue, incrementValue):
    i = 0
    numbers = []

    while i < maxValue:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + incrementValue
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)


maxValue = int(input("Enter maximum looping value: "))
incrementalValue = int(input("Enter incremental value: "))
listFunction(maxValue, incrementalValue)
