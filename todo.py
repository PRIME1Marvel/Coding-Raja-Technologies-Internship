# Function to display the to-do list
def display_list(todo_list):
    print("To-Do List:")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index}. {item}")

# Function to add an item to the to-do list
def add_item(todo_list, item):
    todo_list.append(item)
    print(f"'{item}' added to the to-do list.")

# Function to remove an item from the to-do list
def remove_item(todo_list, index):
    if 1 <= index <= len(todo_list):
        item = todo_list.pop(index - 1)
        print(f"'{item}' removed from the to-do list.")
    else:
        print("Invalid index.")

# Main function
def main():
    todo_list = []

    while True:
        print("\nChoose an option:")
        print("1. Display to-do list")
        print("2. Add item to to-do list")
        print("3. Remove item from to-do list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_list(todo_list)
        elif choice == "2":
            item = input("Enter the item to add: ")
            add_item(todo_list, item)
        elif choice == "3":
            index = int(input("Enter the index of the item to remove: "))
            remove_item(todo_list, index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

main()