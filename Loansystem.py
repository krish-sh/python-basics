name = input("Enter your name: ")
age = int(input("Enter your age: "))
Salary = int(input("Enter your Salary: "))
Score = int(input("Enter your Score: "))
if age >= 21 and age <=60:
    if Salary >= 25000:
        if Score >= 700:
            print("Eligble for Loan")
        else:
            print("Score is low")
    else:
        print("Salary is less than from our Loan criteria")
else:
    print("Your age is not under the loan criteria")