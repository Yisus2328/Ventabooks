import funcionesn as f


while True:
    f.limpiarpantalla()
    f.titulo()
    opcion=int(input("Seleccione :"))
    if opcion==0:
        f.printv("Hasta luego")
        break
    else:
        f.opciones(opcion)