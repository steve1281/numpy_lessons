import numpy as np

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(f"Using array:\n{a}")
print(f"Which has shape: {a.shape}")

print(f"Look at a[1, 5] => {a[1,5]}")

print(f"Also   a[1, -2] => {a[1, -2]}")

print(f"Get specific row: a[0,:] {a[0,:]}")

print(f"Get specific col: a[:,2] {a[:,2]}")

print(f"get a [startindex:endindex:stepsize]")
print(f"{a[0, 1:6:2]}")
print(f"{a[0, 1:-1:2]}")

print(f"Assignment a[1,5] = 10.")
a[1,5] = 20
print(f"{a}")

print(f"Assignment column, a[:,2] = 5")
a[:,2] = 5
print(f"{a}")

print(f"Assignment column, a[:,3] = [55, 65]")
a[:,3] = [55, 65]
print(f"{a}")
