import psycopg2
import Utilidades
import crear_user_storie
import leer_user_stories
import Editar_user_storie
import eliminar_user_stories
import Detalle_user_storie
import conexion_BD

#Variables Globales
id_proyecto = 0
Proyecto = 0

def consulta_especifica(id):

    global id_proyecto

    id_proyecto = id

    conexion=conexion_BD.get_conexion()
    Cursor=conexion_BD.get_cursor()
    
    sql ='select * from Proyectos where id=%s'
    parametros=(str(id))
    Cursor.execute(sql,parametros)

    filas= Cursor.fetchall()
    
    datos=[]

    for fila in filas:
        datos.append(fila[0])
        datos.append(fila[1])
        datos.append(fila[2])

    conexion_BD.desconectar()    

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
    print('DATOS DEL PROYECTO \n')
    print('----------------------------')

    while fila < contador:




        if fila == 0:

            p1= ("Codigo de Proyecto: "+ str( buscar[fila])+"\n")
            


        elif fila == 1:

            p2 = ("Nombre de Proyecto: "+ str(buscar[fila])+"\n")
            

        elif fila == 2:

            p3 = ("Descripcion del Proyecto: "+ str(buscar[fila])+"\n")
            

        
        fila = fila+1

    Proyecto=(p1+p2+p3)
    

 
Menu_UStroies = (
    "1) Crear User Story"+"\n"
    "2) Ver User Story"+"\n"
    "3) Editar User Story"+"\n"
    "4) Eliminar User Story"+"\n"
    "5) Salir"+"\n")

def Opciones_UStories():

    global Proyecto

    global id_proyecto

    print(Proyecto)

    leer_user_stories.consulta_general(id_proyecto)

    print(Menu_UStroies)

    Opcion = (input("cual opcion desea escoger: "))


    if Opcion == "1":
        
        Utilidades.clear()
        print("Crear User Storie")
        crear_user_storie.correr(id_proyecto)
        input("Pulse una tecla para continuar")
        Utilidades.clear()
        Opciones_UStories()

    elif Opcion == "2":
        Utilidades.clear()
        codigo_user = Detalle_user_storie.seleccionar_user_storie(id_proyecto)
        Utilidades.clear()
        Opciones_UStories()
    
    elif Opcion == "3":

        Utilidades.clear()
        Editar_user_storie.Correr(id_proyecto)
        Utilidades.clear()
        Opciones_UStories()

    elif Opcion == "4":

        Utilidades.clear()
        codigo_user = Detalle_user_storie.seleccionar_user_storie(id_proyecto)
        eliminar_user_stories.eliminar(codigo_user)
        input("Pulse una tecla para continuar")
        Utilidades.clear()
        Opciones_UStories()

    elif Opcion == "5":

        Utilidades.clear()
        input("Pulse una tecla para Salir")
        Utilidades.clear()

    
    else:

        input("La seleccion escogida no existe, pulse cualquier tecla para intentarlo nuevamente")

        Opciones_UStories()

def id_proyecto_Peticion():

    global id_proyecto
    
    idn = id_proyecto

    return idn

