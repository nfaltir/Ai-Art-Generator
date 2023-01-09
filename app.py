import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import json
import openai


#streamlit config
st.set_page_config(page_title="OpenAi Art", page_icon="🎨")
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """<style>footer {visibility: hidden;}</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #EB455F; font-size: 4.5rem;'> OpenAI Art 🎨</h1>", unsafe_allow_html=True)
st.write("<hr><br>", unsafe_allow_html=True)


#OpenAI api keys

openai.api_key = st.secrets["api_key"]

image_desc = st.text_area("Describe image for ai: ")

#center 'generate' button using streamlit hack
col1, col2, col3 , col4, col5 = st.columns(5)
with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button("Generate")

#using html <br> tags for margin, style preference
st.write("<br>", unsafe_allow_html=True)

if len(image_desc) > 0:
    ai_image = openai.Image.create(
        prompt= image_desc,
        n = 1,
        size="1024x1024"
    )
    #process json data from openai
    data_obj = json.dumps(ai_image.data)
    json_obj = json.loads(data_obj)

    #retrieve url link
    for get_image_url in json_obj:
        image_url = get_image_url['url']

    #process image
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    #show image
    st.image(img, caption='generated by: OpenAi (1024x1024)')



