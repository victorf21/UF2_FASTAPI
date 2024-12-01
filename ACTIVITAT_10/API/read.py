from conn import get_connection
import psycopg2

def select_theme():
    try:
        # Conexión a la base de datos
        conn, connection = get_connection()
        sql = "SELECT DISTINCT theme FROM paraules" 
        connection.execute(sql) # Ejecuta la query
        tematiques = connection.fetchall()
        return tematiques
    except (Exception, psycopg2.Error) as error:
        # Manejo de errores en la lectura 
        print("Error al leer las tematicas:", error)
        return []
    finally:
         # Cierra la conexión a la base de datos
            connection.close()
            conn.close()


def get_word(theme: str):
    try:
        # Conexión a la base de dades
        conn, connection = get_connection()
        sql = "SELECT word FROM paraules WHERE theme = %s ORDER BY RANDOM() LIMIT 1"
        connection.execute(sql, (theme,))  # Pasa la tematica como parametro 
        word = connection.fetchone()  # Recuperem una sola paraula
        return word
    except (Exception, psycopg2.Error) as error:
        print(f"Error en obtenir una paraula:", error)
        return None
    finally:
        # Cierra la conexión a la base de datos
            connection.close()
            conn.close()