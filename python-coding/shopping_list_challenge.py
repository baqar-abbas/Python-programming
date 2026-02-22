# Challenge: Shopping List formatter

shopping_list = []

# Section One: Creating the shopping list
while True:

    item = input("Enter an item (or 'q' to quit): ")
    if item.lower() == 'q':
        break

    # Challenge: Ask user for a price (int)
    # handle any ValueError by printing a message, skipping a loop and asking for a new item

    price = int(input("Enter the price (£) of the item: "))

    shopping_list.append((item, price))

    # SECTION TWO - formatting the shopping list
total = 0

# Challenge: use a for loop to print each item and price on its own line
# after all items have been output, also print out the total price