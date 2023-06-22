#llamamos a las funciones a utilizar
from colorama import Style,Fore,Back
import numpy
import os 
import msvcrt
import random

#crear el arreglo de los productos
productos=numpy.empty([10,5], object)

#######################################
#DISEÑO

def printr(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def printv(texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def printa(texto):
    print(f"{Fore.YELLOW}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def printb(texto):
    print(f"{Fore.BLUE}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def titulo(texto):
    printv("-------------------------")
    printb(f"     {texto.upper()}")
    printv("-------------------------")

def limpiarpantalla():
    printa("<<Presione una tecla para continuar>>")
    msvcrt.getch()
    os.system("cls")


#####################
#OPERACIONES PARA EL ARREGLO

#Validar codigo: recorrer el arreglo y encontrar un codigo. si lo encuentra
#retornaremos la posicion , sino lo encuentra retornaremos un valor negativo
def validarcodigo(codigo):
    for i in range (10):
        if productos[i,0]==codigo:
            return i #retornamos la posicion si lo encontramos
    return -1 #sino lo encontramos retornamos negativo

#Guardar
def guardar(codigo,nombre,descripcion,precio,stock):
    if None in productos: #Validamos que haya espacio disponible
        if validarcodigo(codigo)<0: #si es negativo es porque no lo encontro
            if len(nombre)>=3: #validamos que el nombre tenga a lo menos 3 caracteres 
                if precio>=0: #validamos que el precio no sea negativo
                    if stock>=0: #validamos que el stock no sea negaivo
                        for i in range(10): #Recorremos las posiciones del arreglo 
                            if productos[i,0]==None: #verificamos si el espacio esta desocupado
                                productos[i,0]=codigo
                                productos[i,1]=nombre
                                productos[i,2]=descripcion
                                productos[i,3]=precio
                                productos[i,4]=stock
                                printv(f"Producto {nombre} Registrado")
                                break
                    else:
                        printr("El stoc no puede ser negativo")
                else:
                    printr("El precio no puede ser negativo")
            else:
                printr("El nombre debe tener a lo menos 3 caracteres ")
        else:
            printr("El codigo esta repetido")
    else:
        printr("No hay espacio disponible ")

#Listar
def listar():
    for i in range(10):
        if productos[i,0]!=None:
            if productos[i,4]>0:
                printa(f"{productos[i,0]} {productos[i,1]} {productos[i,2]} ${productos[i,3]} stock: {productos[i,4]}")
            else:
                printr (f"{productos[i,0]} {productos[i,1]} SIN STOCK")

#Certificado
opiniones = []
opiniones.append("Producto muy bueno")
opiniones.append("Producto malito")
opiniones.append("Esta vencido")
opiniones.append("He visto mejores")
opiniones.append("Sin comentarios")
opiniones.append("Lo mejor de la vida")
opiniones.append("Lo mejor que puedes encontrar en el sector")
opiniones.append("Primer comentario :D")
opiniones.append("Tengo el mismo producto pero mas barato lamame al 991959693")
opiniones.append("Like si ves en el 2023")

def certificadoopiniones(codigo):
    posicion=validarcodigo(codigo)
    if posicion>=0:
        print(f"""{Fore.BLUE}
        --------------------------------------
        CERTIFICADO DE OPINIONES DE {productos[posicion,1]}
        --------------------------------------
        Descripcion : {productos[posicion,2]}
        Precio      $ {productos[posicion,3]}
        Stock       : {productos[posicion,4]}
        --------------------------------------
        comentario 1: {opiniones[random.randint(0,9)]}         
        comentario 2: {opiniones[random.randint(0,9)]}         
        comentario 3: {opiniones[random.randint(0,9)]} 
        --------------------------------------        
        {Fore.RESET}""")
    else:
        printr("Codigo no encontrado")
