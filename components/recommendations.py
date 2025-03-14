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

    # Создаем и добавляем легенду
    legend_html = """
    <div class="legend">
        <div class="label-left">Минимум</div>
        <div class="gradient"></div>
        <div class="label-right">Максимум</div>
    </div>
    """
    st.markdown(legend_html, unsafe_allow_html=True)

    # CSS стили для легенды
    st.markdown(
        """
        <style>
        .legend {
            position: relative;
            width: 100%;
            margin: 0 auto;
            text-align: center;
            background-color: white;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .gradient {
            width: 60%; /* Достаточно места для текста */
            height: 20px;
            background: linear-gradient(to right, blue, cyan, yellow, orange, red);
            display: inline-block;
            margin: 0 10px;
        }

        .label-left,
        .label-right {
            display: inline-block;
            width: 80px; /* Увеличенная ширина для текста */
            text-align: center;
            white-space: nowrap;
        }

        .label-left {
            text-align: right;
        }

        .label-right {
            text-align: left;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar:
        with open("data/comp.json", "r", errors='ignore') as f:
            data = json.load(f)
        st_lottie(data)

    st.markdown("""
    <style>
    /* Стилизация заголовков */
    .stTextInput label {
        font-size: 18px;
    }

    /* Стилизация input fields */
    .stTextInput input {
        font-size: 18px;
        padding: 10px;
        margin: 5px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2); /* Добавление тени */
    }

    /* Стилизация блоков input, включая метки и поля */
    .stTextInput {
        background: #FFFFFF; /* Белый фон */
        border-radius: 5px;
        margin-bottom: 10px; /* Отступ снизу */
    }

    /* Стилизация кнопки */
    .stButton > button {
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 5px;
        border: none;
        color: white;
        background-color: #183F71;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2); /* Добавление тени */
        transition: background-color 0.3s, box-shadow 0.3s, opacity 0.3s;
    }

    .stButton > button:active {
        background-color: transparent; /* Прозрачный фон при нажатии */
        color: #183F71; /* Цвет текста при нажатии */
        box-shadow: none; /* Убрать тень */
        opacity: 0.6; /* Немного прозрачности для визуального отклика */
    }

    /* Стилизация заголовков input */
    .stNumberInput label {
        font-size: 24px;
        font-weight: bold;
        color: #062042; /* Темно-синий цвет текста */
    }

    /* Стилизация контейнера input */
    .stNumberInput > div {
        margin-bottom: 10px; /* Отступ снизу для каждого input */
    }

    /* Стилизация поля input */
    .stNumberInput input {
        font-size: 18px;
        padding: 10px; /* Побольше padding для удобства */
        border-radius: 5px; /* Скругленные углы */
        border: 1px solid #ced4da; /* Светло-серая граница */
        background-color: #f8f9fa; /* Светло-серый фон поля ввода */
    }

    /* Стилизация самого виджета input (может понадобиться дополнительная стилизация) */
    .stNumberInput {
        border: none; /* Убрать рамку, если она есть */
    }

    /* Стилизация кнопок управления "+" и "-" */
    .stNumberInput .step-up, .stNumberInput .step-down {
        background-color: #f8f9fa; /* Светло-серый фон кнопок */
    }

    /* Применить стиль ко всем кнопкам внутри виджета number input */
    .stNumberInput button {
        border: 1px solid #ced4da; /* Светло-серая граница */
        background-color: #f8f9fa; /* Светло-серый фон кнопок */
        color: #333; /* Цвет текста */
    }

    /* Указать стиль при наведении */
    .stNumberInput button:hover {
        background-color: #e2e6ea; /* Немного темнее при наведении */
    }
    </style>
    """, unsafe_allow_html=True)
