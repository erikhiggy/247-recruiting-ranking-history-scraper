import urllib.request
from bs4 import BeautifulSoup

year_range = range(2020, 2021)


def parse_page_of_recruits(url):
    request = urllib.request.Request(
        url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    rankings_page_div = soup.find('div', class_='rankings-page__main')
    list_items = rankings_page_div.find_all(
        'li', class_='rankings-page__list-item')
    for list_item in list_items:
        name_link = list_item.find('a', class_='rankings-page__name-link')
        if(name_link != None):
            print(name_link['href'].split('-')[-1])
            print(name_link.text)


for year in year_range:
    for page_index in range(1, 2):
        url = f'https://247sports.com/Season/{year}-Football/CompositeRecruitRankings/?page={page_index}'
        print(url)
        parse_page_of_recruits(url)
