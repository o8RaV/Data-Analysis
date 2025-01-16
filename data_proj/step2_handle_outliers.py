import pandas as pd
import numpy as np

df = pd.read_csv('csv files/step1.csv')

# Function to cap outliers using IQR
def cap_outliers(df):
    for col in df.select_dtypes(include=[np.number]):
        Q1, Q3 = df[col].quantile([0.25, 0.75])
        IQR = Q3 - Q1
        lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
        df[col] = np.clip(df[col], lower, upper)
    return df

# Apply and save capped data
df_capped = cap_outliers(df)
df_capped.to_csv('csv files/step2.csv', index=False)

print("Outliers capped and saved.")
