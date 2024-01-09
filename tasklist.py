tasks = []

def add_task(tasks, task_name):
  task = {"task": task_name, "Completed": False}
  tasks.append(task)
  print(f"The task {task} was successfully added")
  return

while True:
  print("\nTask Manager Menu: ")
  print("1. Add task")
  print("2. See one task")
  print("3. Update task")
  print("4. Mark task as done")
  print("5. Delete completed task")
  print("6. Exit")

  choice = input("Type your choice: ")

  if choice == "1":
    task_name = input("Type the name of the task: ")
    add_task(tasks, task_name)
  elif choice == "6":
    break

print("==== System Off ====")

