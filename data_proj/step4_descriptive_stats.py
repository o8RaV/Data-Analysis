import pandas as pd

data = pd.read_csv('csv files/step3_net_worth.csv')

# Drop the 'year' and 'fund code' columns
data = data.drop(columns=['Year', 'Fund Code', 'Receivership', 'Quarter', 'Failure Date'], errors='ignore')

# Initialize a list to hold the results
statistics = {}

# Compute statistics for each numeric column
for column in data.columns:
    if pd.api.types.is_numeric_dtype(data[column]):  # Check if the column is numeric
        statistics[column] = {
            'Mean': data[column].mean(),
            'Median': data[column].median(),
            'Mode': data[column].mode()[0],
            'Standard Deviation': data[column].std(),
            'Variance': data[column].var(),
            'Range': [data[column].max(), data[column].min()],
            'Interquartile Range': [data[column].quantile(0.75), data[column].quantile(0.25)],
            'Skewness': data[column].skew()
        }
    else:
        print(f"Skipping non-numeric column: {column}")

# Convert statistics dictionary to a DataFrame
stats_df = pd.DataFrame(statistics).T

# Save the descriptive statistics to a text file with descriptive labels
with open('csv files/step4_descriptive_statz.txt', 'w') as f:  # Specify the filename
    # Write the explanation of skewness
    f.write("### Explanation of Skewness:\n")
    f.write("-Skewness is a measure of the asymmetry of the distribution of values in a dataset.\n")
    f.write("-A positive skew indicates that the tail on the right side of the distribution is longer or fatter than the left side, meaning there are a number of unusually high values.\n")
    f.write("-A negative skew indicates that the tail on the left side is longer or fatter than the right side, meaning there are a number of unusually low values.\n")
    f.write("-A skewness close to zero suggests that the distribution is symmetric.\n")
    f.write("\n") 
    
    # Add interpretations of skewness
    f.write("### Interpretations of Skewness:\n")
    f.write("-Highly negatively skewed: Skewness < -1\n")
    f.write("-Moderately negatively skewed: -1 < Skewness < -0.5\n")
    f.write("-Approximately symmetric: -0.5 < Skewness < 0.5\n")
    f.write("-Moderately positively skewed: 0.5 < Skewness < 1\n")
    f.write("-Highly positively skewed: Skewness > 1\n")
    f.write("\n") 

    for column, stats in stats_df.iterrows():
        f.write(f"Statistics for {column}:\n")
        for stat_name, value in stats.items():
            if isinstance(value, list):
                f.write(f"{stat_name}: {', '.join(map(str, value))}\n") 
            else:
                f.write(f"{stat_name}: {value:.2f}\n")
        
        # Add explanation of skewness for the current column
        skewness = stats['Skewness']
        if skewness < -1:
            f.write("Skewness Interpretation: Highly negatively skewed.\n")
        elif skewness < -0.5:
            f.write("Skewness Interpretation: Moderately negatively skewed.\n")
        elif skewness < 0.5:
            f.write("Skewness Interpretation: Approximately symmetric.\n")
        elif skewness < 1:
            f.write("Skewness Interpretation: Moderately positively skewed.\n")
        else:
            f.write("Skewness Interpretation: Highly positively skewed.\n")
        
        f.write("\n") 
