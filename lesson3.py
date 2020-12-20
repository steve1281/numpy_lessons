import numpy as np

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(f"b is \n{b}")

print("Get specific element, work outside in...")
print(f"b[0,1,1] = {b[0,1,1]}")
print(f"b[:,1,:] = \n{b[:,1,:]}")

print("You could update that, so long as dimension is ok:")
print("b[:,1,:] = [[9,9],[8,8]]")
b[:,1,:] = [[9,9],[8,8]]
print(b)



