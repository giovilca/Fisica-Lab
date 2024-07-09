import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros del sistema de Lorenz
sigma = 10
rho = 28
beta = 8/3

# Condiciones iniciales
x0 = 1.0
y0 = 1.0 
z0 = 1.0

# Función para calcular las ecuaciones diferenciales
def lorenz(x, y, z, sigma, rho, beta):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# Integrar las ecuaciones diferenciales
dt = 0.01
t = np.arange(0.0, 40.0, dt)
x = np.empty_like(t)
y = np.empty_like(t)
z = np.empty_like(t)

x[0], y[0], z[0] = (x0, y0, z0)
for i in range(1, len(t)):
    dx, dy, dz = lorenz(x[i-1], y[i-1], z[i-1], sigma, rho, beta)
    x[i] = x[i-1] + (dx * dt)
    y[i] = y[i-1] + (dy * dt)
    z[i] = z[i-1] + (dz * dt)

# Graficar el atractor de Lorenz
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, lw=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Atractor de Lorenz")
plt.show()
