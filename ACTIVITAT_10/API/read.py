from conn import get_connection
import psycopg2

def select_theme():
    try:
        # Conexión a la base de datos
        conn, connection = get_connection()
        sql = "SELECT DISTINCT theme FROM words;" 
        connection.execute(sql) # Ejecuta la query
        users = connection.fetchall() # Recupera todos los registros
        # Muestra los users
        for user in users:
            print(user)
    except (Exception, psycopg2.Error) as error:
        # Manejo de errores en la lectura de usuarios
        print("Error al leer los usuarios:", error)
    finally:
         # Cierra la conexión a la base de datos
        connection.close()
        conn.close()
    return users