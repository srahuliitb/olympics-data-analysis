# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Step 1
# Data Loading 
data = pd.read_csv(path)
data.rename(columns = {'Total' : 'Total_Medals'}, inplace = True)
print(data.head(10))

# Step 2
# Summer or Winter
def map(df):
    new_list = []
    for i in df.index.values:
        if df['Total_Summer'][i] > df['Total_Winter'][i]:
            new_list.append('Summer')
        elif df['Total_Summer'][i] < df['Total_Winter'][i]:
            new_list.append('Winter')
        else:
            new_list.append('Both')
    return pd.Series(new_list, index = df.index.values)

data['Better_Event'] = map(data)
better_event = data['Better_Event'].value_counts().index[0]

# Step 3
# Top 10
top_countries = data[['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']]
top_countries = top_countries[:-1]

def top_ten(df, col):
    top_10 = df.nlargest(10, col)
    return list(top_10['Country_Name'])

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
# print("Top 10 Summer", top_10_summer)
# print("Top 10 Winter", top_10_winter)
# print("Top 10", top_10)

common = [c for c in top_10_summer if (c in top_10_winter) and (c in top_10)]
print(common)

# Step 4
# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind = 'bar', x = 'Country_Name', y = 'Total_Summer')
winter_df.plot(kind = 'bar', x = 'Country_Name', y = 'Total_Winter')
top_df.plot(kind = 'bar', x = 'Country_Name', y = 'Total_Medals')

# Step 5
# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio, summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(), ['Golden_Ratio', 'Country_Name']]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio, winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(), ['Golden_Ratio', 'Country_Name']]

top_df['Golden_Ratio'] = round(top_df['Gold_Total'] / top_df['Total_Medals'], 2)
top_max_ratio, top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(), ['Golden_Ratio', 'Country_Name']]

# Step 6
# Best in the world 
data_1 = data[:-1]
data_1['Total_Points'] = 3 * data_1['Gold_Total'] + 2 * data_1['Silver_Total'] + data_1['Bronze_Total']
most_points, best_country = data_1.loc[data_1['Total_Points'].idxmax(), ['Total_Points', 'Country_Name']]

# Step 7
# Plotting the best
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked = True)
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation = 45)



