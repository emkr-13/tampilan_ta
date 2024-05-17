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
        data = pd.read_csv('resource/dataset_berita_indo.csv')
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
        # st.write(data.random(10))
        st.markdown("""
            \n Di karena dataset load data yang besar maka tidak menampilkan dataset maka dari untuk melihat dataset pada huggeface di link berikut : https://huggingface.co/datasets/emkr-13/Dataset_Berita_Indo
                    """)
        st.text(f"Jumlah Baris Data = {data.shape[0]}")
    
        # Pie chart for news source distribution
        st.subheader('Persebaraan Berita')
        create_pie_chart(data['asal_berita'], 'Persebaraan Berita')
    
        data['tanggal_berita'] = pd.to_datetime(data['tanggal_berita'], format='%Y-%m-%d')
        data['bulan'] = data['tanggal_berita'].dt.month_name()
        news_by_month = data['bulan'].value_counts().sort_index()
        st.subheader('Persebaraan Berita Berdasarkan Bulan')
        plot_bar_chart(news_by_month, 'Bulan', 'Frequency', 'Persebaraan Berita Berdasarkan Bulan')
        
        # Filtered bar chart for news distribution based on news source
        st.subheader('Persebaraan Berita Berdasarkan Bulan dan Asal Berita')
        selected_source = st.selectbox('Pilih Asal Berita:', data['asal_berita'].unique())
        filtered_data = data[data['asal_berita'] == selected_source]
        news_by_month_filtered = filtered_data['bulan'].value_counts().sort_index()
        plot_bar_chart(news_by_month_filtered, 'Bulan', 'Frequency', 'Persebaraan Berita Berdasarkan Bulan dari ' + selected_source)
    
        st.header('Sentimen Analsis')
        st.write("Sentimen analsis berdasarkan dataset yang digunakaan ")
        # Pie chart for sentiment distribution
        st.subheader('Persebaraan Sentimen')
        create_pie_chart(data['sentimen'], 'Persebaraan Sentimen')
        
        # Pie chart for sentiment distribution based on news source
        st.subheader('Persebaraan Sentimen Berdasarkan Berita')
        selected_source = st.selectbox('Pilih Berita:', data['asal_berita'].unique(), key='select_berita')
        filtered_data = data[data['asal_berita'] == selected_source]
        create_pie_chart(filtered_data['sentimen'], 'Persebaraan Sentimen Berdasarkan Berita dari ' + selected_source)
        
        # Bar chart for sentiment distribution based on month of news date
        sentimen_by_month = data.groupby(['bulan', 'sentimen']).size().unstack(fill_value=0)
        st.subheader('Persebaraan Sentimen Berdasarkan Bulan')
        plot_bar_chart(sentimen_by_month, 'Bulan', 'Frequency', 'Persebaraan Sentimen Berdasarkan Bulan')
    
        # Bar chart for sentiment distribution based on month of news date and news source
        sentimen_by_month_and_source = data.groupby(['bulan', 'sentimen', 'asal_berita']).size().unstack(fill_value=0)
        st.subheader('Persebaraan Sentimen Berdasarkan Bulan dan Asal Berita')
        plot_bar_chart(sentimen_by_month_and_source, 'Bulan', 'Frequency', 'Persebaraan Sentimen Berdasarkan Bulan dan Asal Berita')
    
        # Line chart for sentiment distribution per day for a specific month
        selected_month = st.selectbox('Pilih Bulan:', data['bulan'].unique(), key='select_bulan')
        filtered_data = data[data['bulan'] == selected_month]
        sentiment_by_day = filtered_data.groupby(filtered_data['tanggal_berita'].dt.day)['sentimen'].value_counts().unstack(fill_value=0)
        st.subheader('Persebaraan Sentimen per hari Berdasarkan Bulan ' + selected_month)
        plot_line_chart(sentiment_by_day, 'Tangggal', 'Frequency', 'Persebaraan Sentimen per hari Berdasarkan Bulan ' + selected_month)
    except Exception as e:
        logger.error(f"Error in home_content: {e}")
        st.error("An error occurred while processing your request.")