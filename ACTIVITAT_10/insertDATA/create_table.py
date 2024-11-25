from ACTIVITAT_9.db_connect.conn import get_connection
import psycopg2

def create_table_users():
    try:
        conn, connection = get_connection() # Conexión a la base de datos
        # Query para crear tabla
        sql = ''' 
            CREATE TABLE IF NOT EXISTS PENJAT(
                word TEXT NOT NULL,
                theme TEXT NOT NULL
            )
        '''
        connection.execute(sql) # Ejecuta la query
        conn.commit() # Guarda los cambios realizados en la base de datos
        print("Tabla creada correctamente.")
    except (Exception, psycopg2.Error) as error:
        # Manejo de errores
        print("Error al crear la tabla: ", error)
    finally:
        # Cierra la conexión a la base de datos
        connection.close()
        conn.close()
        
create_table_users()