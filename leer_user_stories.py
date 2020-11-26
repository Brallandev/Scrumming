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


def consulta_general(id_proyecto):

    global Validacion

    Validacion = []

    if is_connection==True:

        sql='select * from UserStories where idproyecto=%s'

        parametros = (id_proyecto)
        Cursor.execute(sql, parametro)

        filas= Cursor.fetchall()

        for fila in filas:
            codigo=fila[1]
            Validacion.append(codigo)
            nombre= fila[2]
            print(f'Codigo:{codigo}---Nombre:{nombre}\n\n')

    return validacion;    
            
def consulta_especifica(codigo_user):
    
    if is_connection==True:

       sql = 'select * from UserStories where codigo=%s'
       parametro = (codigo_user)
       Cursor.execute(sql, parametro)
       filas = Cursor.fetchall()

       for fila in filas:
           codigo=fila[1]
           nombre=fila[2]
           card=fila[3]
           conversation=fila[4]
           confirmation=fila[5]

           print('==================================\n')
           print(f'[{codigo}] {Nombre}\n')
           print('==================================\n')
           print(f'card->{card}\n')
           print(f'conversation->{conversation}\n')
           print(f'confirmation->{confirmation}\n')
           print('\n\n')
        
        Cursor.close()

        return codigo

       
       