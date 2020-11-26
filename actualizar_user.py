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
    
#datos de ingreso es opcion_actualizar
#modificacion recibe la informacion actualizada de alguno de los campos de las opciones dentro del user
#opciones 1,2,3 y 4
#1 nombre
#2 card
#3 conversation
#4 confirmation
#esta funcion conecta a la base de datos para realizar el update
def actualizar(id, opcion_actualizar):
    if opcion_actualizar == 1:

        cursor = conexion.cursor()
        sql = 'update UserStories set nombre=%s where id=%s'

        while True:

         nombre = input("\n"+"Nuevo nombre del user storie: ")
         validar = len(nombre)

         if validar <= 500:
             break

         print("El contenido escrito supera el parametro de 500 caracteres, intentelo nuevamente")

        parametros = (nombre, id)
        cursor.execute(sql, parametros)
        conexion.commit()
        cursor.close()


    elif opcion_actualizar == 2:
        cursor = conexion.cursor()
        sql = 'update UserStories set card=%s where id=%s'
        while True:
         card = input("\n"+"Nuevo card del user storie: ")

        parametros = (card, id)
        cursor.execute(sql, parametros)
        conexion.commit()
        cursor.close()

    
    elif opcion_actualizar == 3:
        cursor = conexion.cursor()
        sql = 'update UserStories set conversation=%s where id=%s'

        while True:
         conversation = input("\n"+"Nuevo conversation del user storie: ")

        parametros = (conversation, id)
        cursor.execute(sql, parametros)
        conexion.commit()
        cursor.close()

        
    elif opcion_actualizar == 4:
        cursor = conexion.cursor()
        sql = 'update UserStories set confirmation=%s where id=%s'
        while True:
         confirmation = input("\n"+"Nuevo confirmation del user storie: ")

        parametros = (confirmation, id)
        cursor.execute(sql, parametros)
        conexion.commit()
        cursor.close()

    else:
        print('esta opcion no es correcta')

conexion.close()

