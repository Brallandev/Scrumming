import psycopg2
import Utilidades
import Proyecto_y_user_stories
import conexion_BD

def consulta_general(id_proyecto):

    Validacion = []

    conexion=conexion_BD.get_conexion()
    Cursor=conexion_BD.get_cursor()
    
    sql='select * from UserStories where idproyecto=%s'

    parametro = (str(id_proyecto))
    Cursor.execute(sql, parametro)

    filas= Cursor.fetchall()
    
    print('\n USER STORIES DEL PROYECTO: \n')
    print('---------------------------- '+"\n")
    
    if len(filas)==0:
        print('Este proyecto no tiene User Stories \n')

    for fila in filas:
        codigo=fila[1]
        Validacion.append((codigo))
        nombre= fila[2]
        print(f'Codigo:[{codigo}]       Nombre:{nombre}\n\n')
    

    conexion_BD.desconectar()
    return Validacion    
            
def consulta_especifica(codigo_user):
    
    conexion=conexion_BD.get_conexion()
    Cursor=conexion_BD.get_cursor()

    sql = f"select * from UserStories where codigo='{codigo_user}'"
    Cursor.execute(sql)
    filas = Cursor.fetchall()

    for fila in filas:
        codigo=fila[1]
        nombre=fila[2]
        card=fila[3]
        conversation=fila[4]
        confirmation=fila[5]

        print('==================================\n')
        print(f'[{codigo}] {nombre}\n')
        print('==================================\n')
        print(f'card->{card}\n')
        print(f'conversation->{conversation}\n')
        print(f'confirmation->{confirmation}\n')
        print('\n\n')
        input("Pulse una tecla para continuar: ")
        
    conexion_BD.desconectar()  

    return codigo

def buscar_existencia(codigo_user):

    conexion=conexion_BD.get_conexion()
    cursor=conexion_BD.get_cursor()

    sql=f"select * from userstories where codigo ='{codigo_user}'"
    cursor.execute(sql)
    fila=cursor.fetchall()
    if len(fila)!=0:
        print(f'El user story con el codigo {codigo_user} ya existe en la base de datos')
        return True
    else:
        return False
