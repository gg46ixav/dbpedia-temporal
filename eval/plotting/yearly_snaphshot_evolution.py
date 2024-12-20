import pandas as pd
import os
import matplotlib.pyplot as plt

# Directory where the folders are stored
base_dir = '/home/marvin/workspace/data/dbpedia-tkg/stats_1217_1825/FULL/SNAP'

# List to store dataframes
dataframes = []

# Traverse each folder in the base directory
for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    
    # Check if it's a directory
    if os.path.isdir(folder_path):
        summary_path = os.path.join(folder_path, 'summary')
        
        # Locate CSV file in the summary subdirectory
        for file in os.listdir(summary_path):
            if file.endswith('.csv'):
                csv_path = os.path.join(summary_path, file)
                
                # Load CSV into a dataframe
                df = pd.read_csv(csv_path)
                
                # Add a new column with the folder name (date)
                df['date'] = folder
                
                # Append dataframe to the list
                dataframes.append(df)

# Concatenate all dataframes into a single dataframe
final_df = pd.concat(dataframes, ignore_index=True)

# Display the resulting dataframe

# Convert to DataFrame and ensure 'date' is datetime
df = final_df
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

specific_date = pd.to_datetime('2000-06-01')
specific_date2 = pd.to_datetime('2025-06-01')
# Filter out rows where date equals specific_date
df = df[df['date'] != specific_date]
df = df[df['date'] != specific_date2]

df2 = pd.read_csv("/home/marvin/workspace/data/dbpedia-tkg/stats_1217_1825/FULL/yearlyTripleDiffStats/part-00000-f1c15373-69e3-4607-9a39-fba4e6e75b58-c000.csv")

df2['prevYear'] = pd.to_datetime(df2['prevYear'].astype(str) + '-06-01')
df2['currYear'] = pd.to_datetime(df2['currYear'].astype(str) + '-06-01')


# Filter out rows where date equals specific_date
df2 = df2[df2['currYear'] != specific_date2]


# Plot with separate y-axis for df2 data
fig, ax1 = plt.subplots(figsize=(6, 4))

# displayLeftColumns = ['triples', 'distTriples', 'distEntities', 'distTypes', 'disRelations', 'distVersions']
displayLeftColumns = ['triples', 'distEntities', 'distTypes', 'disRelations', 'distVersions']
# displayLeftColumnsLabels = ['Triples', 'Unique Triples', 'Unique Entities', 'Unique Types', 'Unique Relations', 'Unique Versions']
displayLeftColumnsLabels = ['Triples', 'Unique Entities', 'Unique Types', 'Unique Relations', 'Unique Versions']
# Primary y-axis for df1
for column in displayLeftColumns:
    ax1.plot(df['date'], df[column], label=displayLeftColumnsLabels[displayLeftColumns.index(column)])

ax1.set_xlabel('Date')
ax1.set_yscale('log')
ax1.set_ylabel('Total Values', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Secondary y-axis for df2
# ax2 = ax1.twinx()

# # displayRightColumns =  ['prevSize', 'currSize', 'addCount', 'delCount']
# displayRightColumns =  [ 'addCount', 'delCount']
# # displayRightColumnsLabels = ['Previous Size', 'Current Size', 'Added Triples', 'Deleted Triples']
# displayRightColumnsLabels = [ 'Added Triples', 'Deleted Triples']
# for column in displayRightColumns:
#     ax2.plot(df2['currYear'], df2[column], '--', label=displayRightColumnsLabels[displayRightColumns.index(column)])

# ax2.set_ylabel('Diff Values (df2)', color='orange')
# ax2.tick_params(axis='y', labelcolor='orange')

# Combine legends from both axes
lines1, labels1 = ax1.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
ax1.legend(lines1, labels1, loc='upper left')


# Title and grid
plt.title('Snapshot Metrics and Aggregated Triple Changes Over Time')
plt.grid()
plt.tight_layout()

plt.savefig("snapshot_evolution.pdf", format="pdf", bbox_inches="tight")
