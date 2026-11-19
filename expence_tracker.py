# Expense Tracker Project

expenses_list = []  # List of expenses stored as dictionaries
print("Welcome to Expense Tracker!")

while True:
    print("\n==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    try:
        choice = int(input("Please enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    # 1. Add Expense
    if choice == 1:
        date = input("Enter date (e.g., 19-11-2026): ")
        category = input("Enter category (Food, Travel, Books, Other): ")
        description = input("Enter description: ")
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Expense not added.")
            continue

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses_list.append(expense)
        print("\nExpense added successfully!")

    # 2. View All Expenses
    elif choice == 2:
        if len(expenses_list) == 0:
            print("No expenses recorded yet.")
        else:
            print("\n===== All Recorded Expenses =====")
            for count, item in enumerate(expenses_list, start=1):
                print(
                    f"#{count} | Date: {item['date']} | Category: {item['category']} "
                    f"| Description: {item['description']} | Amount: ₹{item['amount']:.2f}"
                )

    # 3. View Total Spending
    elif choice == 3:
        total = sum(item["amount"] for item in expenses_list)
        print(f"\nTOTAL SPENDING = ₹{total:.2f}")

    # 4. Exit
    elif choice == 4:
        print("Thank you for using Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
