import numpy as np

img = np.array([1,2,3,4,5,6,7])
# print(np.clip(x, 2,4))

print(img.dtype)

img=img.astype(np.uint8)
print(img.dtype)
