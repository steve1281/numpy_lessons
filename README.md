# Learning NumPY
Based on youtube tutorial here : https://www.youtube.com/watch?v=QUT1VHiLmmI

## General Discussion/Overview

lists vs NumPy

* numpy uses fixed types
* lists use objects

numpy, for example, a value of 5 will be Int32; 4 bytes

list will use : Size, Reference Count, Object Type, Object Value: will be 8 + 8 + 8 +4 = 28 bytes.

Less memory, means faster.

iterating doesn't require type checking in numpy; so faster again

numpy uses contigous memory.

SIMD single instruction multiple data - ML instruction which really speads up

Example:

```

a = [1,3,5]
b = [1,2,3]

a * b = ERROR

vs

a = np.array([1,3,5])
b = np.array([1,2,3])
a * b = np.array([1,6,15])
```


