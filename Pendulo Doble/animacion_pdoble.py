import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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

# Crear la figura para la animación
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 1)
ax.set_aspect('equal')
ax.grid()

# Inicializar las líneas del péndulo
line1, = ax.plot([], [], 'o-', lw=2, color='blue')
line2, = ax.plot([], [], 'o-', lw=2, color='purple')

# Función de inicialización
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Función de actualización para la animación
def update(frame):
    line1.set_data([0, x1[frame]], [0, y1[frame]])
    line2.set_data([x1[frame], x2[frame]], [y1[frame], y2[frame]])
    return line1, line2

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=20)

plt.title('Animación del Péndulo Doble')
plt.show()
