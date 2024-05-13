def main():
    print(" ******** MÁQUINA DE ATWOOD ******** ")
    while True:
        m1 = float(input("Ingrese la masa del primer objeto: "))
        m2 = float(input("Ingrese la masa del segundo objeto: "))


        g = 9.8   # gravedad
        if m1 > m2:
            a = (m1 - m2) * g / (m1 + m2)    # aceleración
            t = m2 * (a + g)                 # tensión
            print("\nLa aceleración de los objetos es:", a)
            print("La tensión es:", t)
            break  
        elif m2 > m1:
            a = (m2 - m1) * g / (m1 + m2)
            t = m1 * ( a + g)
            print("\nLa aceleracion de los objetos es: ", a)
            print("La tension es: ", t)
            break
        elif m1 == m2:
            a = 0
            t = m1 * g
            print("\nLa aceleracion de los objetos es: ", a)
            print("La tension es: ", t)
            break
        else:
            print("Error")

main()

