import numpy as np
a = [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0]
f = np.exp(a) / np.sum(np.exp(a))
print(sum(f))
