import psycopg2
from conexion import dc

is_connection=True

try:
     conexion=psycopg2.connect(**dc)
     Cursor = conexion.cursor()

except :
    print("No se pudo conectar a la base de datos")
    is_connection=False
    input("\n"+"Pulse una tecla para Salir")
    exit()


Validacion = []

def consultar():

    global Validacion

    if is_connection==True:

        Cursor.execute('select * from Proyectos ')

        filas= Cursor.fetchall()

        for fila in filas:
            id=fila[0]
            Validacion.append(id)
            nombre= fila[1]
            descripcion=fila[2]
            print(f'[{id}] {nombre} \n')
            print(f'Descripcion:{descripcion}'+"\n")
        
        
    
def consulta_especifica(id):

    if is_connection==True:
        sql ='select * from Proyectos where id=%s'
        parametros=(str(id))
        Cursor.execute(sql,parametros)

        filas= Cursor.fetchall()
        
        datos=[]

        for fila in filas:
            datos.append(fila[0])
            datos.append(fila[1])
            datos.append(fila[2])

        Cursor.close()

        return datos

        

def seleccionar_proyecto():

    global Validacion

    consultar()

    Opcion = int(input("Digite el numero del proyecto que desea ver: "))

    Valor_Verificacion= Opcion in Validacion

    if Valor_Verificacion == True:
        Ejecutar_Seleccion(Opcion)
    
    else:
        print("\n"+"El valor seleccionado no existe, vuelva a intentarlo"+"\n")
        seleccionar_proyecto()


<<<<<<< HEAD
def Ejecutar_Seleccion(Opcion):
=======
def Ejecutar_Seleccion():

    print("Ejecutar seleccion")

>>>>>>> 783d89ecc28368f5642c93a59848718518d13678

    #recibe los datos del proyecto selecionado en un arreglo.
    buscar=consulta_especifica(Opcion)






