import streamlit as st
import functions

def app():
    st.header('Deletar')
    with st.form('button'):
        id = st.text_input("Digite o código do usuário a ser deletado")
        button = st.form_submit_button('Deletar')
        
    if button:
        functions.deletar_treinador(código)
        st.success('Treinador deletado')
