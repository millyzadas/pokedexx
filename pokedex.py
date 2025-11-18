
import streamlit as st
import functions

def app():
    st.title("Captura Pokémons")
    with st.form('button'):
        pokemon = st.text_input("Nome do Pokémon capturado...").lower()
        id = st.text_input("Digite o código do treinador que o capturou")
        imagem = st.file_uploader("Envie uma imagem do Pokémon", type=["png", "jpg", "jpeg"])
        button = st.form_submit_button('Capturar!')

    if button:
        existe = functions.verificar_treinador(id)
        if existe == False:
            st.warning("O treinador não existe!")
        else:
            functions.adicionar_pokemon(pokemon, id, imagem)
            st.success("Pokémon capturado")
            st.balloons()
            
    
    st.header('Pokémons encontrados:')
    functions.mostrar_pokemons()

  


