import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.sparse import csr_matrix
from datasets import load_dataset
import joblib

def visualize_topics(model, num_topics, top_n_words, title):
    # Judul aplikasi
    st.header(title)

    # Menampilkan kata-kata kunci untuk setiap topik
    st.subheader("Kata Kunci untuk Setiap Topik")
    for idx, topic in model.print_topics(num_topics):
        st.write(f"Topik {idx + 1}: {topic}")

    # Wordcloud untuk setiap topik
    st.subheader("Wordcloud untuk Setiap Topik")
    plt.figure(figsize=(12, 8))
    for i in range(num_topics):
        plt.subplot(2, 5, i+1)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(model.show_topic(i, topn=top_n_words)))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title(f'Topik {i+1}')
        plt.axis('off')
    plt.tight_layout()
    st.pyplot(plt)

    # Barplot untuk setiap topik
    st.subheader("Barplot untuk Setiap Topik")
    plt.figure(figsize=(12, 8))
    for i in range(num_topics):
        plt.subplot(2, 5, i+1)
        topic_words = [word for word, _ in model.show_topic(i, topn=top_n_words)]
        word_probs = [prob for _, prob in model.show_topic(i, topn=top_n_words)]
        sns.barplot(x=topic_words, y=word_probs)
        plt.title(f'Topik {i+1}')
        plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    
@st.cache_data 
def load_data():
    dataset = load_dataset("emkr-13/Dataset_Berita_Indo")
    return dataset['train'].to_pandas()

def page2_content():
    st.title('Topik Modeling LDA dan LSA')
    st.markdown("""
    \n Untuk melihat hasil coherence score batasaan jumlah topik yang digunakaan bisa di lihat pada link berikut :
    \n Pada Menu Terdiri dari 2 topik utama yaitu LDA dan LSA dan di tampilkan kedalaam worlcoud dan bar chart 
                """)
    
    
    # Memuat kembali model dan vectorizer
    lda_vectorizer, lda_model = joblib.load('resource/lda_tfidf_model.pkl')
    lsa_vectorizer, lsa_model = joblib.load('resource/lsa_tfidf_model.pkl')

    # Load the dataset
    data = load_data()
    
    
    
    st.header("Worlcoud Keseluruhan Data")
    all_texts = ' '.join(data['content_clean'])
    # Generate a word cloud image
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_texts)

    # Display the generated image:
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)  # Use st.pyplot to display the word cloud
    

    # Jumlah topik yang diinginkan
    num_lda_topics = 1
    num_lsa_topics = 2
    top_n_words = 5  # Jumlah kata kunci untuk setiap topik

    visualize_topics(lda_model, num_lda_topics, top_n_words, 'Visualisasi Topik dengan LDA')
    
    visualize_topics(lsa_model, num_lsa_topics, top_n_words, 'Visualisasi Topik dengan LSA')