try:
    num1 = int(input("Enter a number: "))
    op = str(input("Enter a op: "))
    num2 = int(input("Enter a number:"))
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

if op == "+":
    print (num1 + num2)
elif op == "-" :
    print (num1 - num2)
elif op == "*":
    print( num1 * num2)
elif op == "/":
    print (num1 / num2)
else:
    print("Not op")

