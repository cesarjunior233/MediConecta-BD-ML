import streamlit as st
from backend.chatbot import chatbot_response

def main():
    st.set_page_config(page_title="Health Chatbot", page_icon=":hospital:", layout="centered")

    st.title('Health Chatbot')
    st.markdown("""
    <style>
    .reportview-container {
        background: url("https://www.example.com/background-image.jpg")
    }
    .sidebar .sidebar-content {
        background: url("https://www.example.com/sidebar-background-image.jpg")
    }
    </style>
    """, unsafe_allow_html=True)

    st.header("Converse com nosso chatbot sobre seus sintomas de saúde")
    st.write("""
    Digite os sintomas que você está sentindo e o chatbot irá sugerir possíveis doenças com base nos sintomas fornecidos.
    """)
    
    user_input = st.text_input('Digite seus sintomas aqui:')
    if st.button('Enviar'):
        if user_input:
            bot_response = chatbot_response(user_input)
            st.text_area('Resposta do Chatbot:', value=bot_response, height=200)
        else:
            st.warning("Por favor, digite seus sintomas antes de enviar.")

    st.markdown("---")
    st.markdown("© 2024 Health Chatbot. Todos os direitos reservados.")

if __name__ == '__main__':
    main()