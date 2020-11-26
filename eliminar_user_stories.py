import psycopg2

import conexion_BD
is_connection= True


Menu_eliminar = ( 
    
    "Esta seguro de que quiere eliminar este User UserStories "+"\n"
    "1) Si"+"\n"
    "2) No"+"\n"
    )


def eliminar(id):

    global Menu_eliminar
    
    conexion=conexion_BD.get_conexion()
    cursor = conexion_BD.get_cursor()

    print(Menu_eliminar)

    opcion = input("Ingrese la opcion que desee realizar")

    if opcion == "1":
        sql = f"delete from UserStories where codigo='{id}'"
        cursor.execute(sql)

    elif opcion =="2":
        print("Saliendo")

    else:
        input("la opcion escogida no es valida, pulse una tecla para volver a escojer")
        eliminar(id)



    conexion.commit()
    conexion_BD.desconectar()

