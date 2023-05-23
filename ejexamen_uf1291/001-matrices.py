#  Copyright (c) 2023. José Manuel Abelleira López.
#
import numpy as np

a = np.random.randint(11, size=(3, 4))
print(a)
a = a.reshape(4, 3)
print(a)
