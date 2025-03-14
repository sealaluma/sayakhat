import streamlit as st
from streamlit_lottie import st_lottie
import json
import streamlit.components.v1 as components
import math
import json
import time

# Функция для загрузки данных из GeoJSON файла
def load_geojson_data(file_path):
    with open(file_path, "r") as f:
        geojson_data = json.load(f)
    return geojson_data   

def app():
    with open("components/business.html", "r") as f:
        map_html = f.read()
        components.html(map_html, height=600)