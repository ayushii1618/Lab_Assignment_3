def load_items(file_name):
    """Load items and prices from a file into a dictionary."""
    items = {}
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                if "|" in line:
                    name, price = line.strip().split("|")
                    items[name.strip()] = int(price.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        exit()
    return items


def get_valid_item(items):
    """Prompt the user until a valid item name is entered."""
    while True:
        item = input().strip()
        if item in items:
            return item
        else:
            print(f"Available Items are {list(items.keys())}.")
            print("Try Again.")


def get_valid_money():
    """Prompt the user until a valid integer amount is entered."""
    while True:
        amount = input().strip()
        try:
            return int(amount)
        except ValueError:
            print(f"Bad Input {amount}.")
            print("Try Again.")


def vending_machine():
    items = load_items("VendingItems.txt")
    
    # Step 1: Get valid item
    selected_item = get_valid_item(items)
    price = items[selected_item]
    
    # Step 2: Get valid money
    deposited_money = get_valid_money()
    
    # Step 3: Show purchase message
    if deposited_money < price:
        print(f"Insufficient money. {selected_item} costs {price} Rs.")
    elif deposited_money == price:
        print("Thank you for your purchase. Enjoy")
    else:
        change = deposited_money - price
        print("Thank you for your purchase. Enjoy")
        print(f"Do not forget to collect your change, {change} Rs.")


# Run the vending machine
if __name__ == "__main__":
    vending_machine()
