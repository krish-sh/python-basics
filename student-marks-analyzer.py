students = ["Rahul", "Radhika", "Sahil", "Harish"]
marks = [85, 92,78, 32]

total = sum(marks)
average  = total / len(marks)
highest  = max(marks)
lowest = min(marks)

score = 'Pass'

for i, name in enumerate(students):
    if marks[i] >= 40:
        score  = 'Pass'
    else:
        score = 'Fail'
    print(name, "has scored", marks[i], "-----", score)

print("Average marks: ", average)
print("Highest marks: ", highest)
print("Lowerst marks: ", lowest)