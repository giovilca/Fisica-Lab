import matplotlib.pyplot as plt

def main():
    m = float(input("Escribe la masa del objeto (kg): "))
    t = float(input("Escribe el tiempo transcurrido (s): "))
    Vo = float(input("Escribe la velocidad inicial (m/s): "))
    Vf = float(input("Escribe la velocidad final (m/s): "))
    #distancia = float(input("Escribe la distancia recorrida (m): "))
    
    aceleracion = (Vf - Vo) / t
    fuerza = m * aceleracion
    print("La fuerza que describe el móvil es:", fuerza, "N")
    graficar_proceso(t, Vo, Vf)

def graficar_proceso(t, Vo, Vf):
    tiempos = [0, t]
    velocidades = [Vo, Vf]

    plt.plot(tiempos, velocidades)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.title('Cambio de velocidad')
    plt.grid(True)
    plt.show()

main()

