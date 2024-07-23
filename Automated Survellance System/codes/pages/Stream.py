import streamlit as st
from os import path
from streamlit import rerun
import requests
import numpy as np
from time import sleep
from io import BytesIO
import concurrent.futures
from deepface import DeepFace
from streamlit.runtime.scriptrunner import add_script_run_ctx
from PIL import Image,ImageEnhance



if __name__ == '__main__':
    print("started stream")
    if 'curl' not in st.session_state:
        st.session_state.curl=url
    if 'stream' not in st.session_state:
        st.session_state.stream=False
    if 'ring' not in st.session_state:
        st.session_state.ring=False
    st.title("Live Stream")
    url=st.session_state.curl
    st.text("The Location of cam:")
    st.text(url)
    start=st.button("Start Stream")
    stop=st.button("Stop")
    bell=st.button("Doorbell")
    detect=st.empty()
    db=st.session_state.faces
    detect.write("Nobody Detected.")
    if start or st.session_state.stream:
        st.session_state.stream=True
        container=st.empty()
        while True:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            if bell:
                dfs=[[]]
                try:
                    dfs=DeepFace.find(img_path=np.asarray(img),model_name='ArcFace', enforce_detection=True,db_path=db)
                except:
                    detect.write('Nobody Detected.')
                if(len(dfs[0])>0):
                    st=dfs[0]['identity'][0]
                    n=len(st)
                    s=''
                    for i in range(n-6,-1,-1):
                        if(st[i]!='\\'):
                            s=st[i]+s
                        else:
                            break
                    detect.write(s)
                else:
                    detect.write('Unknown Person')
                sleep(2.5)
                rerun()
            container.image(img)
            if stop:
                container.empty()
                st.session_state.stream=False
                break