import streamlit as st
st.set_page_config(
    page_title="El Salvador Division Research Culture Framework",
    layout="wide"
)
from cdr_twin.ui import app
if __name__ == "__main__":
    app()
