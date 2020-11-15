	
import psycopg2
# Se realizara la debida conexion con la base de datos postgres 
# que se encuentra alojada en AWS

dc = {
    'host' : 'database-1.cpdwyuazzw9j.us-east-1.rds.amazonaws.com',
    'database' : 'Proyecto_scrum_2020',
    'user' : 'postgres',
    'password' : 'proyecto_programacion'
}

# Conexión a la base de datos
conexion = psycopg2.connect(**dc)


print('conectado')