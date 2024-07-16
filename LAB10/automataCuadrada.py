import numpy as np
import matplotlib.pyplot as plt

def reglas():
    
    #Define las reglas del automata celular basado en la tabla proporcionada
    return [
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 0]
    ]

def sig_estado(reglas, izq, act, der):

    #Determina el siguiente estado de una celda basado en sus vecinos y las reglas
    for regla in reglas:
        if regla[0] == izq and regla[1] == act and regla[2] == der:
            return regla[3]
    return 0

def sig_gen(estado_act):
    
    #Genera la siguiente generacion utilizando las reglas definidas
    reglas_def = reglas()
    nueva_gen = []
    n = len(estado_act)
    
    for i in range(n):
        izq = estado_act[i - 1]
        act = estado_act[i]
        der = estado_act[(i + 1) % n]
        nuevo_estado = sig_estado(reglas_def, izq, act, der)
        nueva_gen.append(nuevo_estado)
    
    return nueva_gen

def auto(estado_inicial, iteraciones):
    #Simula el automata celular
    #estado inicial del automata
    #número de iteraciones que realizara el automata
    matriz = np.zeros((iteraciones, len(estado_inicial)))
    matriz[0] = estado_inicial
    
    for i in range(1, iteraciones):
        matriz[i] = sig_gen(matriz[i - 1])
    
    return matriz

def ejecutar_auto_cuad():
    
    num_celdas = 31  # Numero de celdas iniciales para una matriz cuadrada
    estado_inicial = [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]
    iteraciones = num_celdas  # Numero de iteraciones igual al numero de celdas
    
    # Generar matriz cuadrada
    matriz_cuad = auto(estado_inicial, iteraciones)
    plt.imshow(matriz_cuad, cmap='Greys', interpolation='nearest')
    plt.title('Autómata Celular - Matriz Cuadrada')
    plt.savefig('auto_cuadrada.png')
    plt.show()

# Ejecuta para generar la matriz cuadrada
ejecutar_auto_cuad()
