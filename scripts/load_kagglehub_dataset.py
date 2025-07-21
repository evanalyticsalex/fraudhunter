import kagglehub
import pandas as pd
import os

print("📦 Starting KaggleHub download...")

try:
    # Step 1: Download dataset using kagglehub
    dataset_path = kagglehub.dataset_download(
        "sahilislam007/e-commerce-customer-analytics-loyalty-vs-fraud"
    )

    print("✅ Dataset downloaded to:", dataset_path)

    # Step 2: Load the correct CSV file manually
    csv_file = os.path.join(dataset_path, "synthetic_ecommerce_churn_dataset.csv")
    df = pd.read_csv(csv_file)

    print("✅ Dataset loaded successfully")
    print(df.head())
    # Step 3: Save to project-root /data/ecommerce.csv
    save_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "ecommerce.csv")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"💾 Saved to {save_path}")


except Exception as e:
    print("❌ Error occurred:", e)
