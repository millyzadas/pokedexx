
import streamlit as st
import functions

def app():
    if 'logado' not in st.session_state:
        st.session_state.logado = False
    if 'códogo_treinador' not in st.session_state:
        st.session_state.id_treinador = None
    if 'nome_treinador' not in st.session_state:
        st.session_state.nome_treinador = None
    if 'cidade_treinador' not in st.session_state:
        st.session_state.cidade_treinador = None
    
    if not st.session_state.logado:
        st.header('Entrar')
        with st.form('login_form'):
            nome = st.text_input("Digite seu nome")
            cidade = st.text_input("Digite sua cidade")
            código = st.text_input("Digite seu ID de treinador")
            button = st.form_submit_button('Entrar')

        st.write("Não tem conta?")
        if st.button("Cadastre-se"):
            st.session_state.pagina = "cadastrar"
        
        if button:
            treinadorExiste = functions.verificar_treinador(id)
            if treinadorExiste:
                st.session_state.logado = True
                st.session_state.id_treinador = id
                st.session_state.nome_treinador = nome
                st.session_state.cidade_treinador = cidade
                st.rerun()
            else:
                st.error('código inválido')
    
    else:
        st.header('Perfil:')
        functions.mostrar_treinador(st.session_state.id_treinador)
        st.subheader('Pokémons:')
        functions.mostrar_pokemon(st.session_state.id_treinador)
        
        if st.button("Sair"):
            st.session_state.logado = False
            st.session_state.id_treinador = None
            st.session_state.nome_treinador = None
            st.session_state.cidade_treinador = None
            st.rerun()
