def display_groceries(grocery_data):
    """Display all groceries in a formatted table."""
    print("\nID | Name | Price | Stock")
    for item in grocery_data[1:]:  # Skipping the header row
        print(f"{item[0]} | {item[1]} | ${item[2]} | {item[3]}")
    print("\n")

def update_grocery_stock(grocery_data):
    """Update the stock of an existing grocery product."""
    product_id = input("Enter product ID to update stock: ")
    new_stock = input("Enter new stock quantity: ")
    for item in grocery_data:
        if item[0] == product_id:
            item[3] = new_stock
            print("Stock updated successfully!")
            return grocery_data
    print("Product not found!")
    return grocery_data

def add_new_product(grocery_data):
    """Add a new product to the grocery list."""
    product_id = input("Enter new product ID: ")
    product_name = input("Enter product name: ")
    price = input("Enter product price: ")
    stock = input("Enter initial stock level: ")

    # Create a new product entry
    new_product = [product_id, product_name, price, stock]
    grocery_data.append(new_product)
    print("New product added successfully!")
    
    return grocery_data

def search_groceries_by_name(grocery_data):
    """Search groceries by partial name (case-insensitive)."""
    search_term = input("Enter product name to search: ").lower()
    results = [item for item in grocery_data if search_term in item[1].lower()]
    
    if results:
        print(f"\nProducts matching '{search_term}':")
        print("ID | Name | Price | Stock")
        for item in results:
            print(f"{item[0]} | {item[1]} | ${item[2]} | {item[3]}")
    else:
        print(f"No products found matching '{search_term}'")
    print("\n")

def update_grocery_details(grocery_data):
    """Update details of an existing grocery product."""
    product_id = input("Enter the product ID to update: ")
    product = next((item for item in grocery_data if item[0] == product_id), None)

    if product:
        print(f"Current details: ID: {product[0]}, Name: {product[1]}, Price: ${product[2]}, Stock: {product[3]}")
        
        # Update price and stock
        new_price = input("Enter new price (or press enter to keep current): ")
        new_stock = input("Enter new stock (or press enter to keep current): ")
        
        if new_price:
            product[2] = new_price
        if new_stock:
            product[3] = new_stock
        
        print("Product details updated successfully!")
    else:
        print("Product ID not found.")
    
    return grocery_data
