#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

while True: 
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))

        if num1 == num2:
            print("Equal")
        break
    except ValueError:
        print("Error: Enter a valid number.")