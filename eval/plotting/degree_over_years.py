import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys

file_path=sys.argv[1]#"/home/marvin/workspace/data/dbpedia-tkg/stats_1217_1613/FULL/yearlyOutDegreeDistribution/part-00000-b56c3516-e455-4cab-a302-a390601b825c-c000.csv"
remove_outliers=False
scale_type="log"
output_file=sys.argv[2]

def filter_outliers(df, column):
    """
    Removes outliers from a DataFrame based on the IQR method for a specific column.

    Parameters:
    - df: The DataFrame.
    - column: The column to check for outliers.

    Returns:
    - A DataFrame with outliers removed.
    """
    q1 = df[column].quantile(0.25)  # 1st Quartile (25th percentile)
    q3 = df[column].quantile(0.75)  # 3rd Quartile (75th percentile)
    iqr = q3 - q1  # Interquartile Range
    upper_bound = q3 + 1.5 * iqr  # Upper fence

    return df[df[column] <= upper_bound]



try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    
# identify degree column and year column
if "in_degree" in data.columns:
    degree_col = "in_degree"
    year_col = "year"
elif "out_degree" in data.columns:
    degree_col = "out_degree"
    year_col = "year"
else:
    print(f"Skipping file {file_path}: Columns do not match expected 'degree' format.")
    
# Remove outliers from the degree column if specified
if remove_outliers:
    data = filter_outliers(data, degree_col)
# normalize years for a color gradient
years = data[year_col].unique()
cmap = plt.cm.coolwarm  # use a blue-to-red color map
# create scatter plot
plt.figure(figsize=(6, 4))
scatter = plt.scatter(
    data[degree_col],
    data["count"],
    c=data[year_col],
    cmap=cmap,
    alpha=0.7,
    edgecolor="k",
    linewidth=0.1,
    s=20  # Adjust marker size
)
# handle scale types
if scale_type == "log":
    plt.xscale("log")
    plt.yscale("log")
elif scale_type == "symlog":
    plt.xscale("symlog")
    plt.yscale("symlog")
elif scale_type == "linear":
    plt.xscale("linear")
    plt.yscale("linear")
else:
    print(f"Unknown scale type '{scale_type}', defaulting to log.")
    plt.xscale("log")
    plt.yscale("log")
# label and grid
plt.xlabel("Degree (Number of Connections)")
plt.ylabel("Frequency (Count of Occurrences)")
# plt.title(f"Degree Distribution for {folder_name} ({scale_type.capitalize()} Scale)")
plt.grid(True, linestyle="--", linewidth=0.5)
# add color bar with year labels
cbar = plt.colorbar(scatter, ax=plt.gca(), orientation="vertical")
cbar.set_label("Year")
cbar.set_ticks(years)
cbar.ax.set_yticklabels([str(year) for year in years])
# save the plot
# output_file = "degree_distribution.png" #os.path.join(output_dir, f"{folder_name}_count_on_{scale_type}_scala.png")
plt.tight_layout()
plt.savefig(output_file, format="png", dpi=300, bbox_inches="tight")
