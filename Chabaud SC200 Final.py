#!/usr/bin/env python
# coding: utf-8

# In[49]:


#Kody Chabaud
#SC200
#5-10-22: Due Date
#Final Project

#Rename this notebook file with your last name before submitting.
#By submitting this project you agree you have not violated Southeastern's policy on Academic Dishonesty as described on
#the course syllabus.
#'''
#Import ALL necessary packages for the entire notebook here.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

#Module 1 (5 points.)
#'''An object falling vertically through the air is subjected to viscous resistance as well as to the force of gravity. 
#Assume that an object with mass m is dropped from a height s_0 and that the height of the object after t seconds is
#given by
#s(t) = s_0 - m*g*t/k + m^2 * g * (1 - exp(-k*t/m))/k^2,
#where g = 32.17 ft/s^2 and k represents the coefficient of air resistance in lb-s/ft.
#Suppose s_0 = 300 ft, m = 0.25 lb, and k = 0.1 lb-s/ft. '''
g = 32.17
s_0 = 300
m = 0.25
k = .1

#Create an array t from [0, 10].
t = np.arange(0,11,1)
print(t)
#Plot the function s(t) on this interval. Add a title and label all axes. Make the graph look nice.
def s(x):
    return (s_0 - m*g*x/k + m**2*g*(1-math.exp(-k*x/m))/k**2)
s2 = np.vectorize(s)
#print(s(t[i]))
plt.plot(t,s2(t))
plt.xlabel('Time(Seconds)')
plt.ylabel('Height')
plt.title('Object Falling')
plt.grid()
plt.show()


# In[52]:


# Module 2 (2 points)
#'''For the problem from Module 1, find the time it takes the object to hit the ground using scipy's fsolve function.
fsolve(s2,6)
#Print the solution.'''
print('The object reaches the ground at ', fsolve(s2,6), 'seconds')


# In[107]:


# Module 2 Continued (8 points)
#'''A circuit has four resistors and two voltage sources. The resistors are R1, R2, R3, and R4 ohms. The voltage
#sources are E1 and E2 volts. The currents are i1, i2, and i3 amps. From Kirchoff's laws the following linear system is 
#derived.

#(R1 + R4)*i1 + R2*i2 = E1 + E2
#(R1 + R4)*i1 + R3*i3 = E1
#i1 - i2 - i3 = 0

#Create the coefficient matrix A and vector b for the linear system described above.
A = np.array([[3,2,22],
            [3,4,12]])
b = np.array([1,-1,-1]) 


#Use a linear system solver to find i1, i2, and i3 when E1 = 12 volts, E2 = 10 volts, R1 = 2 ohms, R2 = 2 ohms, 
#R3 = 4 ohms, and R4 = 1 ohm. Print your solution.'''
E1 = 12
E2 = 10
R1 = 2 
R2 = 2
R3 = 4
R4 = 1
X = np.array([[3,2,0],[3,0,4],[1,-1,-1]])
Y = np.array([22,12,0])
C = np.linalg.inv(X).dot(Y)
print(C)


# In[96]:


#Module 4 (10 points.)
#Create a 3D plot of the function z = 4 - x^2 - y^2 for 0 <= x <= 1 and 0 <=y <= 2
fig = plt.figure()
ax = plt.axes(projection='3d')
N = 10000
x = np.arange(0, 1, .01)
y = np.arange(0, 2, .01)
def z(x,y):
    return 4-x**2-y**2
xdata = np.random.random(N)
ydata = 2*np.random.random(N)
zdata = z(xdata, ydata)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Blues');
#Use Monte Carlo simulation (dartboard integration) to compute the volume of the region bounded
#by the curve and the xy plane.
x_min = 0
x_max = 1
y_min = 0
y_max = 2
integral = 0.0

for i in range(N):
    integral += zdata[i]
    
#print(integral)
Volume_Curve = ((x_max-x_min)*(y_max-y_min))
Volume = Volume_Curve*integral/float(N)
#Print the volume.
print('The volume under the curve is ', Volume, 'cm^3')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




