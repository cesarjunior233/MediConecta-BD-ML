import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from .db import load_symptoms  # Import relativo

def train_model():
    # Carregar o dataset
    df = load_symptoms()
    
    # Preparar os dados
    df['symptoms'] = df['symptom_name'].apply(lambda x: x.split(', '))
    df['symptoms'] = df['symptoms'].apply(lambda x: ' '.join(x))
    X = df['symptoms']
    y = df['disease']
    
    # Dividir os dados em conjunto de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Criar um pipeline de processamento de texto e modelo de classificação
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])
    
    # Treinar o modelo
    pipeline.fit(X_train, y_train)
    
    # Avaliar o modelo
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')
    
    # Salvar o modelo treinado
    joblib.dump(pipeline, 'backend/chatbot_model.pkl')

def predict_disease(symptoms):
    # Carregar o modelo treinado
    model = joblib.load('backend/chatbot_model.pkl')
    
    # Fazer a predição
    prediction = model.predict([symptoms])
    return prediction[0]

if __name__ == "__main__":
    train_model()