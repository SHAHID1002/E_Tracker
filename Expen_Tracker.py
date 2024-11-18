import os
from datetime import datetime


FILENAME = 'expenses.txt'


if not os.path.exists(FILENAME):
    with open(FILENAME, 'w') as file:
        file.write("Date,Description,Amount\n")


def add_expense():
    description = input("Enter expense description: ").strip()
    amount = input("Enter amount: ").strip()
    

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return


    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(FILENAME, 'a') as file:
        file.write(f"{current_time},{description},{amount}\n")
    print("Expense added successfully!\n")


def view_expenses():
    print("\n--- All Expenses ---")
    with open(FILENAME, 'r') as file:
        lines = file.readlines()

        if len(lines) <= 1:
            print("No expenses recorded yet.")
            return
        
        print("No.\tDate and Time\t\tDescription\tAmount")
        print("---------------------------------------------------------")
        
        for index, line in enumerate(lines[1:], start=1):
            date, description, amount = line.strip().split(',')
            print(f"{index}\t{date}\t{description}\tRs:{float(amount):.2f}")
    print()

def calculate_total():
    with open(FILENAME, 'r') as file:
        lines = file.readlines()

        if len(lines) <= 1:
            print("No expenses recorded yet.")
            return

        total = 0
        for line in lines[1:]:
            _, _, amount = line.strip().split(',')
            total += float(amount)

    print(f"\nTotal Expenses: Rs:{total:.2f}\n")


def search_expense():
    keyword = input("Enter keyword to search: ").strip().lower()

    with open(FILENAME, 'r') as file:
        lines = file.readlines()

        if len(lines) <= 1:
            print("No expenses recorded yet.")
            return

        print("\n--- Search Results ---")
        print("No.\tDate and Time\t\tDescription\tAmount")
        print("---------------------------------------------------------")

        found = False
        for index, line in enumerate(lines[1:], start=1):
            date, description, amount = line.strip().split(',')
            if keyword in description.lower():
                print(f"{index}\t{date}\t{description}\tRs:{float(amount):.2f}")
                found = True

        if not found:
            print("No matching expenses found.")
    print()


def delete_expense():
    view_expenses()
    try:
        index_to_delete = int(input("Enter the expense number to delete: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    with open(FILENAME, 'r') as file:
        lines = file.readlines()

    if len(lines) <= 1 or index_to_delete < 1 or index_to_delete > len(lines) - 1:
        print("Invalid expense number.")
        return

    del lines[index_to_delete]

    with open(FILENAME, 'w') as file:
        file.writelines(lines)

    print("Expense deleted successfully!\n")

# Function to display the menu
def display_menu():
    print("===== Simple Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expenses")
    print("4. Search Expenses by Description")
    print("5. Delete an Expense")
    print("6. Exit")

def main():
    for _ in iter(int, 1): 
        display_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_total()
        elif choice == '4':
            search_expense()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

# Run the main function
if __name__ == "__main__":
    main()
