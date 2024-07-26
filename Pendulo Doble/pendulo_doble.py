import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parámetros del péndulo
g = 9.81  # Aceleración debida a la gravedad (m/s^2)
L1 = 1.0  # Longitud del primer péndulo (m)
L2 = 1.0  # Longitud del segundo péndulo (m)

def derivs(state, t):
    θ1, θ2, ω1, ω2 = state
    dθ1dt = ω1
    dθ2dt = ω2

    Δθ = θ2 - θ1
    den1 = (L1/L2) * np.cos(Δθ)
    den2 = (L1/L2) * np.cos(Δθ)**2

    dω1dt = (-g*(2*np.sin(θ1) + np.sin(θ2)*den1) / (2 - den2))
    dω2dt = (-g*(2*np.sin(θ2) + np.sin(θ1)*den1) / (2 - den2))

    return dθ1dt, dθ2dt, dω1dt, dω2dt

# Condiciones iniciales
θ1_init = 1.0  # Ángulo inicial del primer péndulo (rad)
θ2_init = 0.5  # Ángulo inicial del segundo péndulo (rad)
ω1_init = 0.0  # Velocidad angular inicial del primer péndulo
ω2_init = 0.0  # Velocidad angular inicial del segundo péndulo
state_init = [θ1_init, θ2_init, ω1_init, ω2_init]

# Tiempo de simulación
t = np.linspace(0, 15, 1000)

# Resolver las ecuaciones
state = odeint(derivs, state_init, t)

# Extraer los ángulos
θ1 = state[:, 0]
θ2 = state[:, 1]

# Calcular las posiciones x e y
x1 = L1 * np.sin(θ1)
y1 = -L1 * np.cos(θ1)
x2 = x1 + L2 * np.sin(θ2)
y2 = y1 - L2 * np.cos(θ2)

# Graficar las trayectorias
plt.figure(figsize=(10, 5))
plt.plot(x1, y1, label='Trayectoria del Péndulo 1 (θ1 = 1 rad)', color='blue')
plt.plot(x2, y2, label='Trayectoria del Péndulo 2 (θ2 = 0.5 rad)', color='purple')
plt.title('Trayectoria del Péndulo Doble')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
