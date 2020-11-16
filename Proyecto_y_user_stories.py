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

    Utilidades.clear()

    #recibe los datos del proyecto selecionado en un arreglo.

    buscar = consulta_especifica(Opcion)

    contador = len(buscar)

    fila = 0 

    while fila < contador:

        if fila == 0:

            print("Codigo de Proyecto: "+ str( buscar[fila])+"\n")


        elif fila == 1:

            print("Nombre de Proyecto: "+ str(buscar[fila])+"\n")

        elif fila == 2:

            print("Descripcion del Proyecto: "+ str(buscar[fila])+"\n")
        
        fila = fila+1

def Opciones_UStories():

    Menu_UStroies = (

    "1) Crear User Storie"+"\n"
    "2) Ver User Storie"+"\n"
    "3) Editar User Storie"+"\n"
    "4) Eliminar User Storie"+"\n"
    "5) Salir"+"\n"
    )

    print(Menu_UStroies)

    input("todo esta funcionando")