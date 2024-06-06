from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Dados de exemplo: doenças e seus sintomas
data = {
    'doenças': ['resfriado', 'gripe', 'alergia'],
    'sintomas': [
        'nariz escorrendo, espirros, dor de garganta',
        'febre, dor no corpo, tosse',
        'coceira nos olhos, espirros, erupções cutâneas'
    ]
}

# Transformando os dados em vetores TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data['sintomas'])

# Função para encontrar a doença correspondente aos sintomas fornecidos
def encontrar_doenca(sintomas):
    sintomas_vetorizados = tfidf_vectorizer.transform([sintomas])
    similarity = cosine_similarity(sintomas_vetorizados, tfidf_matrix)
    max_similarity_index = np.argmax(similarity)
    return data['doenças'][max_similarity_index]

# Exemplo de uso: fornecer sintomas e obter a doença correspondente
sintomas_usuario = "espirros, dor de garganta"
doenca_identificada = encontrar_doenca(sintomas_usuario)
print("Com base nos sintomas fornecidos, a doença identificada é:", doenca_identificada)