from conn import get_connection
import psycopg2

# Obtiene todos los texts_joc de la tabla informacio.
def get_info(): 
    # Conexión a la base de datos
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT textos_joc FROM informacio"
        cursor.execute(sql)  # Ejecuta la consulta
        infos = cursor.fetchall()

        return [{"textos_joc": row[0]} for row in infos]
    except (Exception, psycopg2.Error) as error:
        print("Error al obtener la información:", error)
    finally:
        # Cerrar cursor y conexión
        cursor.close()
        conn.close()

# Obtiene el alfabeto asociado al idioma proporcionado.
def get_alfabet(idioma: str): 
    # Conexión a la base de datos
    conn = get_connection()
    try:
        # Conexión a la base de datos
        cursor = conn.cursor()
        sql = "SELECT lletres FROM alfabet WHERE idioma = %s"
        cursor.execute(sql, (idioma,)) 
        alfabet = cursor.fetchone()
        # Devuelve el resultado si existe
        return alfabet[0] if alfabet else None
    except (Exception, psycopg2.Error) as error:
        print("Error al obtener el alfabeto:", error)
        return None
    finally:
        # Cerrar cursor y conexión
        cursor.close()
        conn.close()

def update_informacio(nombre_usuario, partidas_jugadas, partidas_ganadas, puntos_totales, mejor_partida):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        # Verificar si el usuario existe en la tabla 'informacio'
        cursor.execute("SELECT COUNT(*) FROM informacio WHERE nombre_usuario = %s", (nombre_usuario,))
        existe_usuario = cursor.fetchone()[0]

        if not existe_usuario:
            return {"error": f"El usuario '{nombre_usuario}' no existe en la tabla 'informacio'"}

        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE informacio
            SET partidas_jugadas = partidas_jugadas + %s,
                partidas_ganadas = partidas_ganadas + %s,
                puntos_totales = puntos_totales + %s,
                mejor_partida = GREATEST(mejor_partida, %s)
            WHERE nombre_usuario = %s
            """, 
        (partidas_jugadas, partidas_ganadas, puntos_totales, mejor_partida, nombre_usuario))
        conn.commit()
        return {"message": f"Datos actualizados correctamente para el usuario '{nombre_usuario}'"}
    
    except (Exception, psycopg2.Error) as error:
        print("Error en actualizar la información:", error)
        return None
    finally:
        # Cerrar cursor y conexión
        cursor.close()
        conn.close()

def update_total_intents(id_informacio, total_intents):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM informacio WHERE id_informacio = %s", (id_informacio,))
        existe_usuario = cursor.fetchone()[0]

        if not existe_usuario:
            return {"error": f"La id: {id_informacio} no existe en la tabla 'informacio'"}

        cursor.execute(
            """
            UPDATE informacio
            SET total_intents = %s
            WHERE id_informacio = %s
            """, 
        (total_intents, id_informacio))
        conn.commit()
        
        return {"message": "El valor de total_intents ha sido actualizado."}

    except (Exception, psycopg2.Error) as error:
        print("Error en actualizar la información:", error)
        return None
    finally:
        # Cerrar cursor y conexión
        cursor.close()
        conn.close()