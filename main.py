import requests # библиотека для запросов
from bs4 import BeautifulSoup # библиотека для работы с html

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
} # очень важный параметр для обхода блокировки браузером неавторизованного запроса

# Запрос на сервер 1-ссылка запроса, 2-заголовки
hh_request = requests.get('https://spb.hh.ru/search/vacancy?text=преподаватель&items_on_page=100', headers=headers) 
hh_soup = BeautifulSoup(hh_request.text, 'html.parser') # создаем объект, понимающий HTML

pages = [] # список страниц

paginator = hh_soup.find_all("span", {'class':'pager-item-not-in-short-range'}) # найти все span-ы с классом

for page in paginator: # перебираем все страницы (span-ы)
    pages.append(int(page.find('a').text)) # добавляем в список числа от текста ссылки


max_page = pages[-1] # находим последний элемент (страницу)