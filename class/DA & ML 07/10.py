import numpy as np

pixel = 120

# Normalize
pixel = pixel / 255


def sigmoid(x):
    return 1 / (1 + np.power(np.e, -x))


for i in range(100):
    pixel *= 1.1
    pixel = sigmoid(pixel)

# Scale
print(pixel * 255)
