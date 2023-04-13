import numpy as np
import scipy as sp
import cupy as cp
import time

# dimensioni delle matrici
n = 1000
m = 2000

# creazione di due matrici con numeri casuali
a_np = np.random.rand(n, m)
b_np = np.random.rand(m, n)

# conversione delle matrici in formato CuPy
a_cp = cp.asarray(a_np)
b_cp = cp.asarray(b_np)

# calcolo del prodotto matrice-matrice in NumPy
start_time = time.time()
c_np = np.dot(a_np, b_np)
numpy_time = time.time() - start_time

# calcolo del prodotto matrice-matrice in SciPy
start_time = time.time()
c_sp = np.dot(a_np, b_np)
scipy_time = time.time() - start_time

# calcolo del prodotto matrice-matrice in CuPy
start_time = time.time()
c_cp = cp.dot(a_cp, b_cp)
cupy_time = time.time() - start_time

# stampa dei tempi di esecuzione
print("NumPy time:", numpy_time)
print("SciPy time:", scipy_time)
print("CuPy time:", cupy_time)

