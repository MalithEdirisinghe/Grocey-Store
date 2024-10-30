from datetime import datetime

def add_sales_transaction(transaction_data, grocery_data):
    
    # Get current date and time
    date = datetime.now().strftime('%d/%m/%Y')  # Adjusted to DD/MM/YYYY format for consistency
    time = datetime.now().strftime('%I:%M:%S %p')
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity: "))

    # Find the product in grocery_data
    for product in grocery_data:
        if product[0] == product_id:
            price = float(product[2])
            payment = price * quantity
            
            # Update stock
            current_stock = int(product[3])
            if quantity > current_stock:
                print(f"Insufficient stock! Only {current_stock} items available.")
                return transaction_data, grocery_data
            
            product[3] = str(current_stock - quantity)

            # Create a new transaction entry
            new_transaction = [date, time, product_id, str(quantity), f"{payment:.2f}"]
            
            # Add the transaction to transaction_data
            transaction_data.append(new_transaction)
            
            print("Transaction added:", new_transaction)  # Debugging statement
            return transaction_data, grocery_data

    print("Product not found!")
    return transaction_data, grocery_data

def search_transactions(transaction_data, grocery_data):
    """
    Search transactions based on user-specified criteria.
    """
    print("\nSearch Transactions")
    print("1. Search by Date")
    print("2. Search by Product Name")
    print("3. Search by Product Name and Date Range")
    choice = input("Enter your choice: ")

    if choice == '1':
        # Search by date
        input_date = input("Enter date (YYYY-MM-DD): ")
        formatted_date = datetime.strptime(input_date, '%Y-%m-%d').strftime('%d/%m/%Y')
        results = [t for t in transaction_data[1:] if t[0] == formatted_date]  # Skip header row

        if results:
            print(f"\nTransactions on {formatted_date}:")
            for transaction in results:
                print(transaction)
        else:
            print("No transactions found on this date.")

    elif choice == '2':
        # Search by product name
        search_term = input("Enter product name to search: ").lower()
        matching_product_ids = [g[0] for g in grocery_data if search_term in g[1].lower()]
        results = [t for t in transaction_data[1:] if t[2] in matching_product_ids]  # Skip header row

        if results:
            print(f"\nTransactions for products matching '{search_term}':")
            for transaction in results:
                print(transaction)
        else:
            print(f"No transactions found for products matching '{search_term}'.")

    elif choice == '3':
        # Search by product name and date range
        search_term = input("Enter product name to search: ").lower()
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        # Convert start and end dates to datetime objects
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')

        # Find matching product IDs
        matching_product_ids = [g[0] for g in grocery_data if search_term in g[1].lower()]

        # Filter transactions by product ID and date range
        results = []
        for t in transaction_data[1:]:  # Skip header row
            try:
                transaction_date_dt = datetime.strptime(t[0], '%d/%m/%Y')  # Convert transaction date to datetime
            except ValueError:
                print(f"Invalid date format in transaction: {t[0]}")
                continue
            
            if t[2] in matching_product_ids and start_date_dt <= transaction_date_dt <= end_date_dt:
                results.append(t)

        if results:
            print(f"\nTransactions for '{search_term}' between {start_date} and {end_date}:")
            for transaction in results:
                print(transaction)
        else:
            print(f"No transactions found for '{search_term}' in the specified date range.")

    else:
        print("Invalid choice. Please try again.")
