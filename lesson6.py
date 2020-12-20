import numpy as np

## Linear Algerbra Type stuff

a = np.ones((2,3))
print("a = np.ones((2,3))")
print(a)

b = np.full((3,2),2)
print("b = np.full((3,2),2)")
print(b)

# recall the columns of M1 equal dimension to rows of M2

# matrix multiplication

c = np.matmul(a,b)
print("c = np.matmul(a,b)")
print(c)


# say you wanted the dterminant of a matrix
c = np.identity(3)
print(f"np.linalg.det(np.identity(3))\n{np.linalg.det(c)}")


