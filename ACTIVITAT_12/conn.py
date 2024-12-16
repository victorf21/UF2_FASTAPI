import psycopg2

def get_connection():
    try:
        dbname = "postgres1"
        user = "postgres"
        password = "root"
        host = "localhost"
        port = "5432"
        
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=dbname
        )
        print("Conexió exitosa a la base de dades")
        return conn

    except Exception as e:
        print(f"Error de connexió a la base de dades: {e}")
        return None  # Retornar None si hi ha un error