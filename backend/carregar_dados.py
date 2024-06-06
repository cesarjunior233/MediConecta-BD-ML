import pandas as pd

def load_data(file_path):
    """Carregar dados de um arquivo CSV e retornar um DataFrame do Pandas."""
    return pd.read_csv(file_path)