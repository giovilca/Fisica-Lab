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
f5 = lambda x: (np.e)**(x+x**2)
a, b = 0, 1
integral_5_mc = monte_carlo(f5, a, b, N)
integral_5_teorico, _ = quad(f5, a, b)
print(f'Monte Carlo = {integral_5_mc}')
print(f'Valor Teorico = {integral_5_teorico}')

