import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageOps
import cv2 as cv
from multiapp import MultiApp
from apps import home,sketch,textonimg,Face_detect,Crop,filters
app = MultiApp()

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

app.add_app("Home", home.app)
app.add_app("Filtros", filters.app)
app.add_app("Esboço de Imagem", sketch.app)
app.add_app("Adicionar Titulo", textonimg.app)
app.add_app("Cortar Imagem", Crop.app)
app.add_app("Detecção de Rosto", Face_detect.app)

app.run()
