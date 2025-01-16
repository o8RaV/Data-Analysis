import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('step3_net_worth.csv')

# Sample 50 random rows
sampled_data = data.sample(n=50, random_state=1).reset_index(drop=True)
sampled_data_line = data.sample(n=20, random_state=1).reset_index(drop=True)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Set global font size for all plots
plt.rcParams.update({
    'font.size': 6,         # Set the base font size (adjust this as needed)
    'axes.titlesize': 10,   # Title font size
    'axes.labelsize': 8,    # X and Y label font size
    'xtick.labelsize': 7,   # X tick labels font size
    'ytick.labelsize': 7,   # Y tick labels font size
    'legend.fontsize': 8    # Legend font size
})

# Histogram
axs[0].hist(data['Total Assets'], bins=10, color='skyblue', edgecolor='black', density=True)
sns.kdeplot(data['Total Assets'], ax=axs[0], color='darkblue', linewidth=2)
axs[0].set_title('Histogram of Total Assets')
axs[0].set_xlabel('Total Assets')
axs[0].set_ylabel('Frequency')

# Boxplot
sns.boxplot(x=data['Total Assets'], ax=axs[1], color='lightcoral')
axs[1].set_title('Boxplot of Total Assets')
axs[1].set_xlabel('Total Assets')
plt.suptitle('Distribution of Total Assets')
plt.tight_layout()
plt.savefig('figures/multiple_subplots.png')
plt.show()

#Scattermatrix with correlations
plt.figure(figsize=(10, 10))
scatter_matrix(data[['Cash and Investments', 'Total Assets', 'Net Worth (Deficit)', 'FDIC Subrogated Deposit Claim']], alpha=0.5, diagonal='hist', figsize=(12, 12))
plt.suptitle('Scatter Matrix Showing Correlations')
plt.savefig('figures/scatter_matrix.png')
plt.show()

# Bar chart
plt.figure(figsize=(15, 9))
sns.barplot(y='Receivership', x='Dividends Paid to Date', data=sampled_data, color='m')
plt.title('Dividends Paid to Date by Receivership (Horizontal)')
plt.xlabel('Dividends Paid to Date')
plt.ylabel('Receivership')
plt.savefig('figures/horizontal_bar_chart.png')
plt.show()

# Scatterplot
plt.figure(figsize=(10, 5))
plt.scatter(data['Total Assets'], data['Net Worth (Deficit)'], c=data['Total Liabilities and Net Worth'], s=data['Total Liabilities and Net Worth']*0.01, alpha=0.6, cmap='viridis')
plt.title('Scatter Plot of Total Assets vs Net Worth (Deficit)')
plt.xlabel('Total Assets')
plt.ylabel('Net Worth (Deficit)')
plt.colorbar(label='Total Liabilities and Net Worth')
plt.savefig('figures/scatter_plot.png')
plt.show()

#Histogram
plt.figure(figsize=(10, 5))
plt.hist(data['Cash and Investments'], bins=20, color='g', edgecolor='black')
plt.title('Histogram of Cash and Investments')
plt.xlabel('Cash and Investments')
plt.ylabel('Frequency')
plt.savefig('figures/histogram.png')
plt.show()

# line chart
plt.figure(figsize=(10, 5))
plt.plot(sampled_data_line['Cash and Investments'], sampled_data_line['FDIC Subrogated Deposit Claim'], 
         marker='o', color='b', linestyle='-', label='Data Points')
for i, txt in enumerate(sampled_data_line['FDIC Subrogated Deposit Claim']):
    plt.text(sampled_data_line['Cash and Investments'].iloc[i], txt, f'{txt}', ha='right', va='bottom', fontsize=6)
z = np.polyfit(sampled_data_line['Cash and Investments'], sampled_data_line['FDIC Subrogated Deposit Claim'], 1)
p = np.poly1d(z)
plt.plot(sampled_data_line['Cash and Investments'], p(sampled_data_line['Cash and Investments']), 
         "r--", linewidth=2, label='Best Fit Line')
plt.title('FDIC Subrogated Deposit Claim Over Years')
plt.xlabel('Cash and Investments')
plt.ylabel('FDIC Subrogated Deposit Claim')
plt.grid(True)
plt.legend()
plt.savefig('figures/line_chart_with_best_fit_and_labels.png')
plt.show()
