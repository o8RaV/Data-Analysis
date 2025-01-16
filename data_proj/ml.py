import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import  LabelEncoder
from sklearn.model_selection import train_test_split

data = pd.read_csv('step3_net_worth.csv')

 # Data Preperation
data['year'] = pd.to_datetime(data['Failure Date'], errors='coerce').dt.year.astype('Int64')
data['Year_Binned'] = pd.cut(data['year'], bins=[2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2017, 2019, 2020], include_lowest=True)
data['Year_Binned'] = LabelEncoder().fit_transform(data['Year_Binned'])

target = data['FDIC Subrogated Claim']

data = data.drop(columns=['year', 'Fund Code', 'Receivership', 'Failure Date', 'FDIC Subrogated Claim %', 'Subtotal - Proven Deposit Claims %', 'Dividends Paid to Date %', 'Total Unpaid Deposit Claims %', 'General Creditor %', 'Subtotal- Other Claimants %', 'Total Unpaid Other Claimants %', 'FDIC Subrogated Claim','FDIC Subrogated Deposit Claim', 'Year', 'Quarter'])

# Data Information
print(data.head(), data.describe(), data.info())

# Train Test Split
x_train, x_test, t_train, t_test = train_test_split(data, target, test_size=0.33, random_state=42)

# Training LR
lr_model = LinearRegression()
lr_model.fit(x_train, t_train)

# Scoring
score1 = lr_model.score(x_train, t_train)
score = lr_model.score(x_test, t_test)
print(score1, score)

# Evaluation
y_pred = lr_model.predict(x_test)
lr_rmse = root_mean_squared_error(t_test, y_pred)  # Root Mean Squared Error
lr_mae = mean_absolute_error(t_test, y_pred)  # Mean Absolute Error
lr_r2 = r2_score(t_test, y_pred)  # R-squared
print(lr_rmse, lr_mae, lr_r2)
