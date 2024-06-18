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

# Definimos la funcion a integrar
f1 = lambda x: np.exp(x**2)
a, b = 0, 1

# Calculamos la integral usando el metodo de Monte Carlo
integral_1_mc = monte_carlo(f1, a, b, N)
integral_1_teorico, _ = quad(f1, a, b)

print(f'Monte Carlo = {integral_1_mc}')
print(f'Valor Teorico = {integral_1_teorico}')


