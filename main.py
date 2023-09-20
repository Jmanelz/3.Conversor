from clase import ConversorGradosRadianes

def main():

    while True:
        print("SELECCIONE UNA OPCIÓN")
        print("1. Convertir grados a radianes")
        print("2. Convertir radianes a grados")
        print("3. Salir")

        opcion = input("(1/2/3)---->: ")

        conversor = ConversorGradosRadianes()

        if opcion == "1":
            grados = float(input("Ingresa los grados que deseas convertir: "))
            radianes = conversor.grados_a_radianes(grados)
            print(f"{grados} grados son aproximadamente {radianes} radianes.")
        elif opcion == "2":
            radianes = float(input("Ingresa los radianes que deseas convertir: "))
            grados = conversor.radianes_a_grados(radianes)
            print(f"{radianes} radianes son aproximadamente {grados} grados.")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()

