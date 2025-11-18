import streamlit as st

st.set_page_config(page_title='Pokedex', layout='wide')

st.session_state.setdefault("pagina", "perfil")

opcoes = ["perfil", "cadastrar", "deletar", "pokedex"]
pagina = st.sidebar.selectbox(
    "Escolha uma página:",
    opcoes,
    index=opcoes.index(st.session_state.pagina)
)

st.session_state.pagina = pagina

modulos = {
    "perfil": "page.perfil",
    "cadastrar": "page.cadastrar",
    "deletar": "page.deletar",
    "pokedex": "page.pokedex"
}

modulo = __import__(modulos[pagina], fromlist=["app"])
modulo.app()
