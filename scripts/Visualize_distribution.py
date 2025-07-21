import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the raw dataset
df = pd.read_csv('../data/ecommerce.csv')

# 🔹 Handle missing values (optional but helpful for visuals)
if 'avg_order_value' in df.columns:
    df['avg_order_value'].fillna(df['avg_order_value'].median(), inplace=True)

# Convert customer_since if needed
if 'customer_since' in df.columns and df['customer_since'].dtype == 'object':
    df['customer_since'] = pd.to_datetime(df['customer_since'], errors='coerce')

# ------------------------------------------------
# 🔸 1. HISTOGRAM of Age
# ------------------------------------------------
plt.figure(figsize=(8, 5))
df['age'].plot.hist(bins=20, edgecolor='black')
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ------------------------------------------------
# 🔸 2. BOXPLOT: Age vs Fraud
# ------------------------------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x='is_fraudulent', y='age', data=df)
plt.title('Customer Age by Fraud Status')
plt.xlabel('Is Fraudulent')
plt.ylabel('Age')
plt.tight_layout()
plt.show()

# ------------------------------------------------
# 🔸 3. GROUPBY: Average Order Value by Gender
# ------------------------------------------------
avg_by_gender = df.groupby('gender')['avg_order_value'].mean()

print("\n📊 Average Order Value by Gender:\n")
print(avg_by_gender)

# Optional: Bar chart for visual
plt.figure(figsize=(6, 4))
avg_by_gender.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Order Value by Gender')
plt.ylabel('Average Order Value ($)')
plt.xlabel('Gender')
plt.tight_layout()
plt.show()
