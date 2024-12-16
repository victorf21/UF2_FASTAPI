from conn import get_connection
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

def create_informacio(info):
    conn = get_connection()
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        sql = """
        INSERT INTO informacio (total_intents, textos_joc, partidas_jugadas, partidas_ganadas, puntos_totales, nombre_usuario, mejor_partida)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING *;
        """
        cursor.execute(sql, (
            info.total_intents,
            info.textos_joc,
            info.partidas_jugadas,
            info.partidas_ganadas,
            info.puntos_totales,
            info.nombre_usuario,
            info.mejor_partida
        ))
        conn.commit()
        infonueva = cursor.fetchone()
        return infonueva 
    except (Exception, psycopg2.Error) as error:
        print("Error al crear la información:", error)
        return None  
    finally:
        cursor.close()
        conn.close()