import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parametros del sistema
sigma = 1.0  # Parametro de Lennard-Jones
epsilon = 1.0  # Profundidad del pozo de potencial
dt = 0.01  # Paso de tiempo
t_max = 20.0  # Tiempo total de simulacion

# Potencial de Lennard-Jones
def lj_potential(r):
    return 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)

# Fuerzas derivadas del potencial
def lj_force(r):
    return 24 * epsilon * (2 * (sigma / r)**12 - (sigma / r)**6) / r

# Ecuaciones del movimiento
def derivs(state, t):
    x1, y1, vx1, vy1, x2, y2, vx2, vy2 = state
    r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    fx = lj_force(r) if r > 0 else 0
    fy = lj_force(r) if r > 0 else 0
    ax1 = fx
    ay1 = fy
    ax2 = -fx
    ay2 = -fy
    return [vx1, vy1, ax1, ay1, vx2, vy2, ax2, ay2]

# Condiciones iniciales
x1, y1 = -1.0, 0.0  # Posicion 1
x2, y2 = 1.0, 0.0   # Posicion 2
vx1, vy1 = 0.5, 0.0  # Velocidad 1
vx2, vy2 = -0.5, 0.0  # Velocidad 2
state0 = [x1, y1, vx1, vy1, x2, y2, vx2, vy2]

# Tiempo de simulacion
t = np.arange(0, t_max, dt)

# Solucion del sistema
solution = odeint(derivs, state0, t)
x1, y1, vx1, vy1, x2, y2, vx2, vy2 = solution.T

# Sección de Poincare: muestreo cuando y1 = 0
poincare_section = []
for i in range(1, len(y1)):
    if y1[i-1] * y1[i] < 0:  # Cambio de signo en y1
        poincare_section.append((x1[i], vx1[i]))

# Convertir a numpy array para facilitar el manejo
poincare_section = np.array(poincare_section)

# Graficas de la solución
plt.figure(figsize=(12, 6))

# Grafico de la trayectoria
plt.subplot(1, 1, 1)
plt.plot(x1, y1, label='Trayectoria de la particula 1', color='blue')
plt.plot(x2, y2, label='Trayectoria de la particula 2', color='orange')

# Verificar si hay puntos en la seccion de Poincare antes de graficar
if poincare_section.size > 0:
    plt.scatter(poincare_section[:, 0], poincare_section[:, 1], color='red', label='Seccion de Poincare')

plt.title('Seccion de Poincare en Dinamica Molecular')
plt.xlabel('Posicion en x')
plt.ylabel('Posicion en y')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
