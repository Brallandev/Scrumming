import psycopg2
import conexion_BD


#esta opcion conecta a la base de datos para realizar la elminacion de campos que se encuentran alli

Menu_eliminar = ( 
    
    "Esta seguro de que quiere eliminar este Proyecto"+"\n"
    "RECUERDE QUE LOS USER STORIES DEL PROYECTO SERAN ELIMINADOS"+"\n"
    "1) Si"+"\n"
    "2) No"+"\n"
    )

def eliminar(id):

    global Menu_eliminar

    conexion=conexion_BD.get_conexion()
    cursor = conexion_BD.get_cursor()

    print(Menu_eliminar)

    opcion = input("Ingrese la opcion que desee realizar:")

    if opcion == "1":
        sql = 'delete from Userstories where idproyecto=%s; delete from proyectos where id=%s'
        parametros = (str(id),str(id))
        cursor.execute(sql, parametros)

    elif opcion =="2":
        print("Saliendo")

    else:
        input("la opcion escogida no es valida, pulse una tecla para confirmar \n")
        eliminar(id)

    conexion.commit()
    conexion_BD.desconectar()