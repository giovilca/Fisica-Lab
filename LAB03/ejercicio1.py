import numpy as np
import matplotlib.pyplot as plt

# Constante de Coulomb
k = 9 * (10**9)
def main():
    while True:  
        print ("Calcular campo eléctrico y fuerza eléctrica")
        print ("1. Campo Eléctrico")
        print ("2. Fuerza Eléctrica")
        print ("3. Salir")
        opc = input("Ingrese una opción: ")

        if opc == "1":
            q = float(input("Ingrese la carga (C): "))
            calcular_campo(q)
        elif opc == "2":
            q1 = float(input("Ingrese la carga 1 (C): "))
            q2 = float(input("Ingrese la carga 2 (C): "))
            calcular_fuerza(q1, q2)
        elif opc == "3":
            print("Salió exitosamente")
            break
        else:
            print("Opción incorrecta")

# Función para calcular la fuerza eléctrica
def calcular_fuerza(q1, q2):
    # Definimos un rango de distancias
    distancias = np.linspace(1, 10, 100)

    # Calculamos la fuerza eléctrica para cada distancia
    fuerzas_electricas = [k * q1 * q2 / (r**2) for r in distancias]

    # Graficamos 
    plt.figure(figsize=(10, 5))
    plt.plot(distancias, fuerzas_electricas, label='Fuerza eléctrica')
    plt.xlabel('Distancia (m)')
    plt.ylabel('Fuerza eléctrica (N)')
    plt.title('Fuerza eléctrica en función del inverso cuadrado de la distancia')
    plt.legend()
    plt.grid(True)
    plt.show()

# Función para calcular el campo eléctrico
def calcular_campo(q):
    # Definimos un rango de distancias
    distancias = np.linspace(1, 10, 100)

    # Calculamos el campo eléctrico para cada distancia
    campos_electricos = [k * q / (r**2) for r in distancias]

    # Graficamos 
    plt.figure(figsize=(10, 5))
    plt.plot(distancias, campos_electricos, label='Campo eléctrico')
    plt.xlabel('Distancia (m)')
    plt.ylabel('Campo eléctrico (N/C)')
    plt.title('Campo eléctrico en función del inverso cuadrado de la distancia')
    plt.legend()
    plt.grid(True)
    plt.show()

main()

