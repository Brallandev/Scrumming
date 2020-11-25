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


def creacion(codigo,nombre,card,conversation,confirmation):
    if is_connection==True:
        cursor = conexion.cursor()

        sql= 'insert into UserStories(codigo,nombre,card,conversation,confirmation) values (%s, %s, %s, %s, %s)'

        parametros= (codigo,nombre,card,conversation,confirmation)
        cursor.execute(sql, parametros)

        conexion.commit()

        cursor.close()

        print("El User Storie "+ nombre +" se creo correctamente")


def correr():
    print("---CREACION DE USER STORIE---")

    while True:
        codigo = input("\n"+"Codigo del user storie: ")
        validar = len(codigo)

        if validar <= 45:
            break

        print("El contenido escrito supera el parametro de 45 caracteres, intentelo nuevamente")
    

    while True:

        nombre = input("\n"+"Nombre del user storie: ")
        validar = len(nombre)

        if validar <= 500:
            break

        print("El contenido escrito supera el parametro de 500 caracteres, intentelo nuevamente")


    while True:

        card = input("\n"+"Card del user storie: ")
        

    while True:

        conversation = input("\n"+"conversation del user storie: ")
        
    while True:

        confirmation = input("\n"+"Confirmation del user storie: ")
    
    creacion(codigo,nombre,card,conversation,confirmation)

    input("pulse la tecla para continuar: ")
       
