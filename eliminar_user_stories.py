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

def eliminar(id):
    cursor = conexion.cursor()
    sql = 'delete from UserStories where id=%s'
    parametros = (id)
    cursor.execute(sql, parametros)
    conexion.commit()
    cursor.close()
conexion.close()