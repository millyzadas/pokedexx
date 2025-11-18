import streamlit as st
import functions

def app():
    st.header('Cadastrar')
    with st.form('button'):
        nome = st.text_input("Digite seu nome")
        cidade = st.text_input("Digite sua cidade")
        imagem = st.file_uploader("Foto de perfil")
        id = st.text_input("Crie seu código de treinador")
        confirm_id = st.text_input("Confirme seu código de treinador")
        button = st.form_submit_button('Cadastrar')
    
    st.write('Já tem uma conta?')
    if st.button('Entrar'):
        st.session_state.pagina = "perfil"
        
    if button:
        if confirm_código != código:
            st.warning('Os IDs não se coincidem')
        else:
            treinadorExiste = functions.verificar_treinador(código)
            if treinadorExiste == False:
                functions.inserir_treinador(nome, cidade, imagem, código)
                st.success('Treinador adicionado')
                st.balloons()
            else:
                st.warning(f"O treinador com o código: {código} já existe!")
