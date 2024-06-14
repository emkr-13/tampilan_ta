import os.path
from datasets import load_dataset
import pandas as pd
from loguru import logger

# Function to download dataset if not exist
def download_dataset(file_path):
    # Muat dataset jika belum ada
    if not os.path.exists(file_path):
        dataset = load_dataset("emkr-13/berita_pemilu_2024")
        df = pd.DataFrame(dataset['train'])
        df.to_csv(file_path, index=False)
        logger.info("Dataset telah diunduh dan disimpan sebagai CSV di:", file_path)

# Path to save CSV file
file_path = "resource/dataset_pemilu_2024.csv"

# Download dataset if not exist
download_dataset(file_path)

import streamlit as st
from home import home_content
from page1 import page1_content
from page2 import page2_content
from loguru import logger

# Initialize logger
logger.add("app.log", rotation="500 MB")

def main():
    try:
        st.sidebar.title('Menu ')
        page = st.sidebar.radio("Mau Kemana nih", ('Beranda', 'Model Klasfikasi', 'Model LDA dan LSA'))
        
        if page == 'Beranda':
            try:
                logger.info("Loading Beranda page")
                home_content()
                logger.info("Beranda page loaded successfully")
            except Exception as e:
                logger.error(f"Error loading Beranda page: {e}")
                st.error(f"Failed to load Beranda page {e}")

        elif page == 'Model Klasfikasi':
            try:
                logger.info("Loading Model Klasfikasi page")
                page1_content()
                logger.info("Model Klasfikasi page loaded successfully")
            except Exception as e:
                logger.error(f"Error loading Model Klasfikasi page: {e}")
                st.error(f"Failed to load Model Klasfikasi page {e}")

        elif page == 'Model LDA dan LSA':
            try:
                logger.info("Loading Model LDA dan LSA page")
                page2_content()
                logger.info("Model LDA dan LSA page loaded successfully")
            except Exception as e:
                logger.error(f"Error loading Model LDA dan LSA page: {e}")
                st.error(f"Failed to load Model LDA dan LSA page {e}")
                
    except Exception as e:
        logger.error(f"Error in main function: {e}")
        st.error("An error occurred while processing your request.")

if __name__ == "__main__":
    main()
