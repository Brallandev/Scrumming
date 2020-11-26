import psycopg2
import Utilidades
import actualizar_user
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

Validacion = []

#se consulta el id del user storie
def Consulta(id):

    if is_connection==True:

       sql = 'select * from UserStories where id=%s'
       parametro = (id)
       Cursor.execute(sql, parametro)



#Se seleccionara el user storie el cual se va a editar

def seleccionar_user_storie():
    global Validacion


    Opcion = int(input("Digite el numero del User Storie que quiere modificar: "))

    Valor_Verificacion= Opcion in Validacion

    if Valor_Verificacion == True:
        Proyecto_y_user_stories.Ejecutar_Seleccion(Opcion)
        Proyecto_y_user_stories.Opciones_UStories()

    
    
    else:
        print("\n"+"El valor seleccionado no existe, vuelva a intentarlo"+"\n")



#Se realizara la modificacion en la base de datos

def modificacion_BD():

    global Validacion

    print("¿Que desea modificar del user storie?"+"\n")
    print("1) Nombre"+"\n")
    print("2) Card"+"\n")
    print("3) Conversation"+"\n")
    print("4) Confirmation"+"\n")
   
    Opcion = int(input("Digite el valor de lo que desea modificar en el user: "))

    Valor_Verificacion= Opcion in Validacion

    if Valor_Verificacion == True:
        actualizar_user.actualizar(id,Opcion)
    
    else:
        print("\n"+"El valor seleccionado no existe, vuelva a intentarlo"+"\n")


seleccionar_user_storie()
modificacion_BD()