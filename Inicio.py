import crearproyecto
import ver_proyecto
import eliminar_proyecto
import Utilidades

# Menu Proyectos

Menu = (
    "------Menu Scrum------"+"\n"
    "1) Crear Proyecto"+"\n"
    "2) Ver Proyecto"+"\n"
    "3) Eliminar Proyecto"+"\n"
    "4) Salir"+"\n"
    )

def mostrar_menu():
    Utilidades.titulo()
    print(Menu)

mostrar_menu()

# Seleccionar Opcion

def Seleccion ():

    Opcion = input("cual opcion desea escoger: ")

    while True:
        
        if Opcion.isnumeric():
            Opcion=int(Opcion)
            break

        Utilidades.clear()
        print('Solo se aceptan valores numericos,vuelva a intentarlo \n')
        mostrar_menu()
        Seleccion()

    if Opcion == 1:

        Utilidades.clear()
        crearproyecto.correr_inicio()
        Utilidades.clear()
        mostrar_menu()
        Seleccion()  
        
    elif Opcion == 2:
        Utilidades.clear()
        ver_proyecto.seleccionar_proyecto()
        Utilidades.clear()
        mostrar_menu()
        Seleccion()  
    
    elif Opcion == 3:
        Utilidades.clear()
        ver_proyecto.consultar()
        Opcion = int(input("cual opcion desea escoger: "))
        eliminar_proyecto.eliminar(Opcion)
        Utilidades.clear()
        mostrar_menu()
        Seleccion()
        


    elif Opcion == 4:
        exit()

    else:
        print("Opcion incorrecta"+"\n")
        Seleccion()


Seleccion()

