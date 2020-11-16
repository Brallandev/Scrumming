import psycopg2
from datos_conexion import dc

is_connection=True

def consultar():
    if is_connection==True:

        Cursor = conexion.cursor()

        Cursor.execute('select * from Proyectos ')

        filas= Cursor.fetchall()

        for fila in filas:
            id=fila[0]
            nombre= fila[1]
            descripcion=fila[2]
            print(f'[{id}] {nombre} \n')
            print(f'Descripcion:{descripcion}')
        Cursor.close()
        conexion.close()
