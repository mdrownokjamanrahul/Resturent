# Menu
menu = {
    "Biryani": 180,
    "Chicken Fry": 120,
    "Beef Kebab": 150,
    "Pulao": 130,
    "Cold Drink": 40
}

# Delivery charges
delivery_costs = {
    "Gulistan": 30,
    "Motijheel": 40,
    "Ramna": 50
}

print(" Welcome to our menu:\n")
for item, price in menu.items():
    print(f"{item} - Tk {price}")

# Input order from user and validate items
while True:
    print("\n What would you like to order? (For multiple items, enter names separated by commas e.g., 'Biryani, Pulao, Chicken Fry'):")
    order_input = input("Enter your order: ")
    
    # comma and strip extra spaces
    selected_items = [item.strip() for item in order_input.split(',')]
    invalid_items = []
    
 
    for item in selected_items:
        if item not in menu:
            invalid_items.append(item)

    if invalid_items:
        print("\n Invalid input:", ", ".join(invalid_items))
        print("Please try again with valid items.")
    else:
        break

# Calculate total cost
total_cost = 0
print("\n Processing your selected items:")
for item in selected_items:
    print(f" {item} - Tk {menu[item]}")
    total_cost += menu[item]

print(f"\n Total food cost: Tk {total_cost}")

# Delivery location
print("\n Where do you want your order delivered?")
for city, cost in delivery_costs.items():
    print(f"{city} - Delivery charge Tk {cost}")

city_input = input("\n Enter your city (Gulistan / Motijheel / Ramna): ").strip()

if city_input in delivery_costs:
    delivery_charge = delivery_costs[city_input]
    final_amount = total_cost + delivery_charge
    print(f"\n Delivery charge: Tk {delivery_charge}")
    print(f" Final bill (Food + Delivery): Tk {final_amount}")
else:
    print("\n Invalid city! Delivery charge not added.")
    final_amount = total_cost
    print(f" Final bill (Only food): Tk {final_amount}")

confirm = input("\n Do you want to confirm the order? (yes/no): ").strip().lower()

if confirm == "yes":
    print("\n Thank you! Your order is confirmed. It’ll be delivered soon!")
else:
    print("\n No worries. Come back again later. Bye!")
