no1 = int(input("Enter first Number: "))
no2 = int(input("Enter Second Number: "))

operator = input("Enter any valid Operator: ")

if operator == "+" :
    print(no1 + no2)

elif operator == "-" :
    print(no1 - no2)
elif operator == "*" :
    print(no1 * no2)
elif operator == "/":
    print(no1 / no2)
else :
    print("Not a valid Operator")    