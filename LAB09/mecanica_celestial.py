import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constantes del sistema
G = 1.0  # Constante gravitacional
M = 1.0  # Masa de la estrella
dt = 0.01  # Paso de tiempo
t_max = 20.0  # Tiempo total de simulacion

# Ecuaciones del movimiento
def derivs(state, t):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    ax = -G * M * x / r**3
    ay = -G * M * y / r**3
    return [vx, vy, ax, ay]

# Condiciones iniciales
x0 = 1.0  # Posicion inicial en x
y0 = 0.0  # Posicion inicial en y
vx0 = 0.0  # Velocidad inicial en x
vy0 = 1.0  # Velocidad inicial en y
state0 = [x0, y0, vx0, vy0]

# Tiempo de simulacion
t = np.arange(0, t_max, dt)

# Solucion del sistema
solution = odeint(derivs, state0, t)
x, y, vx, vy = solution.T

# Seccion de Poincare: muestreo del momento en que y=0
poincare_section = []
for i in range(1, len(y)):
    if y[i-1] * y[i] < 0:  # Cambio de signo en y
        poincare_section.append((x[i], vx[i]))

# Convertir a numpy array para facilitar el manejo
poincare_section = np.array(poincare_section)

# Graficas de la solucion
plt.figure(figsize=(12, 6))

# Grafico de la trayectoria
plt.subplot(1, 1, 1)
plt.plot(x, y, label='Trayectoria del cuerpo', color='blue')
plt.scatter(poincare_section[:, 0], poincare_section[:, 1], color='red', label='Seccion de Poincare')
plt.title('Seccion de Poincare en Mecanica Celestial')
plt.xlabel('Posicion en x')
plt.ylabel('Posicion en y')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()



