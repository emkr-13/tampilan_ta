import streamlit as st
import joblib
import time
from scipy.sparse import hstack

def load_model(model_path):
    loaded_model_data = joblib.load(model_path)
    loaded_model = loaded_model_data['model']
    tfidf_vectorizer = loaded_model_data['tfidf_vectorizer']
    count_vectorizer = loaded_model_data['count_vectorizer']
    loaded_label_encoder = loaded_model_data['label_encoder']
    return loaded_model, tfidf_vectorizer,count_vectorizer, loaded_label_encoder


def predict_sentiment(model, tfidf_vectorizer, count_vectorizer, label_encoder, text_data):
    # Transform the new data using the loaded vectorizers
    tfidf_features = tfidf_vectorizer.transform(text_data)
    count_features = count_vectorizer.transform(text_data)
    
    # Combine the features
    combined_features = hstack([tfidf_features, count_features])
    
    # Make predictions
    predictions = model.predict_proba(combined_features)[0]
    predicted_sentiments = {label: f"{p * 100:.2f}%" for label, p in zip(label_encoder.classes_, predictions)}
    return predicted_sentiments

def page1_content():
    st.title('Teks Klasifikasi')
    st.markdown("""
    List Berita yang di buat model teks yang dapat digunakan:
    1. Berita Detik link berikut : https://www.detik.com.
    2. Berita Kompas link berikut : https://www.kompas.com.
    3. Berita CNN link berikut : https://www.cnnindonesia.com.\n
    Bisa mengunakaan berita lain juga selain di atas 
    Untuk mencari teks lain bisa mencari lewat portal berita yang untuk melihat hasil prediksi sentimen.  
    Melihat proses pelatihan model bisa melihat link berikut: [link](https://github.com/emkr-13/model_ta/tree/main/Sentimen)
    """)
    st.write('Masukkan teks untuk melakukan klasifikasi sentimen:')
    text_input = st.text_area('Input Teks:')
    model_path = 'resource/model_sentimen_svm.pkl'
    loaded_model, tfidf_vectorizer,count_vectorizer, loaded_label_encoder = load_model(model_path)
    
    uji_test = st.button('Prediksi Sentimen')
    if uji_test:
        if text_input.strip():
            new_data = [text_input]
            predicted_sentiments = predict_sentiment(loaded_model,  tfidf_vectorizer,count_vectorizer, loaded_label_encoder, new_data)
            with st.spinner('Wait for it...'):
                time.sleep(2)
                st.balloons()
            st.success(f'Prediksi Sentimen: {predicted_sentiments}', icon="✅")
        else:
            st.error('Masukkan teks terlebih dahulu untuk melakukan prediksi.')