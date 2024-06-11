import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def wave_equation(num_steps, num_points, r):
    length = 1.0  
    T = 1.0  
    delta_x = length / (num_points - 1)  
    delta_t = T / num_steps  

    # Inicialización de la malla
    u = np.zeros((num_points, num_steps + 1))  
    u_prev = np.zeros(num_points)  

    # Condición inicial
    u[:, 0] = np.sin(np.pi * np.linspace(0, 1, num_points))  
    u[:, 1] = u[:, 0]  

    # Iteración temporal
    for j in range(1, num_steps):
        for i in range(1, num_points - 1):
            u[i, j + 1] = 2 * (1 - r**2) * u[i, j] + r**2 * (u[i + 1, j] + u[i - 1, j]) - u[i, j - 1]

    x = np.linspace(0, length, num_points)  # Puntos espaciales
    t = np.linspace(0, T, num_steps + 1)  # Puntos temporales

    # Definición del mapa de colores personalizado
    colors = [(1, 0, 0), (1, 0.5, 0), (1, 1, 0)]  
    cmap_name = 'red_orange_yellow'
    cm = LinearSegmentedColormap.from_list(cmap_name, colors, N=100)

    # Visualización
    X, T = np.meshgrid(x, t)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, u.T, cmap=cm)  
    ax.set_xlabel('Posición')
    ax.set_ylabel('Tiempo')
    ax.set_zlabel('Desplazamiento')
    ax.set_title('Evolución de la Onda en una Barra')
    plt.show()

# Parámetros de la simulación
num_points = 50  # Número de puntos de la malla espacial
num_steps = 500  # Número de pasos de tiempo
c = 1.0  # Velocidad de la onda
delta_x = 1.0 / (num_points - 1)
delta_t = 1.0 / num_steps
r = c * delta_t / delta_x  # Número de Courant

# Resolver la ecuación de onda
wave_equation(num_steps, num_points, r)

