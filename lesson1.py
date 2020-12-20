import numpy as np

a = np.array([1,2,3], dtype='int16')    # override the default (which is int32)
b = np.array([[9.0, 8.0, 7.0],[6.0, 5.0, 4.0]])

print("Dump arrays:")
print(f"a:{a}")
print(f"b:{b}")

print("Dimensions:")
print(f"\ta:{a.ndim}")
print(f"\tb:{b.ndim}")

print("Shapes:")
print(f"\ta:{a.shape}")
print(f"\tb:{b.shape}")

print("Type:")
print(f"\ta:{a.dtype}")
print(f"\tb:{b.dtype}")

print("Size (per cell):")
print(f"\ta:{a.itemsize} bytes")
print(f"\tb:{b.itemsize} bytes")

print("Total Size:")
print(f"\ta:{a.nbytes} bytes")
print(f"\tb:{b.nbytes} bytes")


