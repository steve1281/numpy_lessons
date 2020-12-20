import numpy as np

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)


## boolean maskin and advanced masking

print(f"{filedata > 50}")
t = filedata[filedata > 50]
print(f"{filedata[filedata > 50]}")
print()
a = np.array([1,2,3,4,5,6,7,8,9])
print("a = np.array([1,2,3,4,5,6,7,8,9])")
print(f"a[[2,4,6]]= {a[[2,4,6]]}")

print("np.any(filedata>50, axis=0) # cols")
print(np.any(filedata>50, axis=0))

print("np.all(filedata>50, axis=0)")
print(np.all(filedata>50, axis=0))

print("np.any(filedata>50, axis=1) # rows")
print(f"{np.any(filedata>50, axis=1)} # rows")

print("((filedata > 50) & (filedata < 100))")
print(f"{((filedata > 50) & (filedata < 100))}")

