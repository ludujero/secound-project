import streamlit as  st

st.title("Cadastro de Clientes")

nome = st.text_input("Nome:")
endereco = st.text_input("Endereço: ")
dt_nasc = st.date_input("Idade:")
tipo_cliente = st.selectbox("TIpo de Cliente: ", 
                            ["Pessoa Física", "Pessoa Jurídica"])
cadastrar = st.button("Salvar")

if cadastrar:
    with open("clientes.cvs", "a", encoding= "utf8") as arquivo:
        arquivo.write(f"{nome}, {endereco}, {dt_nasc}, {tipo_cliente}\n")
        st.success("Cliente Cadstrado Com Sucesso!")