import streamlit as st
from os import path
import requests
from time import sleep
from io import BytesIO
import concurrent.futures
from streamlit.runtime.scriptrunner import add_script_run_ctx
from PIL import Image,ImageEnhance

base=path.dirname(__file__)
filepath=path.abspath(path.join(base,"faces"))
img=None
url1="http://"
url2=""
url3=""


if __name__ == '__main__':
    print("started index")
    st.title("Welcome to Realtime Automated Surveilance System!")
    url2=st.text_input("Enter the IP for cam")
    quality=st.selectbox("Choose your Quality", ('Low', 'Medium', 'High'))
    if quality=='Low':
        url3="/cam-lo.jpg"
    elif quality=='Medium':
        url3="/cam-mid.jpg"
    elif quality=='High':
        url3="/cam-hi.jpg"
    else:
        url3="/cam-hi.jpg"
    url=url1+url2+url3
    print(url)
    if 'curl' not in st.session_state:
        st.session_state.curl=url
    if 'stream' not in st.session_state:
        st.session_state.stream=False
    if 'ring' not in st.session_state:
        st.session_state.ring=False
    if 'faces' not in st.session_state:
        st.session_state.faces=filepath
        print(filepath)
    if st.button("Save IP"):
        st.session_state.curl=url