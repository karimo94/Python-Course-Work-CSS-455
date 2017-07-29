"""Karim Oumghar - Nov 24 2015
Css 455 - Numerical Diff revisited
Problem #13"""

import math as ma

def toRadian(degree):
    return (degree*(3.141/180))
def function(alpha, beta):
    tan_a = ma.tan(toRadian(alpha))
    tan_b = ma.tan(toRadian(beta))
    x = tan_b/(tan_b - tan_a)
    y = (tan_a * tan_b)/(tan_b-tan_a)
    return x,y
    
times = [9,10,11]
theta = [54.80,54.06,53.34]
beta = [65.59,64.59,63.62]
distance = 500
angles = function(theta[1], beta[1])
avg_theta = (angles[0] + angles[1]) / 2
g = 9.8 #m/s^2, from physics...

#it looks like the problem is now really
#finding velocity from angle and horizontal displacement
#I had to solve for v...from--> distance = (v^2*sin(2*theta))/g
velocity = ma.sqrt(g*distance/ma.sin(2*avg_theta))
print velocity #I think this is correct...