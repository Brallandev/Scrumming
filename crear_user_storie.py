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


def creacion(codigo,nombre,card,conversation,confirmation,id_proyecto):

    if is_connection==True:
        cursor = conexion.cursor()

        sql= 'insert into UserStories(codigo,nombre,card,conversation,confirmation,idproyecto) values (%s, %s, %s, %s, %s, %s)'

        parametros= (codigo,nombre,card,conversation,confirmation,id_proyecto)
        cursor.execute(sql, parametros)

        conexion.commit()

        cursor.close()

        print("El User Storie "+ nombre +" se creo correctamente")


def correr(id):

    print("---CREACION DE USER STORIE---")

    while True:
        codigo = input("\n"+"Codigo del user storie: OBLIGATORIO, MAX:45 \n")
        validar = len(codigo)

        if validar <= 45 and validar>0:
            break

        print("El codigo no cumple con los parametros, intentelo nuevamente\n")
    

    while True:

        nombre = input("\n"+"Nombre del user storie:OBLIGATORIO, MAX:500\n")
        validar = len(nombre)

        if validar <= 500 and validar>0:
            break

        print("El Nombre no cumple con los parametros, intentelo nuevamente\n")


    
    
    card = input("\n"+"Card del user storie: ")
            
    conversation = input("\n"+"conversation del user storie: ")
              
    confirmation = input("\n"+"Confirmation del user storie: ")

    id_proyecto = id
    
    creacion(codigo,nombre,card,conversation,confirmation,id_proyecto)

    input("pulse la tecla para continuar: ")
    
       
