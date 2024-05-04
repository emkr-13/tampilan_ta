import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

def page2_content():
    # Load the dataset
    data = pd.read_csv('resource/online_news_50000_clean_label_all.csv')
    st.title('Sentimen Analysis')
    # Set page title
    st.title('Online News Analysis')

    # Display random 5 rows of the data
    st.subheader('Random 5 Data')
    st.write(data.sample(5))

    # Pie chart for sentiment distribution
    sentimen_counts = data['sentimen'].value_counts()
    st.subheader('Sentimen Distribution')
    fig_sentimen, ax_sentimen = plt.subplots()
    ax_sentimen.pie(sentimen_counts, labels=sentimen_counts.index, autopct='%1.1f%%', startangle=90)
    ax_sentimen.axis('equal')
    st.pyplot(fig_sentimen)
    st.write("Numerical Data:")
    st.write(sentimen_counts)
    
    # Pie chart for news source distribution
    asal_berita_counts = data['asal_berita'].value_counts()
    st.subheader('News Source Distribution')
    fig_asal_berita, ax_asal_berita = plt.subplots()
    ax_asal_berita.pie(asal_berita_counts, labels=asal_berita_counts.index, autopct='%1.1f%%', startangle=90)
    ax_asal_berita.axis('equal')
    st.pyplot(fig_asal_berita)
    st.write("Numerical Data:")
    st.write(asal_berita_counts)
    
 # Bar chart for sentiment distribution based on month of news date
    data['tanggal_berita'] = pd.to_datetime(data['tanggal_berita'], format='%d-%m-%Y')
    data['bulan'] = data['tanggal_berita'].dt.month_name()
    sentimen_by_month = data.groupby(['bulan', 'sentimen']).size().unstack(fill_value=0)

    st.subheader('Sentimen Distribution by Month')
    fig_sentimen_by_month, ax_sentimen_by_month = plt.subplots(figsize=(10, 6))
    sentimen_by_month.plot(kind='bar', ax=ax_sentimen_by_month)
    ax_sentimen_by_month.set_ylabel('Frequency')
    st.pyplot(fig_sentimen_by_month)
    st.write("Numerical Data:")
    st.write(sentimen_by_month)

    # Bar chart for sentiment distribution based on month of news date and news source
    sentimen_by_month_and_source = data.groupby(['bulan', 'sentimen', 'asal_berita']).size().unstack(fill_value=0)

    st.subheader('Sentimen Distribution by Month and News Source')
    fig_sentimen_by_month_and_source, ax_sentimen_by_month_and_source = plt.subplots(figsize=(12, 8))
    sentimen_by_month_and_source.plot(kind='bar', ax=ax_sentimen_by_month_and_source)
    ax_sentimen_by_month_and_source.set_ylabel('Frequency')
    st.pyplot(fig_sentimen_by_month_and_source)
    st.write("Numerical Data:")
    st.write(sentimen_by_month_and_source)