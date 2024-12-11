from conn import get_connection
import psycopg2

def get_info():
    try:
        # Conexión a la base de datos
        conn, connection = get_connection()
        sql = "SELECT texts_joc FROM informacio" 
        connection.execute(sql) # Ejecuta la query
        infos = connection.fetchall()
        return [{"texts_joc": row[0]} for row in infos]
    except (Exception, psycopg2.Error) as error:
        # Manejo de errores en la lectura 
        print("Error al obtener la información:", error)
    finally:
         # Cierra la conexión a la base de datos
            connection.close()
            conn.close()

def get_alfabet(idioma: str):
    try:
        # Conexión a la base de datos
        conn, connection = get_connection()
        sql = "SELECT lletres FROM alfabet WHERE idioma = %s" 
        connection.execute(sql,(idioma,)) # Ejecuta la query
        alfabet = connection.fetchone()
        return alfabet[0]
    except (Exception, psycopg2.Error) as error:
        # Manejo de errores en la lectura 
        print("Error al obtener el alfabeto:", error)
    finally:
         # Cierra la conexión a la base de datos
            connection.close()
            conn.close()