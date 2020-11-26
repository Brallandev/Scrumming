import psycopg2
import Utilidades
from conexion import dc

is_connection=True

try:
     conexion=psycopg2.connect(**dc)
     Cursor = conexion.cursor()

except :
    print("No se pudo conectar a la base de datos")
    is_connection=False
    input("\n"+"Pulse una tecla para Salir")
    exit()

Proyecto = 0

def consulta_especifica(id):

    if is_connection==True:
        sql ='select * from Proyectos where id=%s'
        parametros=(str(id))
        Cursor.execute(sql,parametros)

        filas= Cursor.fetchall()
        
        datos=[]

        for fila in filas:
            datos.append(fila[0])
            datos.append(fila[1])
            datos.append(fila[2])

        Cursor.close()

        return datos




def Ejecutar_Seleccion(Opcion):

    global Proyecto

    Utilidades.clear()

    #recibe los datos del proyecto selecionado en un arreglo.

    buscar = consulta_especifica(Opcion)

    contador = len(buscar)

    fila = 0 

    p1=0
    p2=0
    p3=0

    while fila < contador:

        if fila == 0:

            p1= ("Codigo de Proyecto: "+ str( buscar[fila])+"\n")
            print(p1)


        elif fila == 1:

            p2 = ("Nombre de Proyecto: "+ str(buscar[fila])+"\n")
            print(p2)

        elif fila == 2:

            p3 = ("Descripcion del Proyecto: "+ str(buscar[fila])+"\n")
            print(p3)

        
        fila = fila+1

    Proyecto=(p1+p2+p3)
    

 
Menu_UStroies = (
    "1) Crear User Storie"+"\n"
    "2) Ver User Storie"+"\n"
    "3) Editar User Storie"+"\n"
    "4) Eliminar User Storie"+"\n"
    "5) Salir"+"\n")

def Opciones_UStories():

    global Proyecto

    print(Proyecto)

    print(Menu_UStroies)

    Opcion = int(input("cual opcion desea escoger: "))

    if Opcion == 1:
        
        Utilidades.clear()
        print("Crear User Storie")
        input("Pulse una tecla para continuar")
        Utilidades.clear()
        Opciones_UStories()

    elif Opcion == 2:

        Utilidades.clear()
        print("Ver User Storie")
        input("Pulse una tecla para continuar")
        Utilidades.clear()
        Opciones_UStories()
    
    elif Opcion == 3:

        Utilidades.clear()
        print("Editar User Storie")
        input("Pulse una tecla para continuar")
        Utilidades.clear()
        Opciones_UStories()

    elif Opcion == 4:

        Utilidades.clear()
        print("Eliminar User Storie")
        input("Pulse una tecla para continuar")
        Utilidades.clear()
        Opciones_UStories()

    elif Opcion == 5:

        Utilidades.clear()
        print("Salir")
        input("Pulse una tecla para continuar")
        Utilidades.clear()
        Opciones_UStories()
    
    else:

        input("La seleccion escogida no existe, pulse cualquier tecla para intentarlo nuevamente")

        Opciones_UStories()
