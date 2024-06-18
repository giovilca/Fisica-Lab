import numpy as np
from scipy.integrate import quad

N = 10000

# Funcion para el metodo de Monte Carlo
def monte_carlo(f, a, b, N):
    x = np.random.uniform(a, b, N)
    f_x = f(x)
    integral = (b - a) * np.mean(f_x)
    return integral

# Funcion a integrar
f4 = lambda x: x * (1 + x**2)**(-2)
a, b = 0, 1
integral_4_mc = monte_carlo(f4, a, b, N)
integral_4_teorico, _ = quad(f4, a, b)

print(f'Monte Carlo = {integral_4_mc}')
print(f'Valor Teorico = {integral_4_teorico}')
