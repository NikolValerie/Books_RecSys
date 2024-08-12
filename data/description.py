import streamlit as st

@st.cache_data
def app_description_page():
    st.image('data/2024-04-19 14.05.03.jpg', use_column_width=True)
    st.markdown("""
        <style>
            /* Пользовательские стили */
            .title-shadow {
                font-weight: bold;
                font-size: 26px; /* Уменьшен размер шрифта для заголовка */
                color: #333333; /* Темно-серый цвет для заголовка */
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* Слегка заметная тень для заголовка */
            }
            .text-content {
                font-size:18px;
                color: #333333; /* Темно-серый цвет для лучшего контраста */
            }
            .subtitle {
                font-size:22px; /* Размер шрифта для подзаголовка */
                color: #333333; /* Цвет подзаголовка */
            }
            hr {
                border: none;
                height: 3px; /* Более толстая линия для разделения */
                background: #CCCCCC; /* Светло-серая линия */
                margin: 24px 0; /* Большой отступ после линии */
            }
            .team-title {
                font-size:20px; /* Размер шрифта для названия команды */
                color: #333333; /* Цвет для названия команды */
                margin-bottom: 0.5em; /* Отступ перед списком команды */
            }
        </style>
        """, unsafe_allow_html=True)
    # Title of the app
    st.markdown("<h1 style='text-align: center; color: #333333;'>Приложение для Рекомендации&nbsp;Книг</h1>", unsafe_allow_html=True)
    # Description of the app
    st.write("Это приложение предлагает подборку книг, основываясь на вводе пользователя. Введите желаемое описание книги, и система порекомендует подходящие книги.")
    # Project description subtitle
    st.markdown("<h2 style='color: #333333;'>📚 Описание проекта</h2>", unsafe_allow_html=True)
    # Points about the project
    st.markdown("""
        **1. Парсинг данных с сайта Библио-Глобус:**
        - Информация о книгах различных жанров собирается с помощью веб-парсера.
        - Создается словарь жанров для систематизированного сбора данных.
        - Около 5,000 книг собраны в базу данных приложения.
        
        **2. Модели:**
        1) SentenceTransformer (sentence-transformers/all-mpnet-base-v2) и библиотека FAISS (IndexFlatIP)
        
        IndexFlatIP:
        - идеально подходит для работы с многомерными векторами, которые представляют аннотации книг.
        - обеспечивает быстрый и точный поиск на основе косинусного сходства.
           
        2) cointegrated/rubert-tiny2 
        
        **Преимущества косинусного сходства:**
        - Нечувствительность метрики к длине векторов, обеспечивает точное сравнение текстов разной длины.
        - Возможность высокоточной оценки семантического сходства между текстами.
        
        **3. Приложение на Streamlit:**
        - Удобный интерфейс пользователя разработан с использованием Streamlit.
        - Приложение размещено через Hugging Face, делая его доступным для пользователей по всему миру.
    """)
    
    st.markdown("<br><br>", unsafe_allow_html=True)


