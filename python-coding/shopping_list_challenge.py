# Challenge: Shopping List formatter

shopping_list = []

# Section One: Creating the shopping list
while True:

    item = input("Enter an item (or 'q' to quit): ")
    if item.lower() == 'q':
        break

    # Challenge: Ask user for a price (int)
    # handle any ValueError by printing a message, skipping a loop and asking for a new item

    try:
        price = int(input("Enter the price (£) of the item: "))
    except ValueError as e:
        print("Invalid input! Please enter a valid price.")
        print(f"Error: {e}")
        continue

    shopping_list.append((item, price))

    # SECTION TWO - formatting the shopping list
total = 0

for item, price in shopping_list:
    print(f"{item} - £{price}")
    total += price

print(f"Total price: £{total}")

# Challenge: use a for loop to print each item and price on its own line
# after all items have been output, also print out the total price

"""
Program output:
python shopping_list_challenge.py
Enter an item (or 'q' to quit): flowers
Enter the price (£) of the item: 10
Enter an item (or 'q' to quit): bread
Enter the price (£) of the item: four
Invalid input! Please enter a valid price.
Error: invalid literal for int() with base 10: 'four'
Enter an item (or 'q' to quit): bread
Enter the price (£) of the item: 4
Enter an item (or 'q' to quit): ice cream
Enter the price (£) of the item: 5
Enter an item (or 'q' to quit): q
flowers - £10
bread - £4
ice cream - £5
Total price: £19
"""