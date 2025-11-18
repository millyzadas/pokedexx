import streamlit as st

def app():
    st.header('Entrar')
    with st.form('button'):
        nome = st.text_input("Digite seu nome")
        cidade = st.text_input("Digite sua cidade")
        id = st.text_input("Digite seu código de treinador")
        button = st.form_submit_button('Entrar')

    st.write("Não tem conta?")
    if st.button("Cadastre-se"):
        st.session_state.pagina = "cadastrar"
