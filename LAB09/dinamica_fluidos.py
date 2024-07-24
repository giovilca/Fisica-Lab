import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def lorenz_system(t, state, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Parametros del sistema
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
initial_state = [1.0, 1.0, 1.0]

t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

sol = solve_ivp(lorenz_system, t_span, initial_state, t_eval=t_eval, args=(sigma, rho, beta))
x, y, z = sol.y

# Seccion de Poincare (cruzando el plano y=0)
poincare_x = []
poincare_z = []
for i in range(1, len(y)):
    if y[i-1] < 0 and y[i] >= 0:
        poincare_x.append(x[i])
        poincare_z.append(z[i])

# Visualizacion
fig, axs = plt.subplots(1, 2, figsize=(12, 5))
axs[0].plot(x, z, lw=0.5)
axs[0].set_title('Atractor de Lorenz')
axs[0].set_xlabel('x')
axs[0].set_ylabel('z')

axs[1].scatter(poincare_x, poincare_z, s=1, color='red')
axs[1].set_title('Seccion de Poincare (y=0)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('z')

plt.tight_layout()
plt.show()
