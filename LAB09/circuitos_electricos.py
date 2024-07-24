import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parametros del circuito RLC
R = 1.0  # Resistencia en ohmios
L = 1.0  # Inductancia en henrios
C = 1.0  # Capacitancia en faradios

# Ecuaciones diferenciales del circuito RLC
def model(y, t):
    V, I = y
    dVdt = (1/C) * I
    dIdt = (-R/L) * I - (1/L) * V
    return [dVdt, dIdt]

# Condiciones iniciales
V0 = 1.0  # Voltaje inicial
I0 = 0.0  # Corriente inicial
y0 = [V0, I0]

# Tiempo de simulacion
t = np.linspace(0, 20, 1000)

# Solucion del sistema
solution = odeint(model, y0, t)
V, I = solution[:, 0], solution[:, 1]

# Seccion de Poincare: muestreo del voltaje
poincare_section = []
for i in range(1, len(V)):
    if V[i-1] * V[i] < 0:  # Cambio de signo en V
        poincare_section.append((V[i], I[i]))

# Convertir a numpy array para facilitar el manejo
poincare_section = np.array(poincare_section)

# Graficas de la solucion
plt.figure(figsize=(12, 6))

# Grafico del espacio de fase
plt.subplot(1, 1, 1)
plt.plot(V, I, label='Trayectoria del sistema', color='blue')
plt.scatter(poincare_section[:, 0], poincare_section[:, 1], color='red', label='Seccion de Poincare')
plt.title('Seccion de Poincare del circuito RLC')
plt.xlabel('Voltaje (V)')
plt.ylabel('Corriente (I)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
