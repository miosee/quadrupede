import matplotlib.pyplot as plt
import numpy as np

e = 34
f = 45
t = 82

alpha = np.linspace(0, np.pi/4, 10)
beta = alpha
gamma = alpha

x1 = e*np.cos(alpha)
y1 = e*np.sin(alpha)
z1 = 0*alpha

x2 = x1 + f*np.cos(beta)*np.cos(alpha)
y2 = y1 + f*np.cos(beta)*np.sin(alpha)
z2 = -f*np.sin(beta)

x3 = x2 + t*np.cos(beta+gamma)*np.cos(alpha)
y3 = y2 + t*np.cos(beta+gamma)*np.sin(alpha)
z3 = z2 - t*np.sin(beta+gamma)

print(x1)
fig, ax = plt.subplots(1,3)
ax[0].plot( (0,x1[0],x2[0],x3[0]), (0,z1[0],z2[0],z3[0]), '--' )
ax[0].plot( (0,x1[-1],x2[-1],x3[-1]), (0,z1[-1],z2[-1],z3[-1]), '--'  )
ax[0].plot( x1,z1 )
ax[0].plot( x2,z2 )
ax[0].plot( x3,z3 )
ax[0].set_xlabel('x')
ax[0].set_ylabel('z')

ax[1].plot( (0,x1[0],x2[0],x3[0]), (0,y1[0],y2[0],y3[0]), '--' )
ax[1].plot( (0,x1[-1],x2[-1],x3[-1]), (0,y1[-1],y2[-1],y3[-1]), '--'  )
ax[1].plot( x1,y1 )
ax[1].plot( x2,y2 )
ax[1].plot( x3,y3 )
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')

ax[2].plot( (0,y1[0],y2[0],y3[0]), (0,z1[0],z2[0],z3[0]), '--' )
ax[2].plot( (0,y1[-1],y2[-1],y3[-1]), (0,z1[-1],z2[-1],z3[-1]), '--'  )
ax[2].plot( y1,z1 )
ax[2].plot( y2,z2 )
ax[2].plot( y3,z3 )
ax[2].set_xlabel('y')
ax[2].set_ylabel('z')

plt.show()