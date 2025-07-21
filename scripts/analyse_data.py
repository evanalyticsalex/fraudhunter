import os
import glob
import pandas as pd

# Step 1: Get current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Step 2: Navigate to the data folder (one level up)
data_folder = os.path.join(current_dir, '..', 'data')

# Step 3: Find all CSV files in that folder
csv_files = glob.glob(os.path.join(data_folder, '*.csv'))

# Step 4: Handle no CSV found
if len(csv_files) == 0:
    raise FileNotFoundError(f"No CSV files found in {data_folder}")

# Step 5: Pick the first CSV
csv_path = csv_files[0]

# Step 6: Load into DataFrame
df = pd.read_csv(csv_path)

# Step 7: Preview
print(f"✅ Loaded: {csv_path}")
print("\n📊 First 5 rows:\n", df.head())
print("\n📏 Shape:", df.shape)
print("\n🧠 Columns:", df.columns.tolist())
