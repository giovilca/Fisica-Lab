import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parametros del modelo
alpha = 0.1  # Tasa de crecimiento de las presas
beta = 0.02  # Tasa de depredación
delta = 0.01  # Tasa de crecimiento de los depredadores
gamma = 0.1   # Tasa de mortalidad de los depredadores

# Ecuaciones del modelo de Lotka-Volterra
def lotka_volterra(state, t):
    x, y = state  # x: presas, y: depredadores
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Condiciones iniciales
x0 = 40  # Poblacion inicial de presas
y0 = 9   # Poblacion inicial de depredadores
state0 = [x0, y0]

# Tiempo de simulacion
t = np.linspace(0, 200, 1000)

# Solucion del sistema
solution = odeint(lotka_volterra, state0, t)
x, y = solution.T

# Seccion de Poincare: muestreo cuando y = 0
poincare_section = []
for i in range(1, len(y)):
    if y[i-1] * y[i] < 0:  # Cambio de signo en y
        poincare_section.append((x[i], y[i]))

# Convertir a numpy array para facilitar el manejo
poincare_section = np.array(poincare_section)

# Graficas de la solucion
plt.figure(figsize=(12, 6))

# Grafico de la trayectoria
plt.subplot(1, 1, 1)
plt.plot(t, x, label='Presas (x)', color='blue')
plt.plot(t, y, label='Depredadores (y)', color='orange')

# Verificar si hay puntos en la seccion de Poincaré antes de graficar
if poincare_section.size > 0:
    plt.scatter(poincare_section[:, 0], poincare_section[:, 1], color='red', label='Seccion de Poincaré')

plt.title('Modelo de Lotka-Volterra: Dinamica de Presas y Depredadores')
plt.xlabel('Tiempo')
plt.ylabel('Poblacion')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
