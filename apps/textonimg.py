import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
# organizing imports
import cv2
import numpy as np

DEMO_IMAGE = 'imgs/Tiger.jpg'

def app():
    @st.cache
    def imgtext(photo, text):
        #Read Image
        img = photo
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        image = cv2.putText(img, text, org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)


        return image
    st.title('Adicionar Título com OpenCV')
    img_file_buffer = st.file_uploader("Faça o Upload de uma Imagem", type=[ "jpg", "jpeg",'png'])
    
    if img_file_buffer is not None:
        image = np.array(Image.open(img_file_buffer))
    else:
        demo_image = DEMO_IMAGE
        image = np.array(Image.open(demo_image))
        
    st.image(image, caption=f"Imagem Original",use_column_width= True)

    useWH = st.checkbox('Adicione um Título')

    if useWH:
        st.subheader('Coloque seu texto aqui:')

        text = st.text_area("")
        
        resized_image = imgtext(image , text)

        st.image(resized_image)
