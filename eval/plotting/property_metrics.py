import pandas as pd
import matplotlib.pyplot as plt

# Simulate a large dataset
import random
random.seed(42)

df = pd.read_csv("propAll")
df["rel"] = df["rel"].str.replace("http://dbpedia.org/ontology/", "dbo:", regex=False)
df["rel"] = df["rel"].str.replace("http://purl.org/dc/terms/", "purl:", regex=False)
df["rel"] = df["rel"].str.replace("http://xmlns.com/foaf/0.1/","foaf:", regex=False)
df["rel"] = df["rel"].str.replace("http://www.georss.org/georss/","georss:", regex=False)
df["rel"] = df["rel"].str.replace("http://www.w3.org/2000/01/rdf-schema#","rdfs:", regex=False)
df["rel"] = df["rel"].str.replace("http://www.w3.org/2004/02/skos/core#","skos:", regex=False)
df["rel"] = df["rel"].str.replace("http://www.w3.org/2003/01/geo/wgs84_pos#","geo:", regex=False)
df["rel"] = df["rel"].str.replace("http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdf:", regex=False)

dfOccurences = pd.read_csv("propAll_withTotalHead")
dfOccurences =dfOccurences[["rel", "total_heads"]]
dfOccurences["rel"] = dfOccurences["rel"].str.replace("http://dbpedia.org/ontology/", "dbo:", regex=False)
dfOccurences["rel"] = dfOccurences["rel"].str.replace("http://purl.org/dc/terms/", "purl:", regex=False)
dfOccurences["rel"] = dfOccurences["rel"].str.replace("http://xmlns.com/foaf/0.1/","foaf:", regex=False)
dfOccurences["rel"] = dfOccurences["rel"].str.replace("http://www.georss.org/georss/","georss:", regex=False)
dfOccurences["rel"] = dfOccurences["rel"].str.replace("http://www.w3.org/2000/01/rdf-schema#","rdfs:", regex=False)
dfOccurences["rel"] = dfOccurences["rel"].str.replace("http://www.w3.org/2004/02/skos/core#","skos:", regex=False)
dfOccurences["rel"] = dfOccurences["rel"].str.replace("http://www.w3.org/2003/01/geo/wgs84_pos#","geo:", regex=False)
dfOccurences["rel"] = dfOccurences["rel"].str.replace("http://www.w3.org/1999/02/22-rdf-syntax-ns#","rdf:", regex=False)

# Sort relations by total_heads for clarity
# df_sorted = df.sort_values(by="max_changes", ascending=False)
# Plot charts
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

rawdf = pd.merge(df, dfOccurences, left_on='rel', right_on='rel', how='inner')

# Select top 10 relations
df = rawdf.sort_values(by="total_heads", ascending=False).head(20)
print()
print("### top 10 relations total usages in the graph")
print(df)
df.plot(x="rel", y="total_heads", kind="bar", ax=axes[0, 0], color="red", legend=True)
axes[0, 0].set_xlabel("")
axes[0, 0].set_yscale("log")
axes[0, 0].set_title("Top 10 Relations: Total")
axes[0, 0].set_ylabel("Total Occurences")
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].yaxis.grid()
for label in axes[0, 0].get_xticklabels():
    label.set_ha("right")

# Top 10 unqiue triples
df = rawdf.sort_values(by="total_changes", ascending=False).head(20)
print()
print("### top 10 relations total changes")
print(df)
df.plot(x="rel", y="total_changes", kind="bar", ax=axes[0, 1], color="green", legend=True)
axes[0, 1].set_xlabel("")
axes[0, 1].set_yscale("log")
axes[0, 1].set_title("Top 10 Relations Changes: Total")
axes[0, 1].set_ylabel("Changes Total")
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].yaxis.grid()
for label in axes[0, 1].get_xticklabels():
    label.set_ha("right")


# top 10 average 
df = rawdf.sort_values(by="avg_changes", ascending=False).head(20)
print()
print("### top 10 relations average changes")
print(df)
df.plot(x="rel", y="avg_changes", kind="bar", ax=axes[1, 0], legend=True, color="blue")
axes[1, 0].set_yscale("log")
axes[1, 0].set_xlabel("")
axes[1, 0].set_title("Top 10 Relations Changes: Average")
axes[1, 0].set_ylabel("Changes Average")
axes[1, 0].tick_params(axis='x', rotation=45)
for label in axes[1, 0].get_xticklabels():
    label.set_ha("right")  # Align labels to the start

# top 10 median
df = rawdf.sort_values(by="median", ascending=False).head(20)
print()
print("### top 10 relations median changes")
print(df)
df.plot(
    x="rel",
    # y=["25th_percentile", "median","75th_percentile"],
    y=[ "median"],
    kind="bar",
    ax=axes[1, 1],
    color="orange",
)
# axes[1, 1].set_yscale("log")
axes[1, 1].set_xlabel("")
axes[1, 1].set_title("Top 10 Relations Changes: Median")
axes[1, 1].set_ylabel("Changes Median")
axes[1, 1].tick_params(axis='x', rotation=45)
for label in axes[1, 1].get_xticklabels():
    label.set_ha("right")

# Adjust layout
plt.tight_layout()
plt.savefig("properties_plot.pdf", format="pdf", bbox_inches="tight")
