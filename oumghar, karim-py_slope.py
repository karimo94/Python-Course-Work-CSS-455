"""Karim Oumghar Css 455
Oct 13 2015, slope hw"""

import numpy as N

x = N.array([0,1,2,3,4])
y = N.array([-20.1, -2.9, 1.5, 3.2, -1.3])

def slope(y,x):
    
    slopes = N.array(5) #new array with size 5
    #loop here
    i = 0
    while(i + 2 < slopes.size):
        delta_x = ((y[i+2] - y[i])/(x[i+2] - x[i])) #need a function
        x = 1 #we will have this as a constant
        fx = delta_x * x + intercept(delta_x, y[i], x[i])  
        derivative = ((fx - delta_x) - fx) / delta_x
        slopes[i] = derivative
        i += 1
    #end loop
    return slopes
    
def intercept(slope, y, x):
    if(x != 0):
        temp = y - slope * x
        return temp
    else:
        return x
        
dydx = slope(y,x)

print dydx

"""docstring"""