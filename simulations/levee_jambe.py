import matplotlib.pyplot as plt
import numpy as np

e = 34
f = 45
t = 82

n = 10

x = np.ones(n)*80
y = np.zeros(n)
z = np.linspace(50,70,n)

w = np.sqrt(x**2 + y**2) - e
tmp1 = (w**2 + z**2 + f**2 - t**2)/(2*f*np.sqrt(w**2+z**2))
tmp2 = (w**2 + z**2 - f**2 - t**2)/(2*f*t)
print("w :", w)
print("tmp1 :", tmp1)
print("tmp2 :", tmp2)

alpha = np.arctan2(y,x)
beta = np.arctan2(z,w) - np.arccos(tmp1)
gamma = np.arccos(tmp2) 
print("alpha :", alpha)
print("beta :", beta)
print("gamma : ", gamma)

x1 = e*np.cos(alpha)
y1 = e*np.sin(alpha)
z1 = 0*alpha
print("x1 :",x1)
print("y1 :",y1)

x2 = x1 + f*np.cos(beta)*np.cos(alpha)
y2 = y1 + f*np.cos(beta)*np.sin(alpha)
z2 = -f*np.sin(beta)
print("x2 :",x2)
print("y2 :",y2)
print("z2 :",z2)

x3 = x2 + t*np.cos(beta+gamma)*np.cos(alpha)
y3 = y2 + t*np.cos(beta+gamma)*np.sin(alpha)
z3 = z2 - t*np.sin(beta+gamma)
print("x :", x)
print("x3 :", x3)
print("y :", y)
print("y3 :", y3)
print("z :", z)
print("z3 :", z3)

fig, ax = plt.subplots()
ax.plot( (0,x1[0],x2[0],x3[0]), (0,z1[0],z2[0],z3[0]), '--' )
ax.plot( (0,x1[-1],x2[-1],x3[-1]), (0,z1[-1],z2[-1],z3[-1]), '--'  )
ax.plot( x1,z1 )
ax.plot( x2,z2 )
ax.plot( x3,z3 )
ax.set_xlabel('x')
ax.set_ylabel('z')
plt.xlim(-40,90)
plt.ylim(-90,40)
ax.set_aspect('equal', adjustable='box')

plt.show()