import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset
from loguru import logger

# Initialize logger
logger.add("app.log", rotation="500 MB")


# Function to create pie chart
def create_pie_chart(data, title):
    try:
        counts = data.value_counts()
        fig, ax = plt.subplots()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
        st.write("Persebaraan Data:")
        st.write(counts)
    except Exception as e:
        logger.error(f"Error creating pie chart: {e}")
        st.error("Failed to create pie chart")

# Function to plot bar chart
def plot_bar_chart(data, xlabel, ylabel, title):
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        data.plot(kind='bar', ax=ax)
        ax.set_ylabel(ylabel)
        ax.set_xlabel(xlabel)
        st.pyplot(fig)
        st.write("Persebaraan Data:")
        st.write(data)
    except Exception as e:
        logger.error(f"Error creating bar chart: {e}")
        st.error("Failed to create bar chart")

# Function to plot line chart
def plot_line_chart(data, xlabel, ylabel, title):
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        data.plot(kind='line', ax=ax)
        ax.set_ylabel(ylabel)
        ax.set_xlabel(xlabel)
        st.pyplot(fig)
        st.write("Persebaraan Data:")
        st.write(data)
    except Exception as e:
        logger.error(f"Error creating line chart: {e}")
        st.error("Failed to create line chart")
        
@st.cache_data
def load_data():
    try:
        # Load the dataset
        data = pd.read_csv('resource/dataset_pemilu_2024.csv')
        logger.success("data bisa di load")
        return data
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        st.error("Failed to load data {e}")

def home_content():
    st.title('Selamat Datang di Sentimen Analisis dan Topik Analisis Berita')
    st.write('Selamat datang di website saya Di sini, saya menyajikan hasil skripsi saya tentang Sentimen Analisis dan Topik Analisis Berita.')
    st.markdown("""
    Nama\t : Emmanuel Mathew Krisna Rata\n
    NPM\t : 200710530\n
    """)

    try:
        # Load the dataset
        data = load_data()

        st.header('Dataset Crawling Berita')
        st.markdown("""
            \n Di karena dataset load data yang besar maka tidak menampilkan dataset maka dari untuk melihat dataset pada huggeface di link berikut: [link](https://huggingface.co/datasets/emkr-13/berita_pemilu_2024)
        """)
        st.text(f"Jumlah Baris Data = {data.shape[0]}")

        # Pie chart for news source distribution
        st.subheader('Persebaraan Berita')
        create_pie_chart(data['asal_berita'], 'Persebaraan Berita')

        # Attempt to parse dates in multiple formats
        date_formats = ['%Y-%m-%d', '%d-%m-%Y']
        for fmt in date_formats:
            try:
                data['tanggal_berita'] = pd.to_datetime(data['tanggal_berita'], format=fmt, errors='coerce')
                if data['tanggal_berita'].notna().all():
                    break
            except Exception as e:
                logger.warning(f"Date format {fmt} failed with error: {e}")


        st.header('Sentiment Analysis')
        st.write("Sentiment analysis berdasarkan dataset yang digunakaan ")
        # Pie chart for sentiment distribution
        st.subheader('Persebaraan Sentimen')
        create_pie_chart(data['sentimen'], 'Persebaraan Sentimen')

        # Pie chart for sentiment distribution based on news source
        st.subheader('Persebaraan Sentimen Berdasarkan Berita')
        selected_source = st.selectbox('Pilih Berita:', data['asal_berita'].unique(), key='select_berita')
        filtered_data = data[data['asal_berita'] == selected_source]
        create_pie_chart(filtered_data['sentimen'], 'Persebaraan Sentimen Berdasarkan Berita dari ' + selected_source)


        
    except Exception as e:
        logger.error(f"Error in home_content: {e}")
        st.error(f"An error occurred while processing your request: {e}")

