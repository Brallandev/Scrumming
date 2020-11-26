import psycopg2
import Utilidades
import Proyecto_y_user_stories
import leer_user_stories



#Se seleccionara el user storie
def seleccionar_user_storie(id_proyecto):

    global Validacion

    Validacion=leer_user_stories.consulta_general(str(id_proyecto))

    Opcion = input("Digite el codigo del user storie:")

    Valor_Verificacion= Opcion in Validacion

    if Valor_Verificacion == True:
        leer_user_stories.consulta_especifica(Opcion)
        return Opcion
    
    if len(Validacion) ==0:
        print('no hay user stories creados hasta la fecha')
    
    else:
        Utilidades.clear()
        print("\n"+"El valor seleccionado no existe o pertenece a otro proyecto, vuelva a intentarlo"+"\n")
        seleccionar_user_storie(id_proyecto)

