import psycopg2
import Utilidades
import actualizar_user
import Proyecto_y_user_stories
import leer_user_stories
import conexion_BD

Validacion = []

#se consulta el id del user storie
def Consulta(id):

    conexion=conexion_BD.get_conexion()
    Cursor=conexion_BD.get_cursor()

    global Validacion

    sql = 'select * from UserStories where id=%s'
    parametro = (str(id))
    Validacion = leer_user_stories.consulta_general(id)
    Cursor.execute(sql, parametro)
    
    conexion_BD.desconectar()



#Se seleccionara el user storie el cual se va a editar

def seleccionar_user_storie():

    global Validacion

    print(Validacion)

    Opcion = input("Digite el [CODIGO] del User Story que quiere modificar: ")

    Valor_Verificacion= Opcion in Validacion

    if Valor_Verificacion == True:

        modificacion_BD(Opcion)
        input("Modificacion realizada con exito, Pulse una tecla para continuar")
    
    else:
        print("\n"+"El valor seleccionado no existe o pertenece a otro proyecto"+"\n")
        seleccionar_user_storie()


        



#Se realizara la modificacion en la base de datos

def modificacion_BD(id):

    global Validacion

    Utilidades.clear()
    print('\n'+"OPCIONES DE EDICION"+"\n")
    print("-------------------------------------"+"\n")
    print("¿Que desea modificar del user storie?"+"\n")
    print("1) Nombre"+"\n")
    print("2) Card"+"\n")
    print("3) Conversation"+"\n")
    print("4) Confirmation"+"\n")
    print("5) Salir")

    Opcion = 0
   
    Opcion = (input("Digite la opcion de lo que desea modificar en el user: "))

    while True:

        if  Opcion.isnumeric():
            Opcion=int(Opcion)
            break

        Utilidades.clear()
        print('Solo se aceptan valores numericos,vuelva a intentarlo \n')
        modificacion_BD(id)

    
    if Opcion != 5:

        actualizar_user.actualizar(id,Opcion)
        modificacion_BD(id)

    elif Opcion == 5:
        print("saliendo")


def Correr(id):

    Consulta(id)
    seleccionar_user_storie()
   
