import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Define products and their categories/prices
products = {
    'Coffee': {
        'Espresso': 3.00,
        'Americano': 3.50,
        'Latte': 4.50,
        'Cappuccino': 4.50,
        'Mocha': 5.00,
        'Cold Brew': 4.75,
        'Macchiato': 3.75
    },
    'Tea': {
        'Green Tea': 3.25,
        'Earl Grey': 3.25,
        'Chai Latte': 4.50,
        'Peppermint Tea': 3.25,
        'Matcha Latte': 5.25
    },
    'Bakery': {
        'Croissant': 3.75,
        'Blueberry Muffin': 3.50,
        'Chocolate Chip Cookie': 2.50,
        'Bagel': 3.00,
        'Scone': 3.75
    },
    'Food': {
        'Avocado Toast': 8.50,
        'Breakfast Sandwich': 7.50,
        'Grilled Cheese': 6.50
    }
}

# Flatten product list for easier selection
product_list = []
for category, items in products.items():
    for item, price in items.items():
        product_list.append({'Item': item, 'Category': category, 'Price': price})

# Simulation parameters
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)
num_transactions = 5000  # Number of transactions to simulate

data = []

customer_types = ['Regular', 'New', 'Transient']
payment_methods = ['Credit Card', 'Cash', 'Mobile Payment']

print(f"Generating transactions...")

transaction_id = 1000

current_date = start_date
while current_date <= end_date:
    # Randomize number of transactions per day (more on weekends maybe? lets keep it simple normal distro)
    daily_transactions = int(random.normalvariate(50, 15)) # Avg 50 transactions/day
    daily_transactions = max(10, daily_transactions) # Minimum 10

    for _ in range(daily_transactions):
        # Generate Time (Peak morning hours 7-10, Lunch 12-2, Afternoon 3-5)
        hour = random.choices(
            population=[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            weights=[10, 15, 20, 15, 10, 12, 10, 8, 10, 8, 5, 3, 2],
            k=1
        )[0]
        minute = random.randint(0, 59)
        transaction_time = f"{hour:02d}:{minute:02d}"
        
        # Select Product
        # Coffee is more popular
        prod = random.choices(product_list, weights=[1.5 if p['Category']=='Coffee' else 1.0 for p in product_list], k=1)[0]
        
        # Quantity (mostly 1, sometimes 2 or 3)
        qty = random.choices([1, 2, 3], weights=[80, 15, 5], k=1)[0]
        
        # Payment & Customer
        pay_method = random.choices(payment_methods, weights=[60, 20, 20], k=1)[0]
        cust_type = random.choices(customer_types, weights=[50, 30, 20], k=1)[0]

        data.append({
            'Transaction ID': transaction_id,
            'Date': current_date.strftime('%Y-%m-%d'),
            'Time': transaction_time,
            'Item': prod['Item'],
            'Category': prod['Category'],
            'Price': prod['Price'],
            'Quantity': qty,
            'Total Spent': prod['Price'] * qty,
            'Payment Method': pay_method,
            'Customer Type': cust_type
        })
        transaction_id += 1
    
    current_date += timedelta(days=1)

# Create DataFrame and Save
df = pd.DataFrame(data)
csv_file = 'coffee_shop_sales.csv'
df.to_csv(csv_file, index=False)

print(f"Data generation complete. Saved to {csv_file}")
print(f"Total records: {len(df)}")
