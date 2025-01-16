import pandas as pd

df = pd.read_csv('csv files/BalanceSheetSummaries.xls.csv')

# Check for missing data
missing_data = df.isnull().sum()
total_cells = df.size
total_missing = missing_data.sum()

# Percentage of missing data
percent_missing = (total_missing / total_cells) * 100
print(f"Total missing data: {total_missing} cells")
print(f"Percentage of missing data: {percent_missing:.2f}%")

# Display missing data per column
print("Missing data per column:")
print(missing_data)

# Since total liabilities is the only column with missing entries, we remove it entirely
# Drop the 'Total Liabilities(2)' column
df_cleaned = df.drop(columns=['Total Liabilities(2)'])
print("'Total Liabilities(2)' column removed.")

# Save the cleaned data to a new CSV file
output_file = 'csv files/step1.csv'
df_cleaned.to_csv(output_file, index=False)
print(f"Cleaned data saved to {output_file}")
