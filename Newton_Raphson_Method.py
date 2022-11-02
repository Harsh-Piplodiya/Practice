import time
from math import fabs
from decimal import *
from sympy import *
import matplotlib.pyplot as mp

x=Symbol('x')
eq=x**2+2*x-2
dq=diff(eq,x)

print(solve(eq,x))  # this will print both


def newton():
    i=0
    
    rstart_t = time.perf_counter() #counts or stores the time of execution 
    
    print(f"the equation is : {eq}")
    x0=int(input("enter any approximation point : "))

    e=0.00001
    
    while fabs(eq.subs(x,x0))>e:
        i=1+i
        
        start_t = time.perf_counter()
        temp= eq.subs(x,x0)/dq.subs(x,x0)
        
        temp=float(temp)
        x1=x0-temp
        x0=x1
       
        end_t = time.perf_counter()     #stores or counts the end time/ when the code got finished running
        ttime = end_t - start_t
        
        print(f"the value of x{i} is = {x0:4f}")
        print(f"It took: {ttime: .4f}s  ")

    print(f"the root is : {x0:4f}")
    plot(eq)
     
    #this is to find out the end time of the code and the total time of taken to execute the code  
    rend_t = time.perf_counter()
    rttime = rend_t - rstart_t
    print(f"Total time: {rttime: .4f}s")

newton()