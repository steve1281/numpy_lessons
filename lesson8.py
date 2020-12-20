import numpy as np

# Re-organizing Arrays

before = np.array([[1,2,3,4],[5,6,7,8]])
print(f"before:\n{before}")
print(f"before.shape: {before.shape}")

after = before.reshape((8,1))
print(f"after:\n{after}")
print( f"after.reshape(2,2,2):\n{after.reshape(2,2,2)}")

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(f"v1:\n{v1}")
print(f"v2:\n{v2}")
print(f"np.vstack([v1, v2]):\n{np.vstack([v1,v2])}")
print(f"np.vstack([v1, v2, v2, v2]):\n{np.vstack([v1,v2,v2,v2])}")

h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(f"h1:\n{h1}")
print(f"h2:\n{h2}")
print(f"np.hstack([h1,h2]):\n{np.hstack([h1,h2])}")


