tasks = []

def list_task(tasks):
  print("\nTask list: ")
  for index, task in enumerate(tasks, start=1):
    status = "✓" if task["completed"] else " "
    task_name = task["task"]
    print(f"{index}. [{status}] {task_name}")
  return

def add_task(tasks, task_name):
  task = {"task": task_name, "completed": False}
  tasks.append(task)
  print(f"The task {task} was successfully added")
  return

def update_task(tasks, index, new_task_name):
  formatted_index = formatted_index_helper(index)
  tasks[formatted_index]["task"] = new_task_name
  print(f"Task '{new_task_name}' updated successfully.")
  return

def mark_task_as_done(tasks, index):
  formatted_index = formatted_index_helper(index)
  tasks[formatted_index]["completed"] = True

  print(f"Task {index} marked as completed.")
  return

def formatted_index_helper(index):
  index = int(index) - 1
  return index

def is_valid_index(index):
    formatted_index = formatted_index_helper(index)
    return 0 <= formatted_index < len(tasks)

def task_not_found_helper():
  print("Taks not found")
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
  elif choice == "3":
    list_task(tasks)
    task_index = input("Type the task index number to update: ")
    if is_valid_index(task_index):
      new_task_name = input("Type the new task name: ")
      update_task(tasks, task_index, new_task_name)
    else:
      task_not_found_helper()
  elif choice == "4":
    list_task(tasks)
    task_index = input("Type the task index to mark as completed: ")
    if is_valid_index(task_index):
      mark_task_as_done(tasks, task_index)
    else:
      task_not_found_helper()
  elif choice == "6":
    break

print("==== System Off ====")

