import dictionary

inventory = {}
while True:

    print("1 - Add/Update item")
    print("2 - Delete item")
    print("3 - Exit")

    num = input("Enter number between 1-3: ")

    if num == "1":
        widget_name = input("Enter widget name: ")
        quantity = int(input("Enter the quantity: "))
        dictionary.add_inventory(inventory, widget_name, quantity)            
        print("Item added/updated in inventory.")

    elif num == "2":
        widget_name = input("Enter the widget name to DELETE: ")
        result = dictionary.delete_inventory(inventory, widget_name)
        print(result)

    elif num == "3":
        print("Exiting the program. ")
        break

    else:
        print("Invalid selection. Please enter 1-3: ")