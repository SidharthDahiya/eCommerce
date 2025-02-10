# eCommerce Customer Analytics Suite

Welcome to the eCommerce Customer Analytics Suite, a comprehensive project that performs data analysis and derives actionable insights for eCommerce businesses using Python. The project consists of three primary components:
- **Exploratory Data Analysis (EDA) & Business Insights**
- **Lookalike Modeling**
- **Clustering**

## Project Overview

This project utilizes an eCommerce dataset consisting of:
- **Customers.csv**: Customer information (ID, name, region, signup date)
- **Products.csv**: Product details (ID, name, category, price)
- **Transactions.csv**: Transaction data (ID, customer ID, product ID, date, quantity, total value)

## 🚀 Project Components

### 1. Exploratory Data Analysis (EDA) & Business Insights
**Process:**
- **Data Integration**: Merges customer, product, and transaction datasets using CustomerID/ProductID to create unified analysis base
- **Temporal Analysis**: Converts date fields (SignupDate/TransactionDate) to datetime format for trend analysis
- **Quality Assurance**: Performs data integrity checks through missing value analysis and statistical summaries
- **Visual Storytelling**: Generates 6+ key visualizations including customer demographics, product distribution, and sales trends

**Significance**: Establishes foundational understanding of business performance and customer behavior patterns.

**Results:**
- Total Revenue: $689,995.56
- Key Regional Insight: South America contributes 42% of total revenue
- Visual Outputs: `customer_distribution.png`, `monthly_sales.png`, etc. in plots/ folder
- Insights Report: `Business_Insights.pdf` with strategic recommendations

---

### 2. Lookalike Modeling
**Process:**
- **Feature Engineering**: Creates 15+ features including transaction frequency, spend patterns, and category preferences
- **Behavioral Encoding**: Uses one-hot encoding for regions and standard scaling for normalized comparisons
- **Similarity Framework**: Implements cosine similarity matrix for customer comparisons
- **Recommendation Engine**: Identifies top 3 matches excluding self-references

**Significance**: Enables targeted marketing by identifying high-value customer cohorts.

**Results:**
- Output File: `Lookalike.csv` with recommendations for first 20 customers
- Sample Recommendation:  
  `C0001: C0118 (0.8092), C0096 (0.7908), C0168 (0.7908)`
- Console Output: Printed recommendations with similarity scores

---

### 3. Customer Clustering
**Process:**
- **Feature Aggregation**: Creates 8 behavioral metrics including transaction count, avg spend, and recency
- **Data Sanitization**: Handles missing values through mean imputation
- **Dimensionality Management**: Applies StandardScaler for feature normalization
- **Cluster Optimization**: Uses KMeans with Davies-Bouldin Index for model evaluation

**Significance**: Reveals distinct customer segments for personalized engagement strategies.

**Results:**
- Cluster Assignments: `clustering_results.csv` with 5 customer segments
- Performance Metrics:  
  - Davies-Bouldin Index: 1.6716
  - Silhouette Score: 0.1976
- Cluster Characteristics: Saved in `clustering_metrics.txt`

## 📂 File Structure
```
eCommerce/
├── datasets/
│ ├── Customers.csv              # Customer demographics and signup data
│ ├── Products.csv               # Product catalog with categories and pricing
│ └── Transactions.csv           # Transaction records with timestamps
├── Exploratory Data Analysis (EDA) & Business Insights/
│   ├── EDA.py                   # Python script for EDA & generating business insights
│   ├── plots/                   # Folder containing generated visualizations
│   ├── Business_Insights.pdf    # Detailed business insights report
│   └── eda_insights.txt         # Text file summarizing key insights
├── Lookalike Model/
│   ├── Lookalike.py             # Python script for Lookalike Modeling
│   └── output.csv               # Lookalike model recommendations
├── Clustering/
│   ├── Clustering.py            # Python script for Customer Segmentation / Clustering analysis
│   ├── clustering_metrics.txt   # File containing clustering evaluation metrics
│   └── clustering_results.csv   # File containing clustering results

```
## 🔧 Technologies and Tools

- Python  
- Pandas, NumPy  
- Scikit-Learn  
- Matplotlib, Seaborn  

## 💡 Project Philosophy

This project bridges raw transactional data with actionable insights, enabling data-driven decision-making for enhanced customer engagement and revenue growth.
