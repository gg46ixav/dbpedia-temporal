import pandas as pd
import matplotlib.pyplot as plt
import sys

df_revs = pd.read_csv(sys.argv[1])
df_pages = pd.read_csv(sys.argv[2])
output_file=sys.argv[3]

# Prepare data
all_revs = df_revs.groupby('year')['count'].sum().reset_index()
all_pages = df_pages.groupby('year')['count'].sum().reset_index()
# Separate namespace 0 and namespace 14
ns_0 = df_revs[df_revs['ns'] == 0].groupby('year')['count'].sum().reset_index()
ns_14 = df_revs[df_revs['ns'] == 14].groupby('year')['count'].sum().reset_index()

# Plot the data
fig, ax1 = plt.subplots(figsize=(6, 4))

ax1.set_xlabel('Year')
ax1.set_ylabel('New Pages', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Plot all pages marker='o'
ax1.plot(all_pages['year'], all_pages['count'], label='All New Pages (All NS)', linestyle='-', color='black')

ax2 = ax1.twinx()

# Plot all namespace, marker='o'
ax2.plot(all_revs['year'], all_revs['count'], label='All New Revisions (All NS)', linestyle='--')

# Plot namespace 0marker='s'
ax2.plot(ns_0['year'], ns_0['count'], label='New Article Revisions', linestyle='--')

# Plot namespace 14, marker='^'
ax2.plot(ns_14['year'], ns_14['count'], label='New Category Revisions', linestyle='-.')

ax2.set_ylabel('New Revisions', color='royalblue')
ax2.tick_params(axis='y', labelcolor='royalblue')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='best')

plt.title('Edits per Year for All, Articles and Category Pages')
# plt.legend()
plt.grid(True)
plt.tight_layout()

# Display plot
plt.savefig(output_file, format='pdf', bbox_inches='tight')