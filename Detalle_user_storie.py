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

Validacion = []

#Se hace la consulta del User storie en la base de datos

def Consulta():
 global Validacion
        
    if is_connection==True:

     Cursor.execute('select * from UserStories')

     filas= Cursor.fetchall()

      for fila in filas:
         id=fila[0]
         Validacion.append(id)
         codigo=fila[1]
         nombre=fila[2]
         card=fila[3]
         conversation=fila[4]
         confirmation=fila[5]
         print(f'[{id}] {nombre} \n')
         print(f'Codigo del user:{codigo}'+"\n")
         print(f'Card del user:{card}'+"\n")
         print(f'Conversation del user:{Conversation}'+"\n")
         print(f'Confirmation del user:{codigo}'+"\n")




#Se seleccionara el user storie
  def seleccionar_user_storie():

    global Validacion

    consulta()

    Opcion = int(input("Digite el numero del User Storie que se mostrara: "))

    Valor_Verificacion= Opcion in Validacion

    if Valor_Verificacion == True:
        Proyecto_y_user_stories.Ejecutar_Seleccion(Opcion)
        Proyecto_y_user_stories.Opciones_UStories()
    
    else:
        print("\n"+"El valor seleccionado no existe, vuelva a intentarlo"+"\n")
        seleccionar_proyecto()

seleccionar_proyecto()
