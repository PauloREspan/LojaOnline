import streamlit as st
import streamlit.components.v1 as components
import csv
import os

# Configurar o Arquivo CSV
def inic_csv():
    if not os.path.exists("users.csv"):
        with open("users.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["user", "senha"])

def registar_user(user, senha):
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user, senha])
    return True

# Verificar o login
def verificar_login(user, senha):
    with open("users.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row == [user, senha]:
                return True
    return False


# Exemplo de mapa Google com o link que você forneceu
def mapa_google():
    google_maps_url = "https://g.co/kgs/RQBM66S"
    html_code = f"""
    <iframe src="{google_maps_url}" width="600" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>
    """
    components.html(html_code, height=450)


# Interface do Streamlit
st.sidebar.title("Login")

modo = st.sidebar.radio("Selecionar Opção", ["Login", "Registar"])

utilizador = st.sidebar.text_input("Utilizador")
senha = st.sidebar.text_input("Senha", type="password")

if modo == "Registar":
    if st.sidebar.button("Registar"):
        if registar_user(utilizador, senha):
            st.sidebar.success("Utilizador Registado com Sucesso")
            st.title("Bem-Vindo, " + utilizador)
else:
    if st.sidebar.button("Login"):
        if verificar_login(utilizador, senha):
            st.session_state.autenticado = True
        else:
            st.sidebar.error("Credenciais incorretas")

# Verificar a Autenticação e Display do conteúdo
if st.session_state.get("autenticado", False):
    tabs = st.tabs(["Rota verde", "Loja Online"])

    with tabs[0]:
        st.title("Rota Verde")
        # Display do mapa
        mapa_google()


    with tabs[1]:
        st.title("Loja Online")
        produtos = [
            {"nome": "Cabaz orgânico", "preco": 12, "img": "Horta.jpg"},
            {"nome": "Repolho", "preco": 1, "img": "Repolho.jpg"},
            {"nome": "Fallafel", "preco": 3, "img": "Falafel.jpg"}
        ]

        if "carrinho" not in st.session_state:
            st.session_state.carrinho = []

        cols = st.columns(3)
        for id, produto in enumerate(produtos):
            with cols[id % 3]:
                st.image(produto["img"], width=200)
                if st.button(f"Adicionar {produto['nome']}", key=produto["nome"]):
                    st.session_state.carrinho.append(produto)
                    st.success(f"Produto Adicionado com Sucesso")

        if st.session_state.carrinho:
            st.header("O seu Carrinho")
            total = sum(item["preco"] for item in st.session_state.carrinho)

            for item in st.session_state.carrinho:
                st.write(f"{item['nome']} - {item['preco']}€")
            st.write(f"Total - {total}€")
