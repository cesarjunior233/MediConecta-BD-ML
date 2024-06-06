from backend.ml_model import predict_disease
from backend.db import log_chat

def chatbot_response(user_input):
    """Retornar a resposta do chatbot com base nos sintomas fornecidos pelo usuário."""
    # Obter a predição do modelo
    predicted_disease = predict_disease(user_input)
    
    # Responder com a doença predita
    response = f"Com base nos sintomas fornecidos, você pode ter a seguinte doença: {predicted_disease}"
    
    # Registrar a interação no banco de dados
    log_chat(user_input, response)
    
    return response