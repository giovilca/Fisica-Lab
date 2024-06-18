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
f3 = lambda x: np.sqrt(np.maximum(0, 1 - np.exp(x)**2))
a, b = 0, 1
integral_3_mc = monte_carlo(f3, a, b, N)
integral_3_teorico, _  = quad(f3, a, b)

print(f'Monte Carlo = {integral_3_mc}')
print(f'Valor Teorico = {integral_3_teorico}')

