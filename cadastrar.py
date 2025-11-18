import streamlit as st
import functions

def app():
    st.header('Cadastrar')
    with st.form('button'):
        nome = st.text_input("Digite seu nome")
        cidade = st.text_input("Digite sua cidade")
        imagem = st.file_uploader("Foto de perfil")
        id = st.text_input("Crie seu ID de treinador")
        confirm_id = st.text_input("Confirme seu ID de treinador")
        button = st.form_submit_button('Cadastrar')
    
    st.write('Já tem uma conta?')
    if st.button('Entrar'):
        st.session_state.pagina = "perfil"
        
    if button:
        if confirm_id != id:
            st.warning('Os IDs não se coincidem')
        else:
            treinadorExiste = functions.verificar_treinador(id)
            if treinadorExiste == False:
                functions.inserir_treinador(nome, cidade, imagem, id)
                st.success('Treinador adicionado')
                st.balloons()
            else:
                st.warning(f"O treinador com o id: {id} já existe!")
