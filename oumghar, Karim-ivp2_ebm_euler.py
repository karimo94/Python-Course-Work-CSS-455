"""Karim Oumghar - Css 455 - IVP revisited - euler part"""
import numpy as np
import os
import matplotlib.pyplot as plt

myOutputPath = os.path.join(os.getcwd(), 'Documents',\
'oumghar, karim-py_files_plots.png')
pC = 2.06E+08
S = 342.5
epsilon_times_tau = 0.62
sigma = 5.67E-08
T0 = 287
dt = 86400

T = []
T_ice = 273
T_noice = 293
albedo = 0.3
A_ice = 1
A_noice = 0
def f(y):
    return 
def euler(f,y0,a,b,h):
    t,y = a,y0
    while t <= b:
        print "%6.3f %6.3f" % (t,y)
        t += h
        y += h * f(y)

for i in range(4000):
    if T[i] <= T_ice:
        albedo = A_ice
    elif T[i] >= T_noice:
        albedo = A_noice
    else:
        albedo = ((T[i]-T_ice)/(T_noice-T_ice)*(A_noice-A_ice))+A_ice

    T_tend = ((S*(1-albedo))-(epsilon_times_tau * sigma * (T[i]**4)))/pC
    T[i+1] = T[i] + (T_tend*dt)


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Climate model (Eulers)')
plt.xlim([273,293])
plt.ylim([0,100])
plt.plot(4000, T, 'b')
plt.savefig(myOutputPath)
plt.show()