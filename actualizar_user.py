import psycopg2
import conexion_BD
is_connection= True

    
#datos de ingreso es opcion_actualizar
#modificacion recibe la informacion actualizada de alguno de los campos de las opciones dentro del user
#opciones 1,2,3 y 4
#1 nombre
#2 card
#3 conversation
#4 confirmation
#esta funcion conecta a la base de datos para realizar el update

def actualizar(id, opcion_actualizar):

    print(id)
    print(opcion_actualizar)
    
    conexion=conexion_BD.get_conexion()
    cursor=conexion_BD.get_cursor()

    if opcion_actualizar == 1:

        sql = 'update UserStories set nombre=%s where codigo=%s'

        while True:

         nombre = input("\n"+"Nuevo nombre del user storie: ")
         validar = len(nombre)

         if validar <= 500 and validar > 0:
             break

         print("El contenido escrito supera el parametro de 500 caracteres, intentelo nuevamente")

        parametros = (str(nombre), str(id))
        cursor.execute(sql, parametros)
        conexion.commit()
        


    elif opcion_actualizar == 2:

        cursor = conexion.cursor()
        
        sql = 'update UserStories set card=%s where codigo=%s'
        
        card = input("\n"+"Nuevo card del user storie: ")

        parametros = (str(card), str(id))
        cursor.execute(sql, parametros)
        conexion.commit()
        

    
    elif opcion_actualizar == 3:

        cursor = conexion.cursor()
        
        sql = 'update UserStories set conversation=%s where codigo=%s'

        conversation = input("\n"+"Nuevo conversation del user storie: ")

        parametros = (str(conversation), str(id))
        cursor.execute(sql, parametros)
        conexion.commit()
        

        
    elif opcion_actualizar == 4:

        cursor = conexion.cursor()
        
        sql = 'update UserStories set confirmation=%s where codigo=%s'
       
        confirmation = input("\n"+"Nuevo confirmation del user storie: ")

        parametros = (str(confirmation), str(id))
        cursor.execute(sql, parametros)
        conexion.commit()


    else:
        input('esta opcion no es correcta')     
    
    conexion_BD.desconectar()


