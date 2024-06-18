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
f7 = lambda x: (1 - x**2)**(3/2)
a, b = 0, 1
integral_7_mc = monte_carlo(f7, a, b, N)
integral_7_teorico, _ = quad(f7, a, b)
print(f'Monte Carlo = {integral_7_mc}')
print(f'Valor Teorico = {integral_7_teorico}')

