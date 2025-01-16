import pandas as pd

data = pd.read_csv('csv files/step2.csv')

# Function to find columns with a lot of zero values
def find_zero_columns(df, threshold=0.5):
    """
    This function finds columns in the DataFrame that have a high percentage of zero values.
    
    Parameters:
    - df: The input DataFrame
    - threshold: The threshold percentage of zeros (default is 50%)
    
    Returns:
    - zero_columns: A DataFrame with columns having a high percentage of zeros
    """
    # Calculate the percentage of zero values in each column
    zero_percentage = (df == 0).mean()

    # Filter columns based on the threshold
    zero_columns = zero_percentage[zero_percentage > threshold].index.tolist()
    
    return zero_columns

# Find columns with more than 50% zeros
zero_columns = find_zero_columns(data, threshold=0.5)

# Output the results
print("Columns with more than 50% zero values:")
for col in zero_columns:
    print(f"{col}: {data[col].isnull().sum()} nulls and {((data[col] == 0).mean() * 100):.2f}% zeros")

# based on this i remove the columns that contain more than 50 percent zeroes
# Remove those columns from the original DataFrame
cleaned_data = data.drop(columns=zero_columns)

# Sort by Total Assets and save to a new CSV file
sorted_by_total_assets = cleaned_data.sort_values(by='Total Assets', ascending=False)  # Sort in descending order
sorted_by_total_assets.to_csv('csv files/step3_total_assets.csv', index=False)
print("Data sorted by Total Assets and saved to 'step3_total_assets.csv'.")

# Sort by Net Worth (Deficit) and save to a new CSV file
sorted_by_net_worth = cleaned_data.sort_values(by='Net Worth (Deficit)')
sorted_by_net_worth.to_csv('csv files/step3_net_worth.csv', index=False)
print("Data sorted by Net Worth (Deficit) and saved to 'step3_net_worth.csv'.")

# Filtering the DataFrame based on 'Net Worth (Deficit)' threshold of -75,000
filtered_data = sorted_by_net_worth[sorted_by_net_worth['Net Worth (Deficit)'] > -75000]

# Save the filtered data to a new CSV file
filtered_data.to_csv('csv files/step3_more_75.csv', index=False)
print("Data filtered by 'Net Worth (Deficit)' (threshold: -75,000) and saved to 'step3_more_75.csv'.")

# Save the rest of the data (Net Worth <= -75,000) to a separate CSV file
remaining_data = sorted_by_net_worth[sorted_by_net_worth['Net Worth (Deficit)'] <= -75000]
remaining_data.to_csv('csv files/step3_less_75.csv', index=False)
print("Remaining data (Net Worth <= -75,000) saved to 'step3_less_75.csv'.")

# Output the results
print("Removed columns with more than 50% zero values:")
