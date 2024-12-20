import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys

df = pd.read_csv(sys.argv[1])

df["name"] = df["head"].str.replace(r'.*/([^/]+)', r'\1', regex=True)

counts = df['name'].value_counts()


top_5_names = counts.nlargest(5).index
bottom_5_names = counts.nsmallest(5).index


# Combine top and bottom names into one set
selected_names = top_5_names # .union(bottom_5_names)


# selected_names = ["Berlin", "Madrid", "Rome", "Kyiv", "Paris"]
df = df[df['name'].isin(selected_names)]

# 3. Filter the dataframe to only include the selected names
df_filtered = df[df['name'].isin(selected_names)].copy()

df_filtered["date"] = pd.to_datetime(df_filtered['tFrom'], unit='s')


# Optional: If you have a large dataset, you might want to sort by date
df_filtered.sort_values(by='date', inplace=True)

df_filtered["value"] =  pd.to_numeric(df_filtered["tail"].str.replace(r'\\(\d+).*', r'\1', regex=True), errors='coerce')



def remove_outliers_iqr(group):
    Q1 = group['value'].quantile(0.25)
    Q3 = group['value'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return group[(group['value'] >= lower_bound) & (group['value'] <= upper_bound)]


df_filtered = df_filtered[["name","value","date"]]

with pd.option_context('display.max_rows', None):  # more options can be specified also
    print(df_filtered[["name","date","value"]])

# print(df_filtered)


df_filtered = df_filtered.groupby('name', group_keys=False).apply(remove_outliers_iqr)

df_filtered.sort_values(by="date", inplace=True)

# 4. Plotting
# We'll use a line plot of value over time, with one line per name.
plt.figure(figsize=(6, 4))

# Group the filtered DataFrame by 'name'
for name, group_data in df_filtered.groupby('name'):
    plt.plot(group_data['date'], group_data['value'], label=name)
    
plt.xlabel('Date')
plt.ylabel('Value')
plt.tick_params(axis='x', rotation=45)
plt.title('Entity Changes for: ' + sys.argv[3])
plt.legend()
# plt.grid(True)
plt.tight_layout()
plt.savefig(sys.argv[2], format='pdf', bbox_inches='tight')