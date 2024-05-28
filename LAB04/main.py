import numpy as np
import matplotlib.pyplot as plt
from magpylib.source.magnet import Box, Cylinder
from magpylib import Collection, displaySystem

# Crear los imanes
x1 = Box(mag=(0, 0, 600), dim=(3, 3, 3), pos=(-4, 0, 3))
x2 = Cylinder(mag=(0, 0, 500), dim=(3, 5))

# Crear una colección de imanes
c = Collection(x1, x2)

# Manipular los imanes individualmente
x1.rotate(45, (0, 1, 0), anchor=(0, 0, 0))
x2.move((5, 0, -4))

# Manipular la colección
c.move((-2, 0, 0))

# Calcular el campo magnético en una cuadrícula
xs = np.linspace(-10, 10, 33)
zs = np.linspace(-10, 10, 44)
POS = np.array([(x, 0, z) for z in zs for x in xs])
Bs = c.getB(POS).reshape(44, 33, 3)

# Crear la figura
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121, projection='3d')  # Eje 3D
ax2 = fig.add_subplot(122)  # Eje 2D

# Visualizar la geometría del sistema en ax1
displaySystem(c, subplotAx=ax1, suppress=True)

# Visualizar el campo en el plano xz usando matplotlib
X, Z = np.meshgrid(xs, zs)
U, V = Bs[:, :, 0], Bs[:, :, 2]
field_magnitude = np.sqrt(U**2 + V**2)
strm = ax2.streamplot(X, Z, U, V, color=field_magnitude, linewidth=1, cmap='inferno')
fig.colorbar(strm.lines, ax=ax2, label='amplitud del campo [mT]')

ax2.set_title('Campo magnético')
ax2.set_xlabel('posición x [mm]')
ax2.set_ylabel('posición z [mm]')

plt.tight_layout()
plt.show()

