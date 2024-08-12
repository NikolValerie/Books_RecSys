import streamlit as st
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
from scipy.spatial.distance import cosine
import pandas as pd
import time 

@st.cache_data
def load_data():
    book_embeddings = np.load('pages/rubert/embeddings.npz')
    all_embeddings = book_embeddings['embeddings']

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny2")
    model = AutoModel.from_pretrained("cointegrated/rubert-tiny2").to(device)
    data = pd.read_csv('data/books_data2.csv')
    return all_embeddings, device, tokenizer, model, data

# Функция для получения эмбеддинга

def embed_text(text, tokenizer, model, device):
    encoded_input = tokenizer(text, padding=True, truncation=True, max_length=128, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**encoded_input.to(device))
        embeddings = model_output.last_hidden_state[:,0,:].cpu().numpy()
        return np.mean(embeddings, axis=0)
    
# Функция поиска
def search_books(user_query, all_embeddings, device, tokenizer, model, data, n_results):
    query_embedding = embed_text(user_query, tokenizer, model, device)
    
    similarities = [1 - cosine(query_embedding, book_embedding) for book_embedding in all_embeddings]
    top_results_indices = np.argsort(similarities)[::-1][:n_results]
    top_similarities = np.sort(similarities)[::-1][:n_results]
    
    return top_results_indices, top_similarities

# Streamlit
def ruBert_page():
    st.title("Поиск книг")
    all_embeddings, device, tokenizer, model, data = load_data()

    user_query = st.text_input("Введите цитату или автора:")
    n_results = st.slider("Количество результатов", min_value=1, max_value=20, value=5)

    if st.button("Искать"):
        start_time = time.time() 
        top_books_indices, top_similarities = search_books(user_query, all_embeddings, device, tokenizer, model, data, n_results)
        end_time = time.time()  
        search_time = end_time - start_time  
        st.write("Результаты поиска:")
        for i, idx in enumerate(top_books_indices):
            st.write('---')
            similarity = top_similarities[i]
            st.image(data.loc[idx, 'image_url'], width=250)
            st.write(f"**Название:** {data.loc[idx, 'title']}")
            st.write(f"**Автор:** {data.loc[idx, 'author']}")
            st.write(f"**Жанр:** {data.loc[idx, 'genre']}")
            annotation = data.loc[idx, 'annotation']
            if len(annotation) > 50:
                annotation = ' '.join(annotation.split()[:50]) + '...'
            st.write(f"**Описание:** {annotation}")
            st.write(f"**Косинусное сходство:** {similarity:.3f}")
            st.write(f'**Время поиска:** {search_time:.4f} секунд')
            st.markdown(f"[Читать подробнее]({data.loc[idx, 'page_url']})")
    

        