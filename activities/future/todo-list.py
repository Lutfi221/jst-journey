todos = []


def add_todo(todos):
    todo = input("Enter a todo: ")
    todos.append({"todo": todo, "completed": False})
    print("Todo added: " + todo)

def remove_todo(todos):
    todo = input("Enter a todo: ")
    todos.remove({"todo": todo, "completed": False})
    print("Todo removed: " + todo)

def complete_todo(todos):
    i = input("Enter a todo number: ")
    todos[int(i)]["completed"] = True
    print("Todo completed: " + todos[int(i)]["todo"])

def view_todos(todos):
    for i, t in enumerate(todos):
        print(str(i) + ". " + t["todo"] + " - " + str(t["completed"]))

def main():
    while True:
        print("1. Add a todo")
        print("2. Remove a todo")
        print("3. Complete a todo")
        print("4. View todos")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            remove_todo(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            view_todos(todos)
        elif choice == "5":
            break
