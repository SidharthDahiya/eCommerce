import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


def create_lookalike_model():
    # Load datasets
    customers = pd.read_csv('Customers.csv')
    transactions = pd.read_csv('Transactions.csv')
    products = pd.read_csv('Products.csv')

    # Create customer features
    # 1. Calculate customer purchase metrics
    customer_metrics = transactions.groupby('CustomerID').agg({
        'TransactionID': 'count',  # Number of transactions
        'Quantity': 'sum',  # Total quantity purchased
        'TotalValue': 'sum',  # Total spend
        'ProductID': 'nunique'  # Unique products bought
    }).reset_index()

    # 2. Get category preferences
    trans_products = transactions.merge(products, on='ProductID')
    category_preferences = pd.crosstab(
        trans_products['CustomerID'],
        trans_products['Category']
    ).reset_index()

    # 3. Combine features
    customer_features = customer_metrics.merge(category_preferences, on='CustomerID')

    # 4. Add signup year and region encoding
    customers['SignupYear'] = pd.to_datetime(customers['SignupDate']).dt.year
    region_dummies = pd.get_dummies(customers['Region'], prefix='Region')
    customer_features = customer_features.merge(
        customers[['CustomerID', 'SignupYear']],
        on='CustomerID'
    )
    customer_features = customer_features.merge(
        region_dummies,
        left_index=True,
        right_index=True
    )

    # Normalize features
    scaler = StandardScaler()
    feature_columns = customer_features.columns.drop('CustomerID')
    customer_features[feature_columns] = scaler.fit_transform(
        customer_features[feature_columns]
    )

    # Calculate similarity matrix
    similarity_matrix = cosine_similarity(
        customer_features[feature_columns]
    )

    # Create recommendations dictionary
    recommendations = {}
    customer_ids = customer_features['CustomerID'].tolist()

    for i, target_id in enumerate(customer_ids[:20]):  # First 20 customers
        similarities = similarity_matrix[i]
        # Get top 3 similar customers (excluding self)
        similar_indices = np.argsort(similarities)[-4:][::-1]
        similar_customers = []

        for idx in similar_indices[1:]:  # Skip first (self)
            similar_customers.append({
                'customer_id': customer_ids[idx],
                'similarity_score': round(similarities[idx], 4)
            })

        recommendations[target_id] = similar_customers

    # Create CSV output
    output_rows = []
    for cust_id, lookalikes in recommendations.items():
        lookalike_str = "|".join([
            f"{rec['customer_id']},{rec['similarity_score']}"
            for rec in lookalikes
        ])
        output_rows.append([cust_id, lookalike_str])

    output_df = pd.DataFrame(
        output_rows,
        columns=['CustomerID', 'Lookalikes']
    )
    output_df.to_csv('Lookalike.csv', index=False)

    return recommendations


# Run the model
lookalike_recommendations = create_lookalike_model()

# Print recommendations for first 20 customers
for cust_id, recs in lookalike_recommendations.items():
    print(f"\nCustomer {cust_id} lookalikes:")
    for rec in recs:
        print(f"- {rec['customer_id']}: {rec['similarity_score']}")
