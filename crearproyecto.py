<<<<<<< HEAD
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
=======
print("*******  Este es el inicio para la creacion de un nuevo Proyecto  **********")
print("1. Crear un nuevo Proyecto ")
print("2. Salir ")
opcion= int(input("Digite la opcion deseada: "))
if opcion==1:
    print("Que nombre de proyecto desea")
    nombre_proyecto=input()
    print(f"El nombre del proyecto es : {nombre_proyecto}")
    print("Desea agregar descripcion de su proyecto")
    descripcion_proyecto=input()
    print(f"Su descripcion es : {descripcion_proyecto}")
else:
     print("Usted ha decidido salir de creacion de proyecto")   
   
print("end")
>>>>>>> b5d3002e7f9c75ffc80201537638f146c3f0d24f
