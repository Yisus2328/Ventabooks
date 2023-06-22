from colorama import Fore,Style
import numpy 
import msvcrt
import os
import random

#################################################
#Crear arreglo
libros=numpy.empty([10,4],object)

#################################################
#Funciones de diseño
def printv(texto):
    print(f"{Fore.GREEN}{texto}{Fore.RESET}")

def printr(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def printvv(texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def printa(texto):
    print(f"{Fore.BLUE}{texto}{Fore.RESET}")

def limpiarpantalla():
    printvv("<<Presione una tecla para continuar>>")
    msvcrt.getch()
    os.system("cls")

Criticas=[]

Criticas.append("Me duermo leyendolo")
Criticas.append("Los libros del colegio son mejores")
Criticas.append("Muy caro")
Criticas.append("Mucho texto")
Criticas.append("No entendi nada")
Criticas.append("Dios perdona, yo no ")
Criticas.append("Wazaaaaaaa 👻")
Criticas.append("10 de 10")
Criticas.append("Que bendicion")



def validarcod(cod):
    for i in range(10):
        if libros[i,0]==cod:
            return i
    return -1


def titulo():
    printvv(f"""
    ------------------------
           VENTABOOKS  
    -------------------------""")
    printa("""
    1) Guardar libro
    2) Buscar libro
    3) Imprimir documento 
    0) Salir""")

def opciones(opcion):

    if opcion==1:
        printv("GUARDAR LIBRO")
        if None in libros:
            c=int(input("Ingrese el codigo del libro :"))
            if validarcod(c)<0:
                tit=input("Ingrese el titulo del libro :").capitalize()
                if len(tit)>=4:
                    au=input("Ingrese el nombre del autor :").capitalize()
                    pr=int(input("Ingrese el precio de un libro :"))
                    if pr>=0:
                        for i in range(10):
                            if libros[i,0]==None:
                                libros[i,0]=c
                                libros[i,1]=tit
                                libros[i,2]=au
                                libros[i,3]=pr
                                printv("Libro registrado con exito ")
                                break
                    else:
                        printr("El precio debe ser un numero positivo")
                else:
                    printr("El titulo debe tener minimo 4 caracteres")
            else:
                printr("El codigo esta repetido")
        else:
            printr("No hay espacio disponible")    
    elif opcion==2:
        printv("BUSCAR LIBRO")
        cc=int(input("Ingrese el codigo del libro que desea buscar :"))
        for i in range(10):
            if libros[i,0]==cc:
                printvv("Libro encontrado !!")
                printa(f"Codigo del libro :{libros[i,0]}")
                printv(f"Titulo del libro :{libros[i,1]}")
                printa(f"Autor  del libro :{libros[i,2]}")
                printv(f"Precio del libro :{libros[i,3]}")
                return True
        printr("Libro no encontrado")     
    elif opcion==3:
        printv("IMPRIMIR DOCUMENTOS")
        print("1) Criticas ")
        print("2) Detalles ")
        cert = int(input("Seleccione :"))

        if cert==1:
            c=int(input("Ingrese el codigo del libro :"))
            limpiarpantalla()
            for i in range(10):
                if libros[i,0]==c:
                    printvv(f"""
                            
                    Codigo: {libros[i,0]}
                    Titulo del libro: {libros[i,1]}
                    --------------------------------------
                             Critcas del libro
                    ---------------------------------------
                    1) {Criticas[random.randint(0,8)]}
                    2) {Criticas[random.randint(0,8)]}
                    3) {Criticas[random.randint(0,8)]}
                    4) {Criticas[random.randint(0,8)]}
                    """)
                    return True
            printr("Libro no encontrado")
        elif cert==2:
            printvv("Certificado de detalle de ventas")
            c=int(input("Ingrese el codigo del libro :"))
            limpiarpantalla()
            for i in range(10):
                total=random.randint(0,100)
                if libros[i,0]==c:
                    printvv(f"""
                            
                    Codigo: {libros[i,0]}
                    Titulo del libro: {libros[i,1]}
                    ------------------------------
                         DETALLE DE VENTAS
                    ------------------------------
                    Total vendido: {total}
                    Total recaudado: {total*libros[i,3]}
                    """)
                    return True
            printr("Libro no encontrado")
        else:
            printr("Certificado no valido")
    else:
        printr("OPCION INVALIDA")
