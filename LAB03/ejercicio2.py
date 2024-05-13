import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Función de campo eléctrico E = (Ex,Ey) 
def E(q, r0, x, y):
    """Retorna el vector de campo eléctrico E=(Ex,Ey) debido a la carga q en r0."""
    den = np.hypot(x-r0[0], y-r0[1])**3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den

# Generar una malla de 64 puntos en plano x, y 
nx, ny = 64, 64
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)

# Crear un multipolo con nq cargas de signo alternado, igualmente espaciadas
# en el círculo unitario.
nq = 5
charges = []
for i in range(nq):
    q = i % 2 * 2 - 1
    charges.append((q, (np.cos(2*np.pi*i/nq), np.sin(2*np.pi*i/nq))))

# Vector de campo eléctrico, E=(Ex, Ey), como componentes separadas
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
for charge in charges:
    ex, ey = E(*charge, x=X, y=Y)
    Ex += ex
    Ey += ey

# Crear la figura y el subplot
fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(111)

# Graficar las líneas de campo con un colormap apropiado y estilo de flecha
color = 2 * np.log(np.hypot(Ex, Ey))
ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)

# Agregar círculos llenos para las cargas mismas
charge_colors = {True: '#aa0000', False: '#0000aa'}
for q, pos in charges:
    ax.add_artist(Circle(pos, 0.05, color=charge_colors[q > 0]))

# Etiquetas de ejes
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# Mostrar el gráfico
plt.show()
