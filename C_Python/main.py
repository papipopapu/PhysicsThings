from ctypes import CDLL, POINTER, c_int, c_double
import numpy as np

NPTR = np.ctypeslib.ndpointer(dtype = np.float64, ndim = 2, flags = "C")
EDO = CDLL("/home/joel/C_Python/EDO.so")
EDO.RK4.argtypes = [NPTR, c_double, c_double, c_int, c_int]
EDO.RK4.restype = None





N = int(1e7);  dt = 1; t0 = 0; Y = np.zeros((N, 2), dtype = np.float64); 
Y[0] = np.asarray([1, 0]);
EDO.RK4(Y, t0, dt, 2, N);
print(Y.shape)
#print(Y[:, 0])


