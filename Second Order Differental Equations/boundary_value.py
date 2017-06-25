"""Karim Oumghar - Css 455 - BVP #11"""
import numpy as np
import math as ma
import error
from numpy import sign

#boundary value problem
#solve: y'' + (1/x) * y' + y = 0  y(0) = 1  y'(2) = 0
# y(-1) = 0      y'(-1) = -1      y'(1) = 1

#second order differential equations

def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -3.0*y[0]*y[1]
    return F


def integrate(F,x,y,xStop,h):
    X=[]
    Y=[]
    X.append(x)
    Y.append(y)
    while x < xStop:
        h=min(h,xStop-x)
        y=y+h*F(x,y)
        x=x+h
        X.append(x)
        Y.append(y)
        
    return np.array(X),np.array(Y)

def initCond(u):
    return np.array([0.0, u])

def r(u):
    X,Y = integrate(F,xStart, initCond(u), xStop,h)
    y = Y[len(Y) - 1]
    r = y[0] - 1.0
    return r

def printSoln(X,Y,freq):
    
    def printHead(n):
        print ("\n          x  ")
        for i in range (n):
            print("        y[",i,"] ")
        print()
        
    def printLine(x,y,n):
        print("{:13.4e}".format(x))
        for i in range (n):
            print("{13.4e}".format(y[i]))
        print()
    
    m = len(Y)
    try: n = len(Y[0])
    except TypeError: n=1
    if freq == 0: freq = m
    printHead(n)
    for i in range(0,m,freq):
        printLine(X[i],Y[i],n)
    if i != m - 1: printLine(X[m-1],Y[m-1],n)
    return
        


xStart=0.0
xStop=2.0
u1=0.0
u2=1.0
h=0.1
freq=2
u=0.0
X,Y = integrate(F,xStart,initCond(u),xStop,h)
printSoln(X,Y,freq)
