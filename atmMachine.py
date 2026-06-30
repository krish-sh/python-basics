balance = 5000
pinCode= 4325

Output = int(input("Enter 4 digit PinCode: "))
while Output != pinCode:
    print("Incorrect Pincode, Try again")
    Output = int(input("Enter 4 digit PinCode: "))
    
if pinCode == Output:
    Check = input("What you want to do: Check balance, Deposit Money or Withdraw money.")
    if Check ==  "Check balance":
        print("Current Balance: ", balance)
    elif Check == "Deposit Money":
        Deposit = int(input("Enter Deposit amount: "))
        if Deposit <= 0:
           print("Amount Not valid")
        else:
           balance += Deposit
        print("Money Deposit Successfully")
        print("Current Balance: ", balance)
    elif Check == "Withdraw money":
     amount = int(input("Withdrawl Amount: "))
     if balance >= amount:
        balance = balance - amount
        print("Amount Withdrawl Successfully")
        print("Balance:", balance)
     else :
        print("Insufficent balance")
