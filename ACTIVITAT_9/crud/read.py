from db_connect.conn import get_connection
import psycopg2

def read_users():
    try:
        # Conexión a la base de datos
        conn, connection = get_connection()
        sql = "SELECT * FROM users" # Query para leer todos los users
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