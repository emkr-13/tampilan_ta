import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

# Load the dataset only once
# @st.cache(allow_output_mutation=True)
@st.cache_data 
def load_data():
    dataset = load_dataset("emkr-13/Dataset_Online_News_45000")
    return dataset['train'].to_pandas()

# Function to create pie chart
def create_pie_chart(data, title):
    counts = data.value_counts()
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    st.write("Persebaraan Data:")
    st.write(counts)

# Function to plot bar chart
def plot_bar_chart(data, xlabel, ylabel, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    data.plot(kind='bar', ax=ax)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    st.pyplot(fig)
    st.write("Persebaraan Data:")
    st.write(data)

# Function to plot line chart
def plot_line_chart(data, xlabel, ylabel, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    data.plot(kind='line', ax=ax)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    st.pyplot(fig)
    st.write("Persebaraan Data:")
    st.write(data)


def home_content():
    st.title('Selamat Datang di Sentimen Analisis dan Topik Analisis Berita')
    st.write('Selamat datang di website saya Di sini, saya menyajikan hasil skripsi saya tentang Sentimen Analisis dan Topik Analisis Berita.')
        # Load the dataset
    data = load_data()

    st.title('Sentimen Analisis')

    # Display random 5 rows of the data
    st.subheader('Data 5 Random')
    st.write(data.sample(5))

    # Pie chart for news source distribution
    st.subheader('Persebaraan Berita')
    create_pie_chart(data['asal_berita'], 'Persebaraan Berita')
    
    # Pie chart for sentiment distribution
    st.subheader('Persebaraan Sentimen')
    create_pie_chart(data['sentimen'], 'Persebaraan Sentimen')
    
    # Pie chart for sentiment distribution based on news source
    st.subheader('Persebaraan Sentimen Berdasarkan Berita')
    selected_source = st.selectbox('Pilih Berita:', data['asal_berita'].unique())
    filtered_data = data[data['asal_berita'] == selected_source]
    create_pie_chart(filtered_data['sentimen'], 'Persebaraan Sentimen Berdasarkan Berita dari ' + selected_source)
    
    # Bar chart for sentiment distribution based on month of news date
    data['tanggal_berita'] = pd.to_datetime(data['tanggal_berita'], format='%Y-%m-%d')
    data['bulan'] = data['tanggal_berita'].dt.month_name()
    sentimen_by_month = data.groupby(['bulan', 'sentimen']).size().unstack(fill_value=0)
    st.subheader('Persebaraan Sentimen Berdasarkan Bulan')
    plot_bar_chart(sentimen_by_month, 'Bulan', 'Frequency', 'Persebaraan Sentimen Berdasarkan Bulan')

    # Bar chart for sentiment distribution based on month of news date and news source
    sentimen_by_month_and_source = data.groupby(['bulan', 'sentimen', 'asal_berita']).size().unstack(fill_value=0)
    st.subheader('Persebaraan Sentimen Berdasarkan Bulan dan Asal Berita')
    plot_bar_chart(sentimen_by_month_and_source, 'Bulan', 'Frequency', 'Persebaraan Sentimen Berdasarkan Bulan dan Asal Berita')

    # Line chart for sentiment distribution per day for a specific month
    selected_month = st.selectbox('Pilih Bulan:', data['bulan'].unique())
    filtered_data = data[data['bulan'] == selected_month]
    sentiment_by_day = filtered_data.groupby(filtered_data['tanggal_berita'].dt.day)['sentimen'].value_counts().unstack(fill_value=0)
    st.subheader('Persebaraan Sentimen per hari Berdasarkan Bulan ' + selected_month)
    plot_line_chart(sentiment_by_day, 'Tangggal', 'Frequency', 'Persebaraan Sentimen per hari Berdasarkan Bulan ' + selected_month)
