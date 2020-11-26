import psycopg2
import Utilidades
import Proyecto_y_user_stories
import conexion_BD

Validacion = []

def consultar():

    global Validacion
    
    conexion=conexion_BD.get_conexion()
    Cursor=conexion_BD.get_cursor()
        
    Cursor.execute('select * from Proyectos')

    filas= Cursor.fetchall()

    for fila in filas:
        id=fila[0]
        Validacion.append(id) 
        nombre= fila[1]
        descripcion=fila[2]
        print(f'[{id}] {nombre} \n')
        print(f'Descripcion:{descripcion}'+"\n")

    conexion_BD.desconectar()
        

def seleccionar_proyecto():

    global Validacion

    consultar()
    if len(Validacion) == 0:
        print('no se han creado proyectos hasta la fecha')
        input('pulse una tecla para continuar')
    else:

        Opcion = input("Digite el numero del proyecto que desea ver: ")

        while True:

            if Opcion.isnumeric():
                Opcion=int(Opcion)
                break

            Utilidades.clear()
            print('Solo se aceptan valores numericos,vuelva a intentarlo \n')
            seleccionar_proyecto()    

        Valor_Verificacion= Opcion in Validacion

        if Valor_Verificacion == True:
            Proyecto_y_user_stories.Ejecutar_Seleccion(Opcion)
            Proyecto_y_user_stories.Opciones_UStories()

        else:
            print("\n"+"El valor seleccionado no existe, vuelva a intentarlo"+"\n")
            seleccionar_proyecto()






