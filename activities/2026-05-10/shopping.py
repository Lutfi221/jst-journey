def main():
    shopping_list = []
    
    print("--- Personal Shopping Assistant ---")

    while True:
        # 1. Display the current list
        print("\nYour shopping list:")
        total = 0
        for item in shopping_list:
            item_total = item['price'] * item['qty']
            total += item_total
            print(f"${item['price']} @ {item['qty']} {item['name']} = ${item_total}")
        
        print(f"\nTotal = ${total}")
        print("-" * 30)

        # 2. Get user input
        print("\nAdd item to shopping list (or type 'quit' to exit)")
        name = input("Item name: ")
        if name.lower() == 'quit':
            break
            
        try:
            price = float(input("Price per unit: $"))
            qty = int(input("Quantity: "))
            
            # 3. Store the item
            shopping_list.append({
                "name": name,
                "price": price,
                "qty": qty
            })
        except ValueError:
            print("Invalid input. Please enter numbers for price and quantity.")

    print("Happy shopping!")

if __name__ == "__main__":
    main()