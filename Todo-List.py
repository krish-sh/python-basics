tasks = []

print("===== TODO LIST =====")

user = input("Enter 'Add' for adding and 'Done' for ending, 'Show' for showing, 'Complete' for completing: ")

def add_task(task):
    tasks.append(task)
    print("Added task: ", task)

def show_task():
    print("===== Pending Todo ====")
    for i,t in enumerate(tasks, 1):
        print(i,". ", t)

def completed_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Completed Task✅ ", task )
    else :
        print("Task not found")

add_task('Coading')
add_task('DSA')
add_task('Driving')
add_task('Math')


if user.lower() == 'add':
    while True:
         task = input("Enter items, 'done' for ending: ")
         if task.lower() == "done":
             show_task()
             break
         add_task(task)

elif user.lower() == 'done':
    show_task()

elif user.lower() == 'show':
    show_task()

elif user.lower() == 'complete':
    task = input("Enter Completed Task: ")
    completed_task(task)

