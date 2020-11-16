import psycopg2
from  conexion import dc
conexion=psycopg2.connect(**dc)

def crear (nombre,descripcion):
    cursor = conexion.cursor()

    sql = 'insert into  Proyectos(nombre, descripcion) values(%s, %s)'

    parametros = (nombre,descripcion)

    cursor.execute(sql, parametros)

    conexion.commit()

    cursor.close()

   
    
def consultar():


    Cursor = conexion.cursor()

    Cursor.execute('select * from Proyectos ')

    filas= Cursor.fetchall()

    for fila in filas:
        id=fila[0]
        nombre= fila[1]
        descripcion=fila[2]
        print(f'id={id}\tnombre={nombre}\t descripcion={descripcion}')
    Cursor.close()
    conexion.close()

crear ("prueba dos","prueba02")
consultar()
