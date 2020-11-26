import psycopg2
import Utilidades
import actualizar_user
import Proyecto_y_user_stories
import leer_user_stories
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

Validacion = []

#se consulta el id del user storie
def Consulta(id):

    global Validacion

    if is_connection==True:

       sql = 'select * from UserStories where id=%s'
       parametro = (str(id))
       Validacion = leer_user_stories.consulta_general(id)
       Cursor.execute(sql, parametro)



#Se seleccionara el user storie el cual se va a editar

def seleccionar_user_storie():

    global Validacion

    print(Validacion)

    Opcion = int(input("Digite el numero del User Storie que quiere modificar: "))

    Valor_Verificacion= Opcion in Validacion

    if Valor_Verificacion == True:

        modificacion_BD(Opcion)
        input("esto esta sirviendo presione para continuar: ")

    
    
    else:
        print("\n"+"El valor seleccionado no existe, vuelva a intentarlo"+"\n")
        input("Esto no esta sirviendo")



#Se realizara la modificacion en la base de datos

def modificacion_BD(id):

    global Validacion

    Utilidades.clear()

    print("¿Que desea modificar del user storie?"+"\n")
    print("1) Nombre"+"\n")
    print("2) Card"+"\n")
    print("3) Conversation"+"\n")
    print("4) Confirmation"+"\n")
    print("5) Salir")

    Opcion = 0
   
    Opcion = int(input("Digite la opcion de lo que desea modificar en el user: "))

    
    if Opcion != 5:

        actualizar_user.actualizar(id,Opcion)
        modificacion_BD(id)

def Correr(id):

    Consulta(id)
    seleccionar_user_storie()
   
