import streamlit as st
from chatbot import predict_class, get_response, intents

st.title(" Davis Virtual")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True

for message in st.session_state.messages:
    with st.chat_message(message["role"]): #rol puede ser asistente o usuario
        st.markdown(message["content"]) #mostrar mensaje

if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hola, soy Davis virtual, he sido creado en Python. ¿En qué puedo ayudarte?")

    st.session_state.messages.append({"role": "assistant", "content": "Hola, soy Davis virtual, he sido creado en Python. ¿En qué puedo ayudarte?"})
    st.session_state.first_message = False

if prompt := st.chat_input("¿Cómo puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

# Implementación del algoritmo de AI
    insts = predict_class(prompt)
    res = get_response

    with st.chat_message("assistant"):
        st.markdown(res)

    st.session_state.messages.append({"role": "assistant", "content": res})

