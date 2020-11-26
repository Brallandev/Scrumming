import psycopg2

# Se realizara la debida conexion con la base de datos postgres 
# que se encuentra alojada en AWS

conexion=None
cursor=None

dc = {
    'host' : 'database-1.cpdwyuazzw9j.us-east-1.rds.amazonaws.com',
    'database' : 'Proyecto_scrum_2020',
    'user' : 'postgres',
    'password' : 'proyecto_programacion'
}

def get_conexion():
    global conexion,dc
    try:
     conexion=psycopg2.connect(**dc)
     return conexion
    except :
        print("No se pudo conectar a la base de datos")
        input("\n"+"Pulse una tecla para Salir")
        exit()

def get_cursor():

    global Cursor

    try:
     Cursor = conexion.cursor()
     return Cursor
    except :
        print("No se pudo conectar a la base de datos")
        input("\n"+"Pulse una tecla para Salir")
        exit()

def desconectar():
    global conexion,Cursor
    Cursor.close()
    conexion.close()

