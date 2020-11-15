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