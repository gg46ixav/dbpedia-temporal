import pandas as pd
import matplotlib.pyplot as plt
import sys

df = pd.read_csv(sys.argv[1])
# df_pages = pd.read_csv(sys.argv[2])
output_file=sys.argv[3]

# Sort by cRev in ascending order
df_sorted = df.sort_values(by='cRev', ascending=True)
df_sorted['rank'] = range(1, len(df_sorted) + 1)

# Create a bar plot
plt.figure(figsize=(6,4))
plt.bar(df_sorted['rank'], df_sorted['cRev'], color='skyblue', edgecolor='skyblue')
plt.bar(df_sorted['rank'], df_sorted['cPage'], color='red', edgecolor='red')

# Add labels and title
plt.xlabel('Files')
plt.ylabel('Counts')
plt.title('Meta History Dump: Revision and Page File Distribution')

plt.legend(['Revision Count', 'Pages Count'])

# Rotate x-ticks for readability if needed
plt.xticks(rotation=45)

# Optional: Add grid
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.savefig(sys.argv[3], format="pdf", bbox_inches="tight")