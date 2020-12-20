import numpy as np

# Stats

stats = np.array([[1,2,3],[4,5,6]])
print(f"stats:\n{stats}")
print(f"np.min(stats):{np.min(stats)}")
print(f"np.min(stats, axis=1):{np.min(stats,axis=1)}   # row mins")
print(f"np.min(stats, axis=0):{np.min(stats,axis=0)} # col mins")
print(f"np.sum(stats, axis=0):{np.sum(stats,axis=0)} # col sums")
print(f"np.sum(stats, axis=1):{np.sum(stats,axis=1)} # row sums")

print(f"{np.mean(stats)}")

