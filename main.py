import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="Grade 4 CoTh Assessment",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hide default Streamlit padding and UI elements for a full-screen app feel
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        iframe {
            width: 100vw;
            height: 100vh;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Read and render the HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Render full screen HTML component
components.html(html_code, height=1000, scrolling=True)
