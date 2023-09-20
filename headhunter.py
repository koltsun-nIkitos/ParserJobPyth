import requests # библиотека для запросов
from bs4 import BeautifulSoup # библиотека для работы с html

ITEMS = 100
URL = f'https://spb.hh.ru/search/vacancy?text=преподаватель&items_on_page={ITEMS}'

HEADERS = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
} # очень важный параметр для обхода блокировки браузером неавторизованного запроса

def extract_max_page():
    """ Получает общее количество страниц """

    

    # Запрос на сервер 1-ссылка запроса, 2-заголовки
    hh_request = requests.get(URL, headers=HEADERS) 
    hh_soup = BeautifulSoup(hh_request.text, 'html.parser') # создаем объект, понимающий HTML

    pages = [] # список страниц

    paginator = hh_soup.find_all("span", {'class':'pager-item-not-in-short-range'}) # найти все span-ы с классом

    for page in paginator: # перебираем все страницы (span-ы)
        pages.append(int(page.find('a').text)) # добавляем в список числа от текста ссылки


    return pages[-1] # находим последний элемент (страницу)

def extract_job(html):
    """ Получает данные из вакансии """
    title = html.find('a').text # название вакансии
    company = html.find('div', {'class' : 'vacancy-serp-item__meta-info-company'}).find('a').text # название компании
    company = company.strip() # обрезка лишних пробелов

    return {
            'title' : title, 
            'company' : company
            }

def extract_hh_jobs(last_page):
    """ Возвращает список вакансий """
    jobs = []
    #for page in range(last_page):
    result = requests.get(f'{URL}&page=0', headers=HEADERS)
    #print(result.status_code) # Статус код для получения информации о запросе
    soup = BeautifulSoup(result.text, 'html.parser') # создаем объект, понимающий HTML
    results = soup.find_all('div', {'class' : 'serp-item'})

    for result in results: # обход всех вакансий
        job = extract_job(result)
        jobs.append(job)

    return jobs