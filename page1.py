import streamlit as st
import joblib

def load_model(model_path):
    loaded_model_data = joblib.load(model_path)
    loaded_model = loaded_model_data['model']
    loaded_vectorizer = loaded_model_data['vectorizer']
    loaded_label_encoder = loaded_model_data['label_encoder']
    return loaded_model, loaded_vectorizer, loaded_label_encoder

def predict_sentiment(model, vectorizer, label_encoder, text_data):
    new_data_features = vectorizer.transform(text_data)
    predictions = model.predict(new_data_features)
    predicted_sentiments = label_encoder.inverse_transform(predictions)
    return predicted_sentiments

def page1_content():
    st.title('Teks Klasifikasi')
    st.write('Masukkan teks untuk melakukan klasifikasi sentimen:')
    text_input = st.text_area('Input Teks:')
    model_path = 'resource/model_sentimen_lr.pkl'
    loaded_model, loaded_vectorizer, loaded_label_encoder = load_model(model_path)
    
    if st.button('Prediksi Sentimen'):
        if text_input:
            new_data = [text_input]
            predicted_sentiments = predict_sentiment(loaded_model, loaded_vectorizer, loaded_label_encoder, new_data)
            st.write(f'Prediksi Sentimen: {predicted_sentiments[0]}')

