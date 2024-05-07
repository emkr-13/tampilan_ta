import streamlit as st
from home import home_content
from page1 import page1_content
from page2 import page2_content
from page3 import page3_content

def main():
    st.sidebar.title('Menu ')
    page = st.sidebar.radio("Mau Kemana nih", ('Beranda','Klasifikasi Teks', 'Sentimen Analisis','Topik Analisis'))
    if page == 'Beranda':
        home_content()
    elif page == 'Klasifikasi Teks':
        page1_content()
    elif page == 'Sentimen Analisis':
        page2_content()
    elif page == 'Topik Analisis':
        page3_content()

if __name__ == "__main__":
    main()
