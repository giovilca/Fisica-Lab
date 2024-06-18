import numpy as np
from scipy.integrate import quad

# Numero de puntos
N = 10000

# Funcion para el metodo de Monte Carlo
def monte_carlo(f, a, b, N):
    x = np.random.uniform(a, b, N)
    f_x = f(x)
    integral = (b - a) * np.mean(f_x)
    return integral

f2 = lambda x: (np.e**x)*4
a, b = -1, 1
integral_2_mc = monte_carlo(f2, a, b, N)
integral_2_teorico, _ = quad(f2, a, b)
print(f'Monte Carlo = {integral_2_mc}')
print(f'Valor Teorico = {integral_2_teorico}')