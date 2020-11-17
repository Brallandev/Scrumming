import psycopg2

from  conexion import dc
is_connection= True
try:
     conexion=psycopg2.connect(**dc)

except :
    print("No se pudo conectar a la base de datos")
    is_connection=False
    input("\n"+"Pulse una tecla para Salir")
    exit()



def crear (nombre,descripcion):
    if is_connection==True:
        cursor = conexion.cursor()

        sql = 'insert into  Proyectos(nombre, descripcion) values(%s, %s)'

        parametros = (nombre,descripcion)

        cursor.execute(sql, parametros)

        conexion.commit()

        cursor.close()

        print("El proyecto "+ nombre +" se creo correctamente")

    


def correr_inicio():

    print("---CREACION DE PROYECTO---")

    while True:

        nombre = input("\n"+"Nombre del Proyecto: ")
        validar = len(nombre)

        if validar <= 200:
            break

        print("El contenido escrito supera el parametro de 200 caracteres, intentelo nuevamente")


    while True:

        descripcion = input("\n"+"Descripcion del Proyecto: ")
        validar = len(descripcion)

        if validar <= 1000:
            break

        print("El contenido escrito supera el parametro de 1000 caracteres, intentelo nuevamente")    

        
    
    crear(nombre,descripcion)

    input("pulse la tecla para continuar: ")