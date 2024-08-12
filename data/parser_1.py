import requests
from bs4 import BeautifulSoup
import csv
import time
from fake_useragent import UserAgent

ua = UserAgent()
headers =  {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": ua.random
}

categories = {
    'Классическая литература': 'https://www.biblio-globus.ru/catalog/category?id=226&sort=0&instock=&isdiscount=',
    'Зарубежные детективы': 'https://www.biblio-globus.ru/catalog/category?id=242&sort=0&instock=&isdiscount=',
    'Зарубежная фантастика': 'https://www.biblio-globus.ru/catalog/category?id=251&sort=0&instock=&isdiscount=',
    'Психология': 'https://www.biblio-globus.ru/catalog/category?id=6112&sort=0&instock=&isdiscount=',
    'Сказки': 'https://www.biblio-globus.ru/catalog/category?id=279&sort=0&instock=&isdiscount=',
    'Книги для бизнеса': 'https://www.biblio-globus.ru/catalog/category?id=6129&sort=0&instock=&isdiscount=',
    'Маркетинг': 'https://www.biblio-globus.ru/catalog/category?id=6141&sort=0&instock=&isdiscount='
}

with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(('genre', 'page_url', 'image_url', 'author', 'title', 'annotation'))

    for category, category_url in categories.items():
        for page_num in range(1, 70):  
            url = f'{category_url}&page={page_num}' 
            response = requests.get(url=url, headers=headers)
            if response.status_code != 200:
                print(f"Ошибка доступа к странице: {response.status_code}")
                continue

            src = response.text
            soup = BeautifulSoup(src, 'lxml')
            cards = soup.find_all("div", class_='col-lg-3 col-md-4 col-sm-6 col-6 wrp_mobile')

            if not cards:
                print("Карточки на странице отсутствуют.")
                continue

            for card in cards:
                product_url = 'https://www.biblio-globus.ru' + card.find('a')['href']
                
                product_response = requests.get(url=product_url, headers=headers)
                product_soup = BeautifulSoup(product_response.text, 'lxml')
                url_img = product_soup.find('div', class_='col-sm-12 col-md-12 col-lg-3').find('img').get('src')
                annotation_div = product_soup.find('div', id='collapseExample')
                annotation = annotation_div.get_text(strip=True) if annotation_div else 'Annotation not available'

                book_author = product_soup.find(class_='goToDescription').find('a').text.strip()
                book_title = product_soup.find(class_='item-desc').find('h1').text

                writer.writerow((category, product_url, url_img, book_author, book_title, annotation))

                #time.sleep(1)

        file.flush()