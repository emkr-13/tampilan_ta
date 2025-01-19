import streamlit as st
import joblib
from loguru import logger



def page2_content():
    st.title('Topik Modeling LDA dan LSA')
    st.markdown("""
    \n Untuk melihat hasil coherence score batasaan jumlah topik yang digunakaan bisa di lihat pada link berikut : [Link](https://github.com/emkr-13/model_ta/blob/main/LDA%20dan%20LSA/cara_nilai.ipynb)
    \n Pada Menu Terdiri dari 2 topik utama yaitu LDA dan LSA dan di tampilkan kedalaam worlcoud dan bar chart 
                """)
    
    
    # Memuat kembali model dan vectorizer
    lda_model = joblib.load('resource/lda_tfidf_model_baru.pkl')
    lsa_model = joblib.load('resource/lsa_tfidf_model_baru.pkl')
    
    # Jumlah topik yang diinginkan
    num_lda_topics = 1
    num_lsa_topics = 1
    top_n_words = 5  # Jumlah kata kunci untuk setiap topik

  