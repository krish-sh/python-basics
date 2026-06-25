Number = 6

if Number >= 1 and Number <= 10:
    User = int(input("Guess a number between 1 to 10: "))
    while Number != User:
        if Number > User:
            print("User No is smaller")
            User = int(input("Choose another Number: "))
        else:
            print("User No is Higher")
            User = int(input("Choose another Number: "))
        if Number == User:
            print("Congrats You Guess the Right Number🎉:", User)   
else: 
    print("Your Number is not between 1 to 10")
    Number = int(input("print a number between 1 to 10: "))