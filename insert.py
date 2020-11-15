import psycopg2
from  conexion import dc

conexion = psycopg2.connect(**dc)

cursor = conexion.cursor()

sql = 'insert into  Proyectos(nombre, descripcion) values(%s, %s)'

parametros = ('P.a.p.o.', 'Barras,Barras')

cursor.execute(sql, parametros)

conexion.commit()

cursor.close()

conexion.close()
