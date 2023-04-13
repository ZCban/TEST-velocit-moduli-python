import numpy as np
import time
x=10
y=-10
def abstime():
    start=time.time()
    print( abs(x),abs(y))
    end=time.time()
    print(end-start)

def nabstime():
    start=time.time()
    print( np.abs(x),np.abs(y))
    end=time.time()
    print(end-start)

def bitwise():
    start=time.time()
    x1 = x & (~0 << x.bit_length())
    y1 = y & (~0 << y.bit_length())
    print(x1,y1)
    end=time.time()
    print(end-start)
    
    
abstime()
nabstime()
bitwise()
