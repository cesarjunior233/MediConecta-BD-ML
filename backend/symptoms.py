import pandas as pd
import psycopg2
import configparser

def connect_to_db():
    """Conectar ao banco de dados PostgreSQL."""
    # Leitura das configurações do arquivo config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Obtenção das informações de conexão do PostgreSQL do arquivo config.ini
    DB_HOST = config['POSTGRESQL']['DB_HOST']
    DB_PORT = config['POSTGRESQL']['DB_PORT']
    DB_NAME = config['POSTGRESQL']['DB_NAME']
    DB_USER = config['POSTGRESQL']['DB_USER']
    DB_PASSWORD = config['POSTGRESQL']['DB_PASSWORD']

    # Estabelecer conexão com o banco de dados PostgreSQL
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

def load_symptoms(conn):
    """Carregar dados de sintomas do banco de dados PostgreSQL e retornar um DataFrame do Pandas."""
    query = "SELECT * FROM symptoms;"
    return pd.read_sql(query, conn)

def suggest_diseases(symptoms_df, user_symptoms):
    """Sugerir possíveis doenças com base nos sintomas fornecidos pelo usuário."""
    # Lógica do chatbot para sugerir doenças com base nos sintomas
    # Aqui você pode implementar qualquer algoritmo ou modelo para sugerir doenças
    return ["Resfriado", "Gripe"]  # Exemplo de retorno