import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

def f(x,y):
    return x*np.exp(-(x**2 + y**2))+x**4*np.exp(-(x**2 + y**2))

def grad(x,y):
    return [(1-2*x**2+4*x**3-2*x**5)*np.exp(-(x**2 + y**2)),(-2*y*x-2*y*x**4)*np.exp(-(x**2+y**2))]

x, y = np.meshgrid(np.linspace(-2,2,16),np.linspace(-2,2,16))

z = f(x,y)
u,v = grad(x,y)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_title("courbe de la fonction f(x,y)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x,y)")
ax.plot_surface(x, y, z, rstride=1,cstride=1,cmap=cm.viridis)

fig,ax = plt.subplots(1,1,figsize=(8,8))
cp = ax.contourf(x,y,z)
q = ax.quiver(x,y,u,v)

fig.colorbar(cp)
ax.set_title("courbe de niveau et champ de gradient")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
plt.show()
