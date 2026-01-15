import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_theme(style="whitegrid")

# Create output directory for plots
output_dir = 'visualizations'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1. Load Data
print("Loading data...")
try:
    df = pd.read_csv('coffee_shop_sales.csv')
except FileNotFoundError:
    print("Error: coffee_shop_sales.csv not found. Please run generate_data.py first.")
    exit()

# Convert Date and Time to datetime objects
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour

print(f"Data Loaded: {df.shape[0]} records, {df.shape[1]} columns.")

# --- DEEP ANALYSIS ---

print("\n--- DEEP ANALYSIS ---")

# 1. Financials
total_revenue = df['Total Spent'].sum()
avg_transaction_value = df['Total Spent'].mean()
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Average Transaction Value: ${avg_transaction_value:.2f}")

# 2. Top Performing Products
top_items_qty = df.groupby('Item')['Quantity'].sum().sort_values(ascending=False).head(5)
top_items_rev = df.groupby('Item')['Total Spent'].sum().sort_values(ascending=False).head(5)

print("\nTop 5 Items by Quantity Sold:")
print(top_items_qty)
print("\nTop 5 Items by Revenue:")
print(top_items_rev)

# 3. Category Performance
category_sales = df.groupby('Category')['Total Spent'].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(category_sales)

# 4. Hourly Peak Analysis
peak_hour = df.groupby('Hour')['Transaction ID'].count().idxmax()
print(f"\nPeak Hour for Transactions: {peak_hour}:00")

# --- VISUALIZATIONS ---

print("\n--- GENERATING VISUALIZATIONS ---")

# Plot 1: Monthly Revenue Trend
plt.figure(figsize=(12, 6))
monthly_sales = df.groupby('Month')['Total Spent'].sum()
monthly_sales.index = monthly_sales.index.astype(str) # Convert PeriodIndex to string for plotting
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', color='b')
plt.title('Monthly Revenue Trend (2025)')
plt.xlabel('Month')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{output_dir}/1_monthly_revenue_trend.png')
print(f"Saved: {output_dir}/1_monthly_revenue_trend.png")
plt.close()

# Plot 2: Sales by Category
plt.figure(figsize=(10, 6))
sns.barplot(x=category_sales.index, y=category_sales.values, hue=category_sales.index, palette='viridis', legend=False)
plt.title('Total Revenue by Product Category')
plt.xlabel('Category')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.savefig(f'{output_dir}/2_sales_by_category.png')
print(f"Saved: {output_dir}/2_sales_by_category.png")
plt.close()

# Plot 3: Hourly Transaction Volume
plt.figure(figsize=(12, 6))
hourly_counts = df.groupby('Hour')['Transaction ID'].count()
sns.barplot(x=hourly_counts.index, y=hourly_counts.values, hue=hourly_counts.index, palette='coolwarm', legend=False)
plt.title('Hourly Transaction Volume')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Transactions')
plt.tight_layout()
plt.savefig(f'{output_dir}/3_hourly_transactions.png')
print(f"Saved: {output_dir}/3_hourly_transactions.png")
plt.close()

# Plot 4: Top 10 Items by Quantity
plt.figure(figsize=(12, 6))
top_10_items = df.groupby('Item')['Quantity'].sum().sort_values(ascending=False).head(10)
sns.barplot(y=top_10_items.index, x=top_10_items.values, hue=top_10_items.index, palette='magma', orient='h', legend=False)
plt.title('Top 10 Best-Selling Items (Quantity)')
plt.xlabel('Quantity Sold')
plt.ylabel('Item')
plt.tight_layout()
plt.savefig(f'{output_dir}/4_top_selling_items.png')
print(f"Saved: {output_dir}/4_top_selling_items.png")
plt.close()

# Plot 5: Payment Method Distribution
plt.figure(figsize=(8, 8))
payment_counts = df['Payment Method'].value_counts()
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=140)
plt.title('Payment Method Distribution')
plt.tight_layout()
plt.savefig(f'{output_dir}/5_payment_distribution.png')
print(f"Saved: {output_dir}/5_payment_distribution.png")
plt.close()

print("\nAnalysis Complete. Visualizations saved in 'visualizations/' folder.")
