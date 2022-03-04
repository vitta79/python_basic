try:
    print(str(int(input("Enter a number: "))))
    result = 10 / 0
except ValueError:
    print("Invalid input")
except ZeroDivisionError as err:
    print(err)