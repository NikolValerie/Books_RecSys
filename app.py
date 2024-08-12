import streamlit as st
from pages.rubert.app_bert import ruBert_page
from pages.mpnet_base.mpnet_base_app import mpnet_base_page
from data.description import app_description_page

st.markdown("""
    <style>
        /* Основной фон страницы */
        body {
            background-color: #FFC0CB;  /* Нежно-розовый цвет */
        }
        /* Фон основной панели, чтобы убрать несоответствующие цвета */
        .stApp {
            background-color: #FFC0CB; /* Нежно-розовый цвет для основной панели */
        }
        /* Фон и текст боковой панели */
        .stSidebar > div:first-child {
            background-color: #FFC0CB; /* Нежно-розовый цвет для боковой панели */
            color: #FFFFFF; /* Белый цвет текста для контраста */
        }
        .stSidebar .sidebar-content {
            color: #FFFFFF;
        }
        /* Стиль заголовка боковой панели */
        .stSidebar .sidebar-content h1, .stSidebar .sidebar-content h2, .stSidebar .sidebar-content h3 {
            color: #FFFFFF;
        }
        /* Стиль кнопок */
        .stButton > button {
            background-color: #FF69B4; /* Ярко-розовый цвет кнопок */
            color: #FFFFFF; /* Белый текст на кнопках */
        }
        /* Стили текстового поля */
        .stTextInput input {
            background-color: #FFFFFF; /* Белый фон текстового поля */
            color: #FF69B4; /* Ярко-розовый текст */
        }
        /* Стили активной кнопки радио и чекбокса */
        .stRadio > label > div:first-of-type > div, .stCheckbox > label > div:first-of-type > div {
            background-color: #FF69B4; /* Ярко-розовый фон для активных кнопок радио и чекбоксов */
            border-color: #FF69B4;
        }
        /* Стили слайдера */
        .stSlider > div > div > div > div {
            background-color: #FF69B4; /* Ярко-розовый цвет слайдера */
        }
    </style>
""", unsafe_allow_html=True)

def main():
    st.sidebar.title("Book app")
    page = st.sidebar.radio("Select page:", ["About Project", "📚 Book search", "🔍 Book search (faiss)"])
    if page == "About Project":
        app_description_page()
    if page == "📚 Book search":
        ruBert_page()
    if page == "🔍 Book search (faiss)":
        mpnet_base_page()


if __name__ == "__main__":
    main()