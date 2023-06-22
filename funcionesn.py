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
        if None in libros():
            c=int(input("Ingrese el codigo del libro :"))
            if validarcod(c)<0:
                tit=input("Ingrese el nombre del autor :").capitalize()
            else:
                printr("El codigo esta repetido")
        else:
            printr("No hay espacio disponible")    
    elif opcion==2:
        printv("BUSCAR LIBRO")
    elif opcion==3:
        printv("IMPRIMIR DOCUMENTOS")
        print("1) Criticas ")
        print("2) Detalles ")
        cert = int(input("Seleccione :"))

        if cert==1:
            printv("Certificado de criticas ")
        elif cert==2:
            printv("Certificado de detalle de ventas")
        else:
            printr("Certificado no valido")
    else:
        printr("OPCION INVALIDA")