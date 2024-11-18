
first = int(input("Enter the first number: "))

second = int(input("Enter the Second number: "))

operation = input("Enter the mathematical Operation e.g. + , - , /, * ")

if (operation == '+'):
    result = first + second
    print(result)

elif (operation == '*'):
    result = first * second
    print(result)

elif (operation == '-'):
    result = first - second
    print(result)

elif (operation == '/'):
    if (second != 0):
        result = first / second
        print(result)
    else:
        print("Cannot divide by zero")
        
else:
    print("invalid Operation")
    




