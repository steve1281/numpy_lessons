import numpy as np


# all 0s matrix

a = np.zeros(5)
print(f"np.zeros(5):\n{a}")

# more complex shape
a = np.zeros((2,3))
print(f"np.zeros((2,3)):\n{a}")

# even more complex
a = np.zeros((2,3,4))
print(f"np.zeros((2,3,4)):\n{a}")

# also, all ones
a = np.ones((4,2,2), dtype='int32')   # set the data type
print(f"np.ones((4,2,2)):\n{a}")

# any other number
a = np.full((2,2),99, dtype='float32')
print(f"np.full((2,2),99):\n{a}")

# you can use an other arrays shape
b = np.full_like(a,4)
print(f"b = np.full_like(a, 4) = \n{b}")

# random
a = np.random.rand(4,2)   # <--- NOTE: not a tuple! 
print(f"a =np.random.rand(4,2)\n{a}")

a = np.random.random_sample(b.shape)
print(f"a =np.random_sample(b.shape)\n{a}")

a = np.random.randint(4,7, size=(2,3))
print(f"a = np.random.randint(7, size=(2,3))\n{a}")

a = np.identity(3)
print(f"a = np.identity(3)\n{a}")

arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print("arr = np.array([[1,2,3]])")
print("r1 = np.repeat(arr,3, axis=0)")
print(r1)

# more complicated example
"""
Create:
[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 9. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
"""

output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
output[1:4,1:4] = z
print(output)


##### be careful when copying arrays

a = np.array([1,2,3])
b = a
print(b)
b[0] = 100
print(a)   # a has been changed, so a,b points memory address

## so better to copy
b = a.copy()
b[0] = 200

print(a)
print(b)




