tasks = []

def list_task(tasks):
  print("\nTask list: ")
  for indice, task in enumerate(tasks, start=1):
    status = "✓" if task["completed"] else " "
    task_name = task["task"]
    print(f"{indice}. [{status}] {task_name}")
  return

def add_task(tasks, task_name):
  task = {"task": task_name, "completed": False}
  tasks.append(task)
  print(f"The task {task} was successfully added")
  return

while True:
  print("\nTask Manager Menu: ")
  print("1. Add task")
  print("2. See all tasks")
  print("3. Update task")
  print("4. Mark task as done")
  print("5. Delete completed task")
  print("6. Exit")

  choice = input("Type your choice: ")

  if choice == "1":
    task_name = input("Type the name of the task: ")
    add_task(tasks, task_name)
  elif choice == "2":
    list_task(tasks)
  elif choice == "6":
    break

print("==== System Off ====")

