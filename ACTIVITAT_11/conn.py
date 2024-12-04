import psycopg2

def get_connection():
    try:
        #Configuración de conexión
        conn = psycopg2.connect(
            dbname='postgres',        
            user='user_postgres',     
            password='pass_postgres', 
            host='localhost',         
            port='5432'               
        )
        #Crear un cursor para ejecutar consultas SQL
        connection = conn.cursor() 
        return conn, connection
    except (Exception, psycopg2.Error) as error:
        #Manejo de errores
        print("Error al conectar a la base de datos:", error)
        return None, None
