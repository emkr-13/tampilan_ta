import streamlit as st
import pandas as pd

from loguru import logger

# Initialize logger
logger.add("app.log", rotation="500 MB")




def home_content():
    st.title('Selamat Datang di Sentimen Analisis dan Topik Analisis Berita')
    st.write('Selamat datang di website saya Di sini, saya menyajikan hasil skripsi saya tentang Sentimen Analisis dan Topik Analisis Berita.')
    st.markdown("""
    Nama\t : Emmanuel Mathew Krisna Rata\n
    NPM\t : 200710530\n
    """)

    try:


        st.header('Dataset Crawling Berita')
        st.markdown("""
            \n Di karena dataset load data yang besar maka tidak menampilkan dataset maka dari untuk melihat dataset pada huggeface di link berikut: [link](https://huggingface.co/datasets/emkr-13/berita_pemilu_2024)
        """)


        
    except Exception as e:
        logger.error(f"Error in home_content: {e}")
        st.error(f"An error occurred while processing your request: {e}")

