# organizing imports
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import cv2


DEMO_IMAGE = 'imgs/Tiger.jpg'
def app():
    @st.cache
    def img2sketch(photo, k_size):
        #Read Image
        img = photo
        # Convert to Grey Image
        grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Invert Image
        invert_img=cv2.bitwise_not(grey_img)
        #invert_img=255-grey_img

        # Blur image
        blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

        # Invert Blurred Image
        invblur_img=cv2.bitwise_not(blur_img)
        #invblur_img=255-blur_img

        # Sketch Image
        sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
        #imporve contrast using histogram equilization
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        sketch_img = clahe.apply(sketch_img)

        return sketch_img

    st.title('Esboço de Imagem com OpenCV')
    img_file_buffer = st.file_uploader("Faça o Upload de uma imagem", type=[ "jpg", "jpeg",'png'])
    if img_file_buffer is not None:
            image = np.array(Image.open(img_file_buffer))
    else:
        demo_image = DEMO_IMAGE
        image = np.array(Image.open(demo_image))

    st.image(image, caption=f"Imagem Original",use_column_width= True)


    if st.button("CONVERTER"):

        k_size = 5
        
        resized_image = img2sketch(image , k_size)

        st.image(
        resized_image, caption=f"Esboço da Imagem", use_column_width=True)


    

        
