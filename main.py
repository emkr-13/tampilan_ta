import streamlit as st
from home import home_content
from page1 import page1_content
from page2 import page2_content

def main():
    st.sidebar.title('Menu ')
    page = st.sidebar.radio("Mau Kemana nih", ('Beranda','Model Klasfikasi', 'Model LDA dan LSA'))
    if page == 'Beranda':
        home_content()
    elif page == 'Model Klasfikasi':
        page1_content()
    elif page == 'Model LDA dan LSA':
        page2_content()

if __name__ == "__main__":
    main()
