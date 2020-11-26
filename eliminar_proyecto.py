import psycopg2

from  conexion import dc
is_connection= True

try:
     conexion=psycopg2.connect(**dc)
     cursor = conexion.cursor()

except :
    print("No se pudo conectar a la base de datos")
    is_connection=False
    input("\n"+"Pulse una tecla para Salir")
    exit()

#esta opcion conecta a la base de datos para realizar la elminacion de campos que se encuentran alli

Menu_eliminar = ( 
    
    "Esta seguro de que quiere eliminar este User UserStories "+"\n"
    "1) Si"+"\n"
    "2) No"+"\n"
    )

def eliminar(id):

    global Menu_eliminar

    cursor = conexion.cursor()

    print(Menu_eliminar)

    opcion = input("Ingrese la opcion que desee realizar")

    if opcion == "1":
        sql = 'delete from Proyectos where codigo=%s'
        parametros = (id)
        cursor.execute(sql, parametros)

    elif opcion =="2":
        print("Saliendo")

    else:
        input("la opcion escogida no es valida, pulse una tecla para volver a escojer")
        eliminar(id)



    conexion.commit()
    cursor.close()