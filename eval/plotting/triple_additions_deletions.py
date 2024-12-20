import pandas as pd
import matplotlib.pyplot as plt

accumulated_ends = pd.read_csv("/home/marvin/workspace/data/dbpedia-tkg/stats_1217_1825/FULL/accumulated_ends.csv")
accumulated_starts = pd.read_csv("/home/marvin/workspace/data/dbpedia-tkg/stats_1217_1825/FULL/accumulated_starts.csv")

# Plot the data
plt.figure(figsize=(6, 4))
plt.plot(accumulated_ends.index, accumulated_ends['count_end_triples'], label="Deleted Triples")
plt.plot(accumulated_starts.index, accumulated_starts['count_start_triples'], label="Added Triples")
plt.xlabel("Date")
plt.ylabel("Cumulative Count")
plt.title("Accumulated Event Ends (2000-2025)")
plt.legend()
plt.grid()
plt.savefig("triple_changes_over_time.pdf", format="pdf", bbox_inches="tight")
