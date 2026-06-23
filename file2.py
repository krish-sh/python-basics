name = input("Enter your name:")
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))

bmi = weight / (height * height)

print("Name:", name)
print("BMI:", round(bmi, 2))