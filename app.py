import streamlit as st

# Título
st.title("Widgets Interativos")

# Slider
numero = st.slider("Escolha um número", 0, 100)
st.write(f"Você escolheu: {numero}")

# Botão
if st.button("Clique aqui"):
    st.write("Você clicou no botão!")