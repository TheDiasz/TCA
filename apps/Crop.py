import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image
def app():
    st.set_option('deprecation.showfileUploaderEncoding', False)

    # Upload an image and set some options for demo purposes
    st.header("Cortar Imagem")
    img_file = st.sidebar.file_uploader(label='Faça o Upload de um arquivo', type=['png', 'jpg','jpeg'])
    realtime_update = st.sidebar.checkbox(label="Atualização em tempo real", value=True)
    box_color = st.color_picker(label="Cor do quadrado", value='#0000FF')
    aspect_choice = st.sidebar.radio(label="Formato", options=["1:1", "16:9", "4:3", "2:3", "Free"])
    aspect_dict = {"1:1": (1,1),
                    "16:9": (16,9),
                    "4:3": (4,3),
                    "2:3": (2,3),
                    "Free": None}
    aspect_ratio = aspect_dict[aspect_choice]

    if img_file:
        img = Image.open(img_file)
        if not realtime_update:
            st.write("Clique duas vezes para atualizar")
        # Get a cropped image from the frontend
        cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                                    aspect_ratio=aspect_ratio)
        
        # Manipulate cropped image at will
        st.write("Preview")
        _ = cropped_img.thumbnail((150,150))
        st.image(cropped_img)