import pandas as pd

# Load dataset
df = pd.read_csv('datasets/sample_dataset.csv')

# Clean up: drop duplicates, fill missing, standardize text
df = df.drop_duplicates()
df['name'] = df['name'].str.title()
df['score'] = df['score'].fillna(df['score'].mean())

# Save cleaned dataset
df.to_csv('datasets/cleaned_dataset.csv', index=False)
print("Dataset cleaned and saved!")
