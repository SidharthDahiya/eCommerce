# eCommerce Customer Analytics Suite

Welcome to the eCommerce Customer Analytics Suite, a comprehensive project that integrates three core data science tasks:
- **Exploratory Data Analysis (EDA) & Business Insights**
- **Lookalike Modeling**
- **Customer Segmentation / Clustering**

## Project Overview

This project uses an eCommerce Transactions dataset composed of three files:
- **Customers.csv**: Contains customer ID, name, region, and signup date.
- **Products.csv**: Contains product ID, name, category, and price.
- **Transactions.csv**: Contains transaction details including transaction ID, customer ID, product ID, date, quantity, price, and total value.

## 🚀 Project Components

### 1. Exploratory Data Analysis (EDA) & Business Insights
- Performed a thorough EDA by merging the customer, product, and transaction data.
- Derived over 5 actionable insights (e.g., revenue trends by region, product performance, and customer lifetime value improvements).
- Insights are documented concisely in a PDF report with each insight summarized in under 100 words.

### 2. Lookalike Model
- Built a lookalike model to recommend the top 3 similar customers for a given user based on profile and transaction history.
- The model uses both customer and product data to compute a similarity score.
- Generated recommendations for the first 20 customers (CustomerID: C0001-C0020) and compiled the outputs in a CSV file (Lookalike.csv).

### 3. Customer Segmentation / Clustering
- Implemented clustering techniques by combining data from Customers.csv and Transactions.csv.
- Experimented with clustering algorithms (e.g., DBSCAN, k-means) to identify distinct customer segments.
- Reported key clustering metrics including the number of clusters formed (e.g., 6 clusters) and DB Index (e.g., 0.48).
- Visualizations are provided to illustrate cluster distributions and separation.


## 🚀 Usage

- **EDA**: Run the `EDA.ipynb` notebook to perform data analysis and generate business insights.
- **Lookalike Model**: Execute the `Lookalike_Model.ipynb` notebook to compute similarity scores and generate recommended customer matches.
- **Clustering**: Run the `Clustering.ipynb` notebook to perform customer segmentation and visualize clusters.

## 🔍 Key Results and Metrics

- **Business Insights**: Extracted and documented actionable insights that drive strategic decisions.
- **Lookalike Model**: Provided the top 3 lookalike recommendations for each customer (C0001-C0020) with associated similarity scores.
- **Customer Clustering**:
- **Number of Clusters**: 6 (example)
- **DB Index**: 0.48 (example)

| Model Component      | Metric              | Value  |
|----------------------|---------------------|--------|
| Lookalike Model      | Average Similarity  | 0.89   |
| Customer Clustering  | DB Index            | 0.48   |

## 🔧 Technologies Used

- **Data Processing**: Python, Pandas, NumPy
- **Machine Learning**: Scikit-Learn, XGBoost
- **Visualization**: Matplotlib, Seaborn
- **Interactive Development**: Jupyter Notebook

## 💡 Project Philosophy

Empowering businesses with data-driven insights that bridge raw transactional data with actionable strategies for enhanced customer engagement and revenue growth.


