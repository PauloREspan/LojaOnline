import streamlit as st 
import csv
import os
import streamlit.components.v1 as components

# Configurar o Arquivo CSV

def inic_csv():
  if not os.path.exist("users.csv"):
    with open("user.csv", "w", newline="") as file:
      writer = csv.write(file)
      writer.writerow(["user","senha"])

def registar_user(user,senha):
  with open("user.csv", "a", newline="") as file:
      writer = csv.write(file)
      writer.writerow([user,senha])
  return True

#Verifar o login

def verificar_login(user,senha):
  with open("user.csv", "r", newline="") as file:
      reader = csv.reader(file)
      for row in reader:
        if row ==[user,senha]:
        return True
  return False

  # Iterface do Streamlite

  st.sidebar.title("Login")

  modo = st.sidebar.radio("Selecionar Opção". ["Login", "Registar"])

  utilizador = st.sidebar.text_input("Utilizador")
  senha = st.sidebar.text_input("Senha", type= password)

  if modo == "Registar":
    if st.sidebar.button("Registar"):
      registar_utilizado(user,senha)
      st.sidebar.sucess("Utilizador Registado com Sucesso")
      st.title("Bem-Vindo,", utilizador)

    else:
      if st.sidebar.button("Login"):
        if verificar_login(user,senha):
          st.session_state.autenticado = True
        else:
          st.sidebar.erro("Credenciais incorretas")

# Verificar a Autenticação e Display do conteúdo

if st.session_state.get("autenticado", False):
  tabs = st.tab(["Rota verde", "Loja Online"])

  tab[0]:

    st.title("Rota Verde")
    mapa = st.image("mapa.jpeg")

  tab[1]:

    st.title("Loja Online")
    produtos = [
     {"nome": "Cabaz orgânico", "preço": "12€", "img": "Horta.jpg"}
     {"nome": "Repolho", "preço": "1€", "img": "Repolho.jpg"}
     {"nome": "Fallafel", "preço": "3€", "img": "Falafel.jpg"}
    ]

    if "carrinho" not in st.session_state:
      st.session_state.carrinho = []

      cols = st.columns(3):
      for id, produto in enumerate(produtos):
        with cols[id % 3]:
          st.image(produto["img"],width= 200)
          st.write(f"Adicionar {produto["nome"]}", key=produto ["nome"]):
            st.session_state.carrinho.append(produto)
            st.sucess(f"Produto Adicionado com Sucesso")
    if st.session_state.carrinho:
      st.header("O seu Carrinho")
      total = sum(item["preco"] for item in st.session_state.carrinho)

      for item in st.session_state.carrinho:
        st.write(f"{item["nome"]} - {item["preco"]}€")
        st.write(f"Total - {total}€")

      

