# Books_RecSys

## The Smart Book Search project for russian users 📚
### Task 📍:
To develop a system for recommending books based on a user request. The user enters a promt with a description of the book he wants to receive - the model gives a set number of recommended books.

### Steps of work 💪:
1. Data parsing. I used an online bookstore https://www.biblio-globus.ru . The main problem was the parsing of different genres. I solved it by creating a dictionary with genres in the cycle, in which the key was the name of the genre, and the value was a link to a section of the catalog. As a result, we managed to collect about 5000 books, although initially several hundred more were planned, but not all book cards were allowed to be parsed. The final dataset has 6 columns: page url, image url, author, genre, title, annotation.

2. Creating the model. It was necessary to implement two models.

• First model: SentenceTransformer(sentence-transformers/all-mpnet-base-v2) and FAISS libraries(IndexFlatIP) for efficient similarity search.

• Second model: cointegrated/rubert-tiny2 and Cosine similarity is used as a metric

3. The app on streamlit via hugging face.

### How to run locally? 💻
1. To create a Python virtual environment for running the code, enter:

`python3 -m venv my-env`

2. Activate the new environment:

Windows:
```my-env\Scripts\activate.bat```

MacOS and Linux:
```source my-env/bin/activate```

3. Install all dependencies from the requirements.txt file:

```pip install -r requirements.txt```
