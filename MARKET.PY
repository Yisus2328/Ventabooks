import funciones2 as fu


while True:
    fu.limpiarpantalla()
    fu.titulo("Gestion de productos")
    fu.printa("1) Guardar")
    fu.printa("2) Listar")
    fu.printa("3) certificado")
    fu.printa("0) Salir")
    opcion =int(input("Seleccione :"))

    if opcion==0:
        break
    elif opcion==1:
        fu.titulo("Guardar producto")
        cod=int(input("Ingrese el codigo : "))
        nom=input("Ingrese el nombre :")
        desc=input("Ingrese descripcion :")
        pre=int(input("Ingrese el precio :"))
        sto=int(input("Ingrese stock :"))
        fu.guardar(cod,nom,desc,pre,sto)
    elif opcion==2:
        fu.titulo("Listar productos")
        fu.listar()
    elif opcion==3:
        fu.titulo("Certificado producto")
        codigo=int(input("Ingrese codigo :"))
        fu.certificadoopiniones(codigo)
    else:
        fu.printr("Opcion no valida")