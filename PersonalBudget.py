def input_expenses(categories):
    expenses = {}
    for category in categories:
        expense = float(input(f"Enter your {category} expenses: "))
        expenses[category] = expense
    return expenses

def calculate_total(expenses):
    total = sum(expenses.values())
    return total

def display_summary(expenses, total):
    print("\nExpense Summary:")
    for category, expense in expenses.items():
        print(f"{category}: ${expense:.2f}")
    print(f"Total Expenses: ${total:.2f}")

def main():
    categories = ["Groceries", "Rent", "Utilities", "Entertainment"]
    expenses = input_expenses(categories)
    total = calculate_total(expenses)
    display_summary(expenses, total)

main()