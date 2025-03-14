import streamlit as st
import streamlit.components.v1 as components
from components import recommendations

# Apply theme from the config file
st.set_page_config(
    page_title="Аналитика по городу",
    page_icon="🏙️",
    layout="centered",
    initial_sidebar_state="collapsed"  # Hide sidebar
)

# Adding custom CSS styles using components.html
components.html("""
    <style>
    .container-xxl.d-flex.flex-column.flex-shrink-0.p-3 {
        width: 100%;
        background-color: #f8f9fa; /* Light gray background */
        padding: 20px; /* Add padding */
        border-radius: 10px; /* Rounded corners */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow */
    }
    .st-emotion-cache-z5fcl4 {
        display: none !important; /* Hide Streamlit menu */
    }
    </style>
    """, height=0)

# Directly display recommendations.app()
recommendations.app()

