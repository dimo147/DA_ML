import sys
import time
import numpy as np

n = 2000

print("Python List")
t0 = time.time()
r = list(range(n))
t1 = time.time()

print(sys.getsizeof(r) )
print(t1 - t0, "Second")

print("Numpy NDArray")
t0 = time.time()
r = np.arange(n)
t1 = time.time()

print(sys.getsizeof(r) )
print(t1 - t0, "Second")
