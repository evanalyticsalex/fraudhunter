import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the raw CSV from the correct path
df = pd.read_csv('../data/ecommerce.csv')

# If 'customer_since' exists and is a string, convert to datetime
if 'customer_since' in df.columns and df['customer_since'].dtype == 'object':
    df['customer_since'] = pd.to_datetime(df['customer_since'], errors='coerce')

# Handle missing values (optional but recommended for correlation)
if 'avg_order_value' in df.columns:
    df['avg_order_value'].fillna(df['avg_order_value'].median(), inplace=True)

# Select numeric columns only
numeric_df = df.select_dtypes(include=['number'])

# Compute correlation matrix
corr_matrix = numeric_df.corr()

# Print correlation values
print("📈 Correlation Matrix:")
print(corr_matrix)

# Save to CSV for future reference
corr_matrix.to_csv('../data/correlation_matrix.csv', index=True)

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Matrix - E-Commerce Dataset")
plt.tight_layout()
plt.show()
