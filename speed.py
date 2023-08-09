import numpy as np
import time

N = 1_000_000

arr = np.random.random(N)

print('Starting test...')
start = time.time()
np_arr = arr.reshape(((N // 2), 2))
np_t = time.time() - start

start = time.time()
py_arr = np.array([[arr[i-1], arr[i]] for i in range(1, len(arr), 2)])
py_t = time.time() - start

print(f'Numpy did it in {np_t} seconds')
print(f'Python did it in {py_t} seconds')
print('Np array:')
print(np_arr)
print('--\nPy array:')
print(py_arr)