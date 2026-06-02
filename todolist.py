import os

def load_tasks():
    if os.path.exists('todo.txt'):
        with open('todo.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(tasks):
    with open('todo.txt', 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST ---")
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        
        print("\nOptions: [1] Add [2] Update [3] Delete [4] Exit")
        choice = input("Select: ").strip()

        if choice == '1':
            new_task = input("Enter task: ").strip()
            if new_task:
                tasks.append(f"[ ] {new_task}")
                save_tasks(tasks)
                print("Task added.")

        elif choice == '2':
            if not tasks: continue
            idx = int(input("Task number to update/toggle: ")) - 1
            if 0 <= idx < len(tasks):
                print("[A] Edit Text [B] Mark Done/Undone")
                sub = input("Choice: ").upper()
                if sub == 'A':
                    new_val = input("New text: ").strip()
                    status = "[x]" if "[x]" in tasks[idx] else "[ ]"
                    tasks[idx] = f"{status} {new_val}"
                else:
                    if "[ ]" in tasks[idx]:
                        tasks[idx] = tasks[idx].replace("[ ]", "[x]")
                    else:
                        tasks[idx] = tasks[idx].replace("[x]", "[ ]")
                save_tasks(tasks)
                print("Updated.")

        elif choice == '3':
            if not tasks: continue
            idx = int(input("Task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
                print("Deleted.")

        elif choice == '4':
            print("Done for today.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()