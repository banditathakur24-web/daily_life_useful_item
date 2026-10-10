
import json
import os
from datetime import date

FILE_NAME = "daily_assistant_data.json"


def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            pass
    return {"tasks": [], "expenses": []}


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_task(data):
    task = input("Enter your task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return

    data["tasks"].append({
        "task": task,
        "done": False,
        "date": str(date.today())
    })
    save_data(data)
    print("Task added successfully!")


def view_tasks(data):
    if not data["tasks"]:
        print("No tasks added yet.")
        return

    print("\n--- YOUR TASKS ---")
    for i, task in enumerate(data["tasks"], start=1):
        status = "Completed" if task["done"] else "Pending"
        print(f'{i}. {task["task"]} | {status} | {task["date"]}')


def complete_task(data):
    view_tasks(data)
    if not data["tasks"]:
        return

    try:
        number = int(input("Enter task number to complete: "))
        if 1 <= number <= len(data["tasks"]):
            data["tasks"][number - 1]["done"] = True
            save_data(data)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def add_expense(data):
    title = input("What did you spend money on? ").strip()
    if not title:
        print("Expense description cannot be empty.")
        return

    try:
        amount = float(input("Enter amount in rupees: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    data["expenses"].append({
        "title": title,
        "amount": amount,
        "date": str(date.today())
    })
    save_data(data)
    print("Expense saved successfully!")


def view_expenses(data):
    print("\n--- YOUR EXPENSES ---")
    if not data["expenses"]:
        print("No expenses recorded yet.")
        return

    total = 0
    for i, expense in enumerate(data["expenses"], start=1):
        print(
            f'{i}. {expense["title"]} - '
            f'Rs. {expense["amount"]:.2f} '
            f'({expense["date"]})'
        )
        total += expense["amount"]

    print(f"Total spending: Rs. {total:.2f}")


def main():
    data = load_data()

    print("=" * 38)
    print("    SMART DAILY LIFE ASSISTANT")
    print("=" * 38)

    while True:
        print("\n1. Add a daily task")
        print("2. View all tasks")
        print("3. Mark a task completed")
        print("4. Add an expense")
        print("5. View expenses and total")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_task(data)
        elif choice == "2":
            view_tasks(data)
        elif choice == "3":
            complete_task(data)
        elif choice == "4":
            add_expense(data)
        elif choice == "5":
            view_expenses(data)
        elif choice == "6":
            print("Thank you for using Smart Daily Life Assistant!")
            break
        else:
            print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
    main()