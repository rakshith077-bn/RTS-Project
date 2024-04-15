import matplotlib.pyplot as plt
import pandas as pd

#{snapshot_count}, {size_change}, {count_change}, {average_change}

# Read the CSV data into a DataFrame
df = pd.read_csv('snapshot_binary.csv', header=None)
print(df.head())

# (Size) over time (Snapshot Count)
plt.figure(figsize=(10, 6))  
plt.plot(df[0], df[1])
plt.xlabel('Snapshot Count')
plt.ylabel('Memory Usage (Size)')
plt.title('Memory Usage Over Time')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df[2], df[1])
plt.xlabel('Object Count')
plt.ylabel('Memory Usage (Size)')
plt.title('Object Count vs. Memory Usage')
plt.grid(True)
plt.show()