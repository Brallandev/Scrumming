import psycopg2
from  conexion import dc



conexion=psycopg2.connect(**dc)

Cursor = conexion.cursor()

Cursor.execute('select * from Proyectos ')

filas= Cursor.fetchall()

for fila in filas:
    id=fila[0]
    nombre= fila[1]
    print(f'id={id}\tnombre={nombre}')
Cursor.close()
conexion.close()
