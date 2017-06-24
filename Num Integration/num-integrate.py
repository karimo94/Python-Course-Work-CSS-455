"""Karim Oumghar
Css 455 - Dec 1 - Problem #14
Num Diff revisited"""
import numpy as np
import math

def gaussNodes(m,tol=10e-9):
    def legendre(t,m):
        p0 = 1.0
        p1 = t
        for k in range(1,m):
            p = ((2.0*k + 1.0) * t * p1 - k * p0)/(1.0+k)
            p0 = p1
            p1 = p
        dp = m*(p0 - t*p1)/(1.0-t**2)
        return p,dp
    
    A = np.zeros(m)
    x = np.zeros(m)
    nRoots = int((m + 1)/2)
    for i in range(nRoots):
        t = math.cos(math.pi*(i+0.75)/(m+0.5))
        for j in range(30):
            p,dp = legendre(t,m)
            dt = -p/dp
            t = t + dt
            if abs(dt) < tol:
                x[i] = t
                x[m-i-1] = -t
                A[i] = 2.0/(1.0 - t**2)/(dp**2)
                A[m-i-1] = A[i]
                break
    return x,A

def gaussQuad(f,a,b,m):
    c1 = (b+a)/2.0
    c2 = (b-a)/2.0
    x,A = gaussNodes(m)
    sum = 0.0
    for i in range(len(x)):
        sum = sum + A[i]*f*(c1+c2*x[1])
    return c2*sum   

def trapezoidal_rule(f,a,b,n):
    h = float(b-a)/2
    s = f * a + f * b
    for i in xrange(1,n):
        s += 2 * f * (a + i * h)
    return s * h / 2   
def f(x):
    return pow(x,2) * math.sqrt(1+pow(2*2.3456/5.6789,2))     

#gauss quadrature
print gaussQuad(f(0.5),0,1,10)
print gaussQuad(f(1.0),0,1,10)
print gaussQuad(f(2.0),0,1,10)
#composite trapezoidal rule
print trapezoidal_rule(f(0.5), 0,1,1)
print trapezoidal_rule(f(1.0), 0,1,1)
print trapezoidal_rule(f(2.0), 0,1,1)
