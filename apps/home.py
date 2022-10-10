import streamlit as st
from PIL import Image
def app():
    image = Image.open('imgs/lake.jpeg')
    st.image(image, caption='Bem-Vindo ao aplicativo web!', use_column_width=True)
    st.subheader('Análise e processamento de imagem usando Python')
    st.subheader("", anchor=None)
    st.subheader("", anchor=None)
    st.subheader("", anchor=None)
    st.markdown('', unsafe_allow_html=True)
    st.subheader("", anchor=None)
    st.markdown("&copy; Desenvolvido por: Guilherme Dias Dos Santos")
