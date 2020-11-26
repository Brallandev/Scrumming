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
    

#Se seleccionara el user storie
def seleccionar_user_storie():

    global Validacion

    Consulta(id)

    Opcion = int(input("Digite el numero del User Storie que se mostrara: "))

    Valor_Verificacion= Opcion in Validacion

    if Valor_Verificacion == True:
        Proyecto_y_user_stories.Ejecutar_Seleccion(Opcion)
        Proyecto_y_user_stories.Opciones_UStories()
    
    else:
        print("\n"+"El valor seleccionado no existe, vuelva a intentarlo"+"\n")
        seleccionar_user_storie()

seleccionar_user_storie()