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
#datos de ingreso son modificacion y opcion_actualizar
#modificacion recibe la informacion actualizada de alguno de los campos de las opciones dentro del user
#opciones 1,2,3 y 4
#1 nombre
#2 card
#3 conversation
#4 confirmation
#esta funcion conecta a la base de datos para realizar el update
def actualizar(id, opcion_actualizar, modificacion):
    if opcion_actualizar == 1:

        cursor = conexion.cursor()
        sql = 'update UserStories set nombre=%s where id=%s'
        parametros = (modificacion, id)
        cursor.execute(sql, parametros)
        conexion.commit()
        cursor.close()

    elif opcion_actializar == 2:
        cursor = conexion.cursor()
        sql = 'update UserStories set card=%s where id=%s'
        parametros = (modificacion, id)
        cursor.execute(sql, parametros)
        conexion.commit()
        cursor.close()

    elif opcion_actualizar == 3:
         cursor = conexion.cursor()
        sql = 'update UserStories set conversation=%s where id=%s'
        parametros = (modificacion, id)
        cursor.execute(sql, parametros)
        conexion.commit()
        cursor.close()
        
    elif opcion_actualizar == 4:
           cursor = conexion.cursor()
        sql = 'update UserStories set confirmation=%s where id=%s'
        parametros = (modificacion, id)
        cursor.execute(sql, parametros)
        conexion.commit()
        cursor.close()

    else:
        print('esta opcion no es correcta')

conexion.close()

