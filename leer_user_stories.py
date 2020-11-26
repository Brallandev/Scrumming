import psycopg2
import Utilidades
import Proyecto_y_user_stories
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

  




def consultar():

    global Validacion
    Validacion = []
    if is_connection==True:

        Cursor.execute('select * from UserStories ')

        filas= Cursor.fetchall()

        for fila in filas:
            id=fila[0]
            Validacion.append(id)
            nombre= fila[1]
            descripcion=fila[2]
            print(f'[{id}] {nombre} \n')
            print(f'Descripcion:{descripcion}'+"\n")
