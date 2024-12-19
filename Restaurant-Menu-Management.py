def add_item(menu, item):
    menu.append(item)
    return menu

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"Error: '{item}' not found in the menu.")
    return menu

def check_item(menu, item):
    if item in menu:
        return f"Availability: '{item}' is available"
    else:
        return f"Availability: '{item}' is not available"

def manage_menu():
    menu = input("Enter the initial menu items, separated by commas: ").split(",")
    menu = [item.strip() for item in menu]
    
    while True:
        print("\nMenu Options:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Check item availability")
        print("4. Show current menu")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_item_name = input("Enter the item to add: ")
            menu = add_item(menu, add_item_name)
        
        elif choice == '2':
            remove_item_name = input("Enter the item to remove: ")
            menu = remove_item(menu, remove_item_name)
        
        elif choice == '3':
            check_item_name = input("Enter the item to check: ")
            print(check_item(menu, check_item_name))
        
        elif choice == '4':
            print(f"Current menu: {menu}")
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice, please try again.")

manage_menu()
