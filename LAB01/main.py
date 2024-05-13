def main():
    while True:  
        print("*** CALCULADORA DE MRU - MRUV ***")
        print("1. MRU")
        print("2. MRUV")
        print("3. Salir")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            mru()  
        elif opcion == "2":
            mruv()  
        elif opcion == "3":
            print("¡Hasta luego!")
            break  
        else:
            print("Opcion incorrecta")

def mru():
    variable = input("¿Qué quiere calcular? (d, t, v): ").lower()
    if variable == "d":
        v = float(input("Ingrese la velocidad (m/s): "))
        t = float(input("Ingrese el tiempo (s): "))
        if t > 0 and v > 0:
            print("La distancia es", v * t, "metros\n")
        else:
            print("El tiempo y la velocidad deben ser mayores que cero.\n")
    elif variable == "t":
        d = float(input("Ingrese la distancia (m): "))
        v = float(input("Ingrese la velocidad (m/s): "))
        if  v > 0:
            print("El tiempo es", d / v, "segundos\n")
        else:
            print("La distancia y la velocidad deben ser mayores que cero.\n")
    elif variable == "v":
        d = float(input("Ingrese la distancia (m): "))
        t = float(input("Ingrese el tiempo (s): "))
        if  t > 0:
            print("La velocidad es", d / t, "m/s\n")
        else:
            print("La distancia y el tiempo deben ser mayores que cero.\n")
    else:
        print("Variable no válida\n")


def mruv():
    # Ingresa la variable a calcular
    variable = input("¿Qué quiere calcular? (d, a, t, Vo, Vf): ").lower()
    
    if variable == "d": 
        Vo = float(input("Ingrese la velocidad inicial (m/s): "))  
        t = float(input("Ingrese el tiempo (s): ")) 
        a = float(input("Ingrese la aceleración (m/s^2): "))
        print("La distancia es", Vo * t + 0.5 * a * t ** 2, "metros\n")  
    elif variable == "vo": 
        Vf = float(input("Ingrese la velocidad final (m/s): "))  
        t = float(input("Ingrese el tiempo (s): "))  
        a = float(input("Ingrese la aceleración (m/s^2): "))  
        print("La velocidad inicial es", Vf - a * t, "m/s\n")  
    elif variable == "vf": 
        Vo = float(input("Ingrese la velocidad inicial (m/s): "))  
        t = float(input("Ingrese el tiempo (s): "))  
        a = float(input("Ingrese la aceleración (m/s^2): "))  
        print("La velocidad final es", Vo + a * t, "m/s\n")     
    elif variable == "a":
        Vo = float(input("Ingrese la velocidad inicial (m/s): "))  
        Vf = float(input("Ingrese la velocidad final (m/s): "))  
        t = float(input("Ingrese el tiempo (s): ")) 
        print("La aceleración es", (Vf - Vo) / t, "m/s^\n")  
    elif variable == "t":
        Vo = float(input("Ingrese la velocidad inicial (m/s): "))  
        Vf = float(input("Ingrese la velocidad final (m/s): "))  
        a = float(input("Ingrese la aceleración (m/s^2): "))  
        print("El tiempo es", (Vf - Vo) / a, "segundos\n")  
    else:
        print("Variable no válida\n")  

main()  