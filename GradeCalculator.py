no1 = int(input("Enter Subject First number: "))
no2 = int(input("Enter Subject Second number: "))
no3 = int(input("Enter Subject Third number: "))

total = no1 +no2 + no3
grade =int( (total/300) * 100)

if grade >= 90:
    print("Grade A")
elif grade >= 75 and grade <= 89:
    print("Grade B")
elif grade >= 50 and grade <= 74:
    print("Grade C")
else :
    print("Fail")