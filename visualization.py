# import matplotlib.pyplot as plt
# import numpy as np
# from datetime import datetime

# # Helper function to extract the month from the date in 'dd/mm/yyyy' format
# def extract_month(date_str):
#     return datetime.strptime(date_str, "%d/%m/%Y").strftime("%B")

# # Monthly sales performance line chart
# def plot_monthly_sales(transaction_data):
#     # Extract months and payments from transactions
#     months = [extract_month(row[0]) for row in transaction_data[1:]]
#     payments = [float(row[4]) for row in transaction_data[1:]]

#     # Aggregate sales by month
#     unique_months = sorted(set(months))
#     monthly_sales = [sum(payments[i] for i in range(len(months)) if months[i] == month) for month in unique_months]

#     # Plotting
#     plt.figure(figsize=(10, 6))
#     plt.plot(unique_months, monthly_sales, marker='o')
#     plt.title("Monthly Sales Performance")
#     plt.xlabel("Month")
#     plt.ylabel("Total Sales ($)")
#     plt.grid(True)
#     plt.show()

# # Bar chart for individual product sales
# def plot_product_sales(transaction_data, grocery_data):
#     # Create a mapping of product IDs to product names
#     product_map = {row[0]: row[1] for row in grocery_data[1:]}
#     product_sales = {}

#     # Calculate total sales for each product
#     for transaction in transaction_data[1:]:
#         product_id = transaction[2]
#         payment = float(transaction[4])
#         product_name = product_map.get(product_id, "Unknown")
#         product_sales[product_name] = product_sales.get(product_name, 0) + payment

#     # Extract product names and sales values
#     products = list(product_sales.keys())
#     sales_values = list(product_sales.values())

#     # Plotting
#     plt.figure(figsize=(12, 6))
#     plt.bar(products, sales_values, color='skyblue')
#     plt.title("Total Sales by Product")
#     plt.xlabel("Product")
#     plt.ylabel("Total Sales ($)")
#     plt.xticks(rotation=45, ha='right')
#     plt.tight_layout()
#     plt.show()

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def plot_monthly_sales(transaction_data):
    """
    Plot total monthly sales values and number of sales transactions.
    """
    start_month = input("Enter start month (YYYY-MM): ")
    end_month = input("Enter end month (YYYY-MM): ")
    
    # Prepare monthly data within the specified range
    monthly_sales = {}
    for transaction in transaction_data[1:]:  # Skip header row
        try:
            transaction_date = datetime.strptime(transaction[0], '%d/%m/%Y')
            transaction_month = transaction_date.strftime('%Y-%m')
            
            # Filter by the specified range
            if start_month <= transaction_month <= end_month:
                if transaction_month not in monthly_sales:
                    monthly_sales[transaction_month] = {'total_sales': 0, 'num_transactions': 0}
                
                monthly_sales[transaction_month]['total_sales'] += float(transaction[4])  # Sum payment
                monthly_sales[transaction_month]['num_transactions'] += 1
        except ValueError:
            continue

    if not monthly_sales:
        print(f"No transactions found between {start_month} and {end_month}.")
        return

    # Prepare data for plotting
    months = sorted(monthly_sales.keys())
    total_sales = [monthly_sales[m]['total_sales'] for m in months]
    num_transactions = [monthly_sales[m]['num_transactions'] for m in months]

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(months, total_sales, label='Total Sales', color='b', marker='o')
    ax.plot(months, num_transactions, label='Number of Transactions', color='g', marker='s')
    ax.set_xlabel('Month')
    ax.set_ylabel('Values')
    ax.set_title('Monthly Sales and Transactions')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_product_sales(transaction_data, grocery_data):
    """
    Plot monthly sales values and number of sales for a specific product.
    """
    product_name = input("Enter product name: ").lower()
    start_month = input("Enter start month (YYYY-MM): ")
    end_month = input("Enter end month (YYYY-MM): ")

    # Get the product ID
    product_id = next((g[0] for g in grocery_data if product_name in g[1].lower()), None)
    if not product_id:
        print(f"Product '{product_name}' not found.")
        return

    # Prepare monthly data for the specific product
    monthly_sales = {}
    for transaction in transaction_data[1:]:  # Skip header row
        try:
            transaction_date = datetime.strptime(transaction[0], '%d/%m/%Y')
            transaction_month = transaction_date.strftime('%Y-%m')
            
            if transaction[2] == product_id and start_month <= transaction_month <= end_month:
                if transaction_month not in monthly_sales:
                    monthly_sales[transaction_month] = {'total_sales': 0, 'num_transactions': 0}
                
                monthly_sales[transaction_month]['total_sales'] += float(transaction[4])  # Sum payment
                monthly_sales[transaction_month]['num_transactions'] += 1
        except ValueError:
            continue

    if not monthly_sales:
        print(f"No transactions found for '{product_name}' between {start_month} and {end_month}.")
        return

    # Prepare data for plotting
    months = sorted(monthly_sales.keys())
    total_sales = [monthly_sales[m]['total_sales'] for m in months]
    num_transactions = [monthly_sales[m]['num_transactions'] for m in months]

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(months, total_sales, label='Total Sales', color='b', marker='o')
    ax.plot(months, num_transactions, label='Number of Transactions', color='g', marker='s')
    ax.set_xlabel('Month')
    ax.set_ylabel('Values')
    ax.set_title(f"Monthly Sales for '{product_name.capitalize()}'")
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_total_sales_by_product(transaction_data, grocery_data):
    """
    Plot total sales values by product within a given date range.
    """
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Prepare product sales data within the specified range
    product_sales = {}
    for transaction in transaction_data[1:]:  # Skip header row
        try:
            transaction_date = datetime.strptime(transaction[0], '%d/%m/%Y')
            if start_date <= transaction_date.strftime('%Y-%m-%d') <= end_date:
                product_id = transaction[2]
                product_name = next((g[1] for g in grocery_data if g[0] == product_id), "Unknown")
                if product_name not in product_sales:
                    product_sales[product_name] = 0
                product_sales[product_name] += float(transaction[4])
        except ValueError:
            continue

    if not product_sales:
        print(f"No transactions found between {start_date} and {end_date}.")
        return

    # Sort products by total sales
    sorted_sales = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    products = [item[0] for item in sorted_sales]
    total_sales = [item[1] for item in sorted_sales]

    # Plotting
    fig, ax = plt.subplots()
    ax.bar(products, total_sales, color='b')
    ax.set_xlabel('Product')
    ax.set_ylabel('Total Sales')
    ax.set_title('Total Sales by Product')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
