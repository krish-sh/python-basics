balance = 12000
pinCode= 4325

Output = int(input("Enter 4 digit PinCode: "))

while Output != pinCode:
    print("Incorrect Pincode, Try again")
    Output = int(input("Enter 4 digit PinCode: "))

if pinCode == Output:
    amount = int(input("Withdrawl Amount: "))
    if balance >= amount:
        balance = balance - amount
        print("Amount Withdrawl Successfully")
        print("Balance:", balance)
    else :
        print("Insufficent balance")