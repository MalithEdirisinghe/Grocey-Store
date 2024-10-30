from utils import load_csv, save_csv
from user_manager import authenticate_user
from grocery_manager import (display_groceries, update_grocery_stock, 
                             add_new_product, search_groceries_by_name, 
                             update_grocery_details)
from transaction_manager import add_sales_transaction, search_transactions
from visualization import plot_monthly_sales, plot_product_sales, plot_total_sales_by_product
import os

def main():
    # Set absolute paths for CSV files
    users_file_path = os.path.abspath('./data/users.csv')
    grocery_file_path = os.path.abspath('./data/groceries.csv')
    transactions_file_path = os.path.abspath('./data/transactions.csv')
    
    # Load CSV files
    users_data = load_csv(users_file_path)
    grocery_data = load_csv(grocery_file_path)
    transaction_data = load_csv(transactions_file_path)

    # User Authentication
    role = authenticate_user(users_data)
    if not role:
        print("Authentication failed!")
        return

    while True:
        if role == 'manager':
            print("\nManager Menu")
            print("1. Display Groceries")
            print("2. Update Grocery Stock")
            print("3. Add New Product")
            print("4. Search Transactions")
            print("5. Search Groceries by Name")
            print("6. Update Grocery Details")
            print("7. View Monthly Sales Performance")
            print("8. View Product Sales Performance")
            print("9. View Total Sales by Product")
            print("10. Logout")

        elif role == 'cashier':
            print("\nCashier Menu")
            print("1. Add Sales Transaction")
            print("2. Logout")

        choice = input("Enter your choice: ")

        if role == 'manager':
            if choice == '1':
                display_groceries(grocery_data)

            elif choice == '2':
                grocery_data = update_grocery_stock(grocery_data)

            elif choice == '3':
                grocery_data = add_new_product(grocery_data)

            elif choice == '4':
                search_transactions(transaction_data, grocery_data)

            elif choice == '5':
                search_groceries_by_name(grocery_data)

            elif choice == '6':
                grocery_data = update_grocery_details(grocery_data)

            elif choice == '7':
                plot_monthly_sales(transaction_data)

            elif choice == '8':
                plot_product_sales(transaction_data, grocery_data)

            elif choice == '9':
                plot_total_sales_by_product(transaction_data, grocery_data)

            elif choice == '10':
                save_csv(grocery_file_path, grocery_data)
                save_csv(transactions_file_path, transaction_data)
                print("Data saved. Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

        elif role == 'cashier':
            if choice == '1':
                transaction_data, grocery_data = add_sales_transaction(transaction_data, grocery_data)
                save_csv(transactions_file_path, transaction_data)
                print(f"Transaction data saved to {transactions_file_path}")
            elif choice == '2':
                # Save before logging out
                save_csv(grocery_file_path, grocery_data)
                save_csv(transactions_file_path, transaction_data)
                print("Data saved. Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
