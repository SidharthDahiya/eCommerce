import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

plt.style.use('seaborn-v0_8')


def load_and_prepare_data():
    customers = pd.read_csv('Customers.csv')
    products = pd.read_csv('Products.csv')
    transactions = pd.read_csv('Transactions.csv')

    # Convert dates to datetime
    customers['SignupDate'] = pd.to_datetime(customers['SignupDate'])
    transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])

    # Merge datasets
    merged_data = transactions.merge(customers, on='CustomerID').merge(products, on='ProductID')
    return customers, products, transactions, merged_data


def analyze_data_quality(merged_data):
    # Missing values analysis
    print("\nMissing Values Analysis:")
    print(merged_data.isnull().sum())

    # Basic statistics
    print("\nBasic Statistics:")
    print(merged_data.describe())

    # Data types
    print("\nData Types:")
    print(merged_data.dtypes)


def customer_analysis(customers, merged_data):
    plt.figure(figsize=(12, 6))

    # Customer distribution by region
    sns.countplot(data=customers, x='Region')
    plt.title('Customer Distribution by Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('customer_distribution.png')

    # Customer signup trend
    plt.figure(figsize=(12, 6))
    customers['SignupDate'].hist(bins=20)
    plt.title('Customer Signup Trend')
    plt.xlabel('Date')
    plt.ylabel('Number of Signups')
    plt.tight_layout()
    plt.savefig('signup_trend.png')


def product_analysis(products, merged_data):
    plt.figure(figsize=(12, 6))

    # Product category distribution
    sns.countplot(data=products, x='Category')
    plt.title('Product Distribution by Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('product_distribution.png')

    # Price distribution by category
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=products, x='Category', y='Price')
    plt.title('Price Distribution by Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('price_distribution.png')


def sales_analysis(merged_data):
    # Monthly sales trend
    monthly_sales = merged_data.groupby(merged_data['TransactionDate'].dt.to_period('M'))['TotalValue'].sum()

    plt.figure(figsize=(12, 6))
    monthly_sales.plot(kind='line', marker='o')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.tight_layout()
    plt.savefig('monthly_sales.png')

    # Top selling products
    top_products = merged_data.groupby('ProductName')['Quantity'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(12, 6))
    top_products.plot(kind='bar')
    plt.title('Top 10 Selling Products')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('top_products.png')


def purchase_patterns(merged_data):
    # Average order value by region
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=merged_data, x='Region', y='TotalValue')
    plt.title('Order Value Distribution by Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('order_value_distribution.png')

    # Quantity distribution
    plt.figure(figsize=(12, 6))
    merged_data['Quantity'].hist(bins=20)
    plt.title('Order Quantity Distribution')
    plt.xlabel('Quantity')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('quantity_distribution.png')


def generate_insights(merged_data):
    # Calculate key metrics
    total_revenue = merged_data['TotalValue'].sum()
    avg_order_value = merged_data['TotalValue'].mean()
    total_customers = merged_data['CustomerID'].nunique()
    total_products = merged_data['ProductID'].nunique()

    # Write insights to file
    with open('eda_insights.txt', 'w') as f:
        f.write("EDA Insights:\n\n")
        f.write(f"1. Total Revenue: ${total_revenue:,.2f}\n")
        f.write(f"2. Average Order Value: ${avg_order_value:.2f}\n")
        f.write(f"3. Total Unique Customers: {total_customers}\n")
        f.write(f"4. Total Products: {total_products}\n")
        f.write("5. Regional Performance: South America leads in customer base and revenue\n")
        f.write("6. Product Categories: Electronics and Books are top categories\n")
        f.write("7. Seasonal Trends: Peak sales observed in July and September\n")


def main():
    # Load and prepare data
    customers, products, transactions, merged_data = load_and_prepare_data()

    # Perform analyses
    analyze_data_quality(merged_data)
    customer_analysis(customers, merged_data)
    product_analysis(products, merged_data)
    sales_analysis(merged_data)
    purchase_patterns(merged_data)
    generate_insights(merged_data)

    plt.close('all')


if __name__ == "__main__":
    main()
