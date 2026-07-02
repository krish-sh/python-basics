temps = [32.5, 30.1, 35.8, 31.2, 33.4, 29.8, 36.2]  
days  = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

for i, day in enumerate(days):
    print(f"{day}: {temps[i]}°C")

for i, day in enumerate(days):
    max_temp = max(temps)
    total = sum(temps)
    average = total / len(temps)
    if temps[i] == max_temp:
        print(f"Average temperature: {average: .2f}°C")
        print(f"The highest temperature was on {day}: {temps[i]}°C")