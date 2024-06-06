import psycopg2
import configparser
import pandas as pd

def connect_to_db():
    """Conectar ao banco de dados PostgreSQL."""
    try:
        config = configparser.ConfigParser()
        config.read('backend/config.ini')

        conn = psycopg2.connect(
            host=config['POSTGRESQL']['DB_HOST'],
            port=config['POSTGRESQL']['DB_PORT'],
            dbname=config['POSTGRESQL']['DB_NAME'],
            user=config['POSTGRESQL']['DB_USER'],
            password=config['POSTGRESQL']['DB_PASSWORD']
        )
        return conn
    except UnicodeDecodeError as e:
        print(f"Erro de decodificação: {e}")
        raise
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

def load_symptoms():
    """Carregar dados de sintomas do banco de dados PostgreSQL."""
    conn = connect_to_db()
    query = "SELECT symptom_name, disease FROM symptoms;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def log_chat(user_input, bot_response):
    """Registrar a interação do usuário e a resposta do chatbot no banco de dados PostgreSQL."""
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO chat_logs (user_input, bot_response) VALUES (%s, %s);"
    cursor.execute(query, (user_input, bot_response))
    conn.commit()
    cursor.close()
    conn.close()