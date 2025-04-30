#main menu
def main_menu():
    while True:
        print("\n---INVENTORY SYSTEM---")
        print("\nMain Menu:")
        print("[1] Add New Stock")
        print("[2] Process Sale")
        print("[3] View Inventory")


        print("[4] Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_new_stock()
        elif choice == "2":
            process_sale()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid selection. Please try again.")
#Adding new stock
def add_new_stock():
    while True:
        item_name = input("Enter item name: ")

        # validating the input in quantity 
        while True:
            quantity = input("Enter quantity: ")
            if quantity.isdigit():
                quantity = int(quantity)
                break
            else:
                print("Invalid input. Please enter a number.")

        # validating the correct format in date
        while True:
            purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
            if len(purchase_date) == 10 and purchase_date[4] == '-' and purchase_date[7] == '-':
                year, month, day = purchase_date[:4], purchase_date[5:7], purchase_date[8:]
                if year.isdigit() and month.isdigit() and day.isdigit():
                    break
            print("Invalid date format. Please enter in YYYY-MM-DD format.")

        # adding item in inventory
        inventory.append({"name": item_name, "quantity": quantity, "date": purchase_date})

        # Ask to add another item
        while True:
            another = input("Add another item? (yes/no): ")
            if another == "yes":
                break
            elif another == "no":
                print("Stock added successfully!")
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


        
#Processing sale
def process_sale():
    while True:
        item_name = input("Enter item name: ")
        
   
        if not any(item['name'] == item_name for item in inventory):
            print("Item not found. Please enter a valid item name.")
            continue
        
        while True:
            qts = input("Enter quantity to sell: ")
            if qts.isdigit():
                qts = int(qts)
                break
            else:
                print("Invalid input. Please enter a number.")
        
        available = sum(item['quantity'] for item in inventory if item['name'] == item_name)

        #sorting bydate FIFO
        if available >= qts:
            remaining = qts
            for item in sorted(inventory, key=lambda x: x['date']):
                if item['name'] == item_name:
                    if item['quantity'] <= remaining:
                        remaining -= item['quantity']
                        item['quantity'] = 0
                    else:
                        item['quantity'] -= remaining
                        remaining = 0
                    
                    
                    if remaining == 0:
                        break
                    
            # Remove items with zero quantity
            i = 0
            while i < len(inventory):
                if inventory[i]['quantity'] == 0:
                    del inventory[i]
                else:
                    i += 1


            print("Sale processed successfully!")
            break
        else:
            print("Insufficient stock. Please enter item details again.")

#Viewing inventory
inventory = []

def view_inventory():
    print("\nInventory List:")
    if not inventory:
        print("No items in inventory.")
        return

    # Sort inventory by purchase date (FIFO view)
    sorted_inventory = sorted(inventory, key=lambda x: x['date'])

    print(f"{'Item No.':<10} {'Name':<20} {'Quantity':<10} {'Purchase Date':<15}")
    print("-" * 60)

    for idx, item in enumerate(sorted_inventory, start=1):
        print(f"{idx:<10} {item['name']:<20} {item['quantity']:<10} {item['date']:<15}")

    
main_menu()