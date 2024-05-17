import streamlit as st
from home import home_content
from page1 import page1_content
from page2 import page2_content
from loguru import logger
import tornado.websocket

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
            except tornado.websocket.WebSocketClosedError as ws_error:
                logger.error(f"WebSocket closed error in Beranda page: {ws_error}")
                st.warning("WebSocket connection closed unexpectedly. Please reload the page.")
            except Exception as e:
                logger.error(f"Error loading Beranda page: {e}")
                st.error("Failed to load Beranda page")

        elif page == 'Model Klasfikasi':
            try:
                logger.info("Loading Model Klasfikasi page")
                page1_content()
                logger.info("Model Klasfikasi page loaded successfully")
            except tornado.websocket.WebSocketClosedError as ws_error:
                logger.error(f"WebSocket closed error in Model Klasfikasi page: {ws_error}")
                st.warning("WebSocket connection closed unexpectedly. Please reload the page.")
            except Exception as e:
                logger.error(f"Error loading Model Klasfikasi page: {e}")
                st.error("Failed to load Model Klasfikasi page")

        elif page == 'Model LDA dan LSA':
            try:
                logger.info("Loading Model LDA dan LSA page")
                page2_content()
                logger.info("Model LDA dan LSA page loaded successfully")
            except tornado.websocket.WebSocketClosedError as ws_error:
                logger.error(f"WebSocket closed error in Model LDA dan LSA page: {ws_error}")
                st.warning("WebSocket connection closed unexpectedly. Please reload the page.")
            except Exception as e:
                logger.error(f"Error loading Model LDA dan LSA page: {e}")
                st.error("Failed to load Model LDA dan LSA page")
                
    except Exception as e:
        logger.error(f"Error in main function: {e}")
        st.error("An error occurred while processing your request.")

if __name__ == "__main__":
    main()
