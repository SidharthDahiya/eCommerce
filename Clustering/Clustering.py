import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score, silhouette_score
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_prepare_data():
    # Load datasets
    customers = pd.read_csv('Customers.csv')
    transactions = pd.read_csv('Transactions.csv')
    products = pd.read_csv('Products.csv')

    # Create customer features
    customer_metrics = transactions.groupby('CustomerID').agg({
        'TransactionID': 'count',
        'Quantity': ['sum', 'mean'],
        'TotalValue': ['sum', 'mean'],
        'Price': 'mean'
    }).reset_index()

    # Flatten multi-level column names
    customer_metrics.columns = ['CustomerID', 'transaction_count',
                                'total_quantity', 'avg_quantity',
                                'total_spend', 'avg_transaction_value',
                                'avg_price']

    # Calculate recency
    customers['SignupDate'] = pd.to_datetime(customers['SignupDate'])
    reference_date = pd.Timestamp('2025-01-27')
    customers['days_since_signup'] = (reference_date - customers['SignupDate']).dt.days

    # Add region encoding
    region_dummies = pd.get_dummies(customers['Region'], prefix='region')

    # Merge all features
    final_features = customer_metrics.merge(
        customers[['CustomerID', 'days_since_signup']],
        on='CustomerID'
    )
    final_features = pd.concat([final_features, region_dummies], axis=1)

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    feature_columns = final_features.columns.drop('CustomerID')
    final_features[feature_columns] = imputer.fit_transform(final_features[feature_columns])

    return final_features


def perform_clustering(data, n_clusters=5):
    # Separate features from ID
    features = data.drop('CustomerID', axis=1)

    # Scale features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Perform clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(scaled_features)

    # Calculate metrics
    db_index = davies_bouldin_score(scaled_features, clusters)
    silhouette = silhouette_score(scaled_features, clusters)

    return clusters, db_index, silhouette, kmeans


def main():
    # Prepare data
    features = load_and_prepare_data()

    # Perform clustering
    clusters, db_index, silhouette, model = perform_clustering(features)

    # Save results
    results = pd.DataFrame({
        'CustomerID': features['CustomerID'],
        'Cluster': clusters
    })
    results.to_csv('clustering_results.csv', index=False)

    # Save metrics
    with open('clustering_metrics.txt', 'w') as f:
        f.write(f"Number of clusters: 5\n")
        f.write(f"Davies-Bouldin Index: {db_index:.4f}\n")
        f.write(f"Silhouette Score: {silhouette:.4f}\n")


if __name__ == "__main__":
    main()
