import psycopg2

import conexion_BD


def crear (nombre,descripcion):
    
    conexion=conexion_BD.get_conexion()
    cursor=conexion_BD.get_cursor()

    sql = 'insert into  Proyectos(nombre, descripcion) values(%s, %s)'

    parametros = (nombre,descripcion)

    cursor.execute(sql, parametros)

    conexion.commit()

    conexion_BD.desconectar()

    print("El proyecto "+ nombre +" se creo correctamente")

    


def correr_inicio():

    print("---CREACION DE PROYECTO---")

    while True:

        nombre = input("\n"+"Nombre del Proyecto obligatorio MAX:200: ")
        validar = len(nombre)

        if validar <= 200 and validar > 0:
            break

        print("El contenido escrito no cumple con las condiciones esperadas, intentelo nuevamente")


    while True:

        descripcion = input("\n"+"Descripcion del Proyecto: ")
        validar = len(descripcion)

        if validar <= 1000:
            break

        print("El contenido escrito supera el parametro de 1000 caracteres, intentelo nuevamente")    

        
    
    crear(nombre,descripcion)

    input("pulse la tecla para continuar: ")