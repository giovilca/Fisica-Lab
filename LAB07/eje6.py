import numpy as np
from scipy.integrate import quad

N = 10000

# Funcion para el metodo de Monte Carlo
def monte_carlo(f, a, b, N):
    x = np.random.uniform(a, b, N)
    f_x = f(x)
    integral = (b - a) * np.mean(f_x)
    return integral

# Definimos la funcion a integrar
f6 = lambda x: np.e**(-x)
a, b = 0, 1
integral_6_mc = monte_carlo(f6, a, b, N)
integral_6_teorico, _ = quad(f6, a, b)

print(f'Monte Carlo = {integral_6_mc}')
print(f'Valor Teórico = {integral_6_teorico}')
