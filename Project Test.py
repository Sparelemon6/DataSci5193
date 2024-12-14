import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

# # Read Physician info by county
# df_phys = pd.read_excel('C:/Users/Ryan/PycharmProjects/Final Project/2024_county_health_release_oklahoma_data_-_v1 (2).xlsx', sheet_name='Select Measure Data')
#
# # Select the desired rows and columns
# df_phys = df_phys.iloc[2:81, [0, 2, 134, 135, 136, 137]]  # Assuming EE, EF, EG, EH
# # Print the selected DataFrame
# # print(df_phys)
#
#
# # Read Health Outcomes
# df_outcomes= pd.read_excel('C:/Users/Ryan/PycharmProjects/Final Project/2024_county_health_release_oklahoma_data_-_v1 (2).xlsx', sheet_name='Health Outcomes & Factors')
#
# # Select the desired rows and columns
# df_outcomes = df_outcomes.iloc[2:81, [3, 4, 5, 6]]  # Health Outcomes and Health Factors (Z-score and ranges)
#
# # print(df_outcomes)
#
# ###############################################
# ### Combine Physician data and Outcome data ###
#
# df = pd.concat([df_phys, df_outcomes], axis=1)
#
# # Rename Columns
# df.columns = ['FIPS', 'County', 'PCP', 'PCP per 100k', 'PCP Ratio','PCP z-score','Outcomes','OutcomesRange','Factors','FactorsRange']
# df = df.reset_index(drop=True)
# print('original df')
# print(df)
# df.to_csv(f"C:/Users/Ryan/PycharmProjects/Final Project/FirstCombined.csv", index=False, encoding='utf-8')
#
# df = df.reset_index(drop=True)
#
# # Basic scatter plot
# plt.scatter(df['Outcomes'], df['Factors'])
# plt.xlabel('Outcomes')
# plt.ylabel('Factors')
# plt.title('Scatter Plot')
# #plt.show()
#
# print('Correlation for Outcomes vs Factors')
# # Pearson correlation coefficient
# correlation = df['Outcomes'].corr(df['Factors'])
# print('Pearson correlation coefficient:', correlation)
#
# # Spearman correlation coefficient (for non-linear relationships)
# correlation_spearman = df['Outcomes'].corr(df['Factors'], method='spearman')
# print('Spearman correlation coefficient:', correlation_spearman)
#
# print()
# print('Correlation for PCP per 100k vs Outcomes')
# # Pearson correlation coefficient
# correlation = df['PCP per 100k'].corr(df['Outcomes'])
# print('Pearson correlation coefficient:', correlation)
#
# # Spearman correlation coefficient (for non-linear relationships)
# correlation_spearman = df['PCP per 100k'].corr(df['Outcomes'], method='spearman')
# print('Spearman correlation coefficient:', correlation_spearman)
#
#
#
# df_sooner = pd.read_excel('C:/Users/Ryan/PycharmProjects/Final Project/Expenditure by County.xlsx', sheet_name='Sheet1')
#
# # Select the desired rows and columns
# df_sooner = df_sooner.iloc[0:79, [1, 2, 3, 4, 5, 6]]
# print('next df')
# print(df_sooner)
#
# df2 = pd.concat([df, df_sooner], axis=1)
# print(df2)
# df2.to_csv(f"C:/Users/Ryan/PycharmProjects/Final Project/AllCombined.csv", index=False, encoding='utf-8')


###################################### health outcomes versus expenditures ###############################
# Adjust column indices to include the county column
df_sooner = pd.read_excel('C:/Users/Ryan/PycharmProjects/Final Project/Expenditure by County.xlsx', sheet_name='Sheet1')
df_outcomes = pd.read_excel('C:/Users/Ryan/PycharmProjects/Final Project/2024_county_health_release_oklahoma_data_-_v1 (2).xlsx', sheet_name='Health Outcomes & Factors',header=1)

# Check the structure of both DataFrames
print("Columns in df_sooner:", df_sooner.columns.to_list())
print("Columns in df_outcomes:", df_outcomes.columns.to_list())

# Standardize the 'County' column in both datasets
df_sooner['County'] = df_sooner['County'].str.strip().str.lower()
df_outcomes['County'] = df_outcomes['County'].str.strip().str.lower()

# Merge the datasets on 'County'
df_expenditure_vs_health = pd.merge(df_outcomes, df_sooner, on='County', how='inner')

# Display the merged dataset
print(df_expenditure_vs_health.head())

# Save the merged dataset to a file (optional)
df_expenditure_vs_health.to_csv('C:/Users/Ryan/PycharmProjects/Final Project/expenditure_vs_health.csv', index=False)


df3=df_expenditure_vs_health
# Convert relevant columns to numeric, removing commas and other non-numeric characters
df3['Expenditures'] = pd.to_numeric(df3['Expenditures'].str.replace(',', ''), errors='coerce')
df3['Annual Per Capita'] = pd.to_numeric(df3['Annual Per Capita'], errors='coerce')
df3['National Z-Score'] = pd.to_numeric(df3['National Z-Score'], errors='coerce')
df3['National Z-Score.1'] = pd.to_numeric(df3['National Z-Score.1'], errors='coerce')
df3['Monthly Avg Per Member'] = pd.to_numeric(df3['Monthly Avg Per Member'], errors='coerce')


print(df3.columns)

# Drop rows with missing data in key columns
#df_cleaned = df3.dropna(subset=['Expenditures', 'Annual Per Capita', 'National Z-Score', 'National Z-Score.1'])

#
# # Scatter plot: Expenditures vs National Z-Score
#
# #show county names next to data points
# top_counties = df3.nlargest(10, 'Monthly Avg Per Member')
# bottom_counties = df3.nsmallest(10, 'Monthly Avg Per Member')
# plt.figure(figsize=(12, 6))
# sns.regplot(x='Monthly Avg Per Member', y='National Z-Score', data=df3, scatter_kws={'alpha': 0.7}, line_kws={'color': 'red'},)
# for _, row in top_counties.iterrows():
#     plt.text(row['Monthly Avg Per Member'], row['National Z-Score'], row['County'], fontsize=10, color='blue')
# for _, row in bottom_counties.iterrows():
#     plt.text(row['Monthly Avg Per Member'], row['National Z-Score'], row['County'], fontsize=10, color='blue')
# plt.xlabel('Monthly Avg Per Member')
# plt.ylabel('National Z-Score (Health Outcomes)')
# plt.title('Monthly Avg Per Member vs Health Outcomes')
# plt.grid(True)
#
# # Format x-axis ticks to show million separators and reduce tick density
# ax = plt.gca()
# ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))  # Add commas for readability
# ax.xaxis.set_major_locator(plt.MaxNLocator(nbins=6))  # Limit to 6 ticks for less clutter
#
# plt.show()


