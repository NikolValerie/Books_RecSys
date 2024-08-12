import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import time

# Загрузка данных
@st.cache_data
def load_data_models():
    data = pd.read_csv('data/books_data2.csv')
    data['annotation'] = data['annotation'].astype(str)
    with open('pages/mpnet_base/mpnet_base_embeddings.pkl', 'rb') as f:
        book_embeddings = pickle.load(f)

    index = faiss.read_index('pages/mpnet_base/mpnet_base_index.index')
    embedder = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

    return data, book_embeddings, index, embedder

data, book_embeddings, index, embedder = load_data_models()

# Функция для поиска
def search_books(query, num_results):
    query_embedding = embedder.encode([query], convert_to_tensor=True)
    query_embedding_cpu = query_embedding.cpu()
    query_embedding_normalized = query_embedding_cpu / np.linalg.norm(query_embedding_cpu, axis=1)
    D, I = index.search(np.array(query_embedding_normalized), num_results)
    return I[0], D[0] 

# Streamlit
def mpnet_base_page():
    st.title('Поиск книг')
    user_input = st.text_input("Введите цитату или автора:")
    results_num = st.slider("Количество результатов", min_value=1, max_value=20, value=5)

    if st.button('Искать'):
        start_time = time.time() 
        indices, distances = search_books(user_input, results_num)
        end_time = time.time()  
        search_time = end_time - start_time
        st.write("Результаты поиска:")
        for idx, dist in zip(indices, distances):
            book = data.iloc[idx]
            st.write("---")
            st.image(book['image_url'], width=250)
            st.write(f"**Название:** {book['title']}")
            st.write(f"**Автор:** {book['author']}")
            st.write(f"**Жанр:** {book['genre']}")
            if len(book['annotation']) > 50:
                book['annotation'] = ' '.join(book['annotation'].split()[:50]) + '...'
            st.write(f"**Описание:** {book['annotation']}")
            st.write(f"**Метрика близости:** {dist}")
            st.write(f'**Время поиска:** {search_time:.4f} секунд')
            st.markdown(f"[Читать подробнее]({book['page_url']})", unsafe_allow_html=True)

