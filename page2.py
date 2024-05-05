import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

def create_pie_chart(data, title):
    counts = data.value_counts()
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    st.write("Numerical Data:")
    st.write(counts)

def plot_bar_chart(data, xlabel, ylabel, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    data.plot(kind='bar', ax=ax)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    st.pyplot(fig)
    st.write("Numerical Data:")
    st.write(data)

def plot_line_chart(data, xlabel, ylabel, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    data.plot(kind='line', ax=ax)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    st.pyplot(fig)
    st.write("Numerical Data:")
    st.write(data)

def page2_content():
    # Load the dataset
    data = pd.read_csv('resource/online_news_50000_clean_label_all.csv')
    st.title('Sentimen Analysis')
   #  st.title('Online News Analysis')

    # Display random 5 rows of the data
    st.subheader('Random 5 Data')
    st.write(data.sample(5))

    # Pie chart for news source distribution
    st.subheader('News Source Distribution')
    create_pie_chart(data['asal_berita'], 'News Source Distribution')
    
        # Pie chart for sentiment distribution
    st.subheader('Sentiment Distribution')
    create_pie_chart(data['sentimen'], 'Sentiment Distribution')
    
    # Pie chart for sentiment distribution
    st.subheader('Sentiment Distribution')
    selected_source = st.selectbox('Select News Source:', data['asal_berita'].unique())
    filtered_data = data[data['asal_berita'] == selected_source]
    create_pie_chart(filtered_data['sentimen'], 'Sentiment Distribution for ' + selected_source)
    
    # Bar chart for sentiment distribution based on month of news date
    data['tanggal_berita'] = pd.to_datetime(data['tanggal_berita'], format='%d-%m-%Y')
    data['bulan'] = data['tanggal_berita'].dt.month_name()
    sentimen_by_month = data.groupby(['bulan', 'sentimen']).size().unstack(fill_value=0)
    st.subheader('Sentiment Distribution by Month')
    plot_bar_chart(sentimen_by_month, 'Month', 'Frequency', 'Sentiment Distribution by Month')

    # Bar chart for sentiment distribution based on month of news date and news source
    sentimen_by_month_and_source = data.groupby(['bulan', 'sentimen', 'asal_berita']).size().unstack(fill_value=0)
    st.subheader('Sentiment Distribution by Month and News Source')
    plot_bar_chart(sentimen_by_month_and_source, 'Month', 'Frequency', 'Sentiment Distribution by Month and News Source')

    # Line chart for sentiment distribution per day for a specific month
    selected_month = st.selectbox('Select a month:', data['bulan'].unique())
    filtered_data = data[data['bulan'] == selected_month]
    sentiment_by_day = filtered_data.groupby(filtered_data['tanggal_berita'].dt.day)['sentimen'].value_counts().unstack(fill_value=0)
    st.subheader('Sentiment Distribution per Day for ' + selected_month)
    plot_line_chart(sentiment_by_day, 'Day', 'Frequency', 'Sentiment Distribution per Day for ' + selected_month)

