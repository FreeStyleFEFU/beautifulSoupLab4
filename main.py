import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 YaBrowser/20.12.2.105 Yowser/2.5 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}


def generate_matr_links():

    with open("links_list.html", "w", encoding='utf-8') as file:

        file.writelines('<html>')
        file.writelines('<body>')
        file.writelines('<table>')

        for i in range(1, 11):
            file.writelines('<tr>')

            for j in range(1, 11):
                file.writelines(f'<td><a href="http:/{i * j}.ru">{i * j}</a></td>')

            file.writelines('</tr>')

        file.writelines('</table>')
        file.writelines('</body>')
        file.writelines('</html>')


def article_unique_content_between_code_tags():
    response = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)', headers=HEADERS).text
    code_tags = BeautifulSoup(response, 'html.parser').find_all('code')

    unique_content = {}

    for tag in code_tags:
        try:
            unique_content[tag.text] += 1
        except:
            unique_content[tag.text] = 1

    print(dict((sorted(unique_content.items(), key=lambda x: x[1], reverse=True))))


def sum():
    with open("ntab.html", "r", encoding='utf-8') as file:

        sum = 0
        table_cells = BeautifulSoup(file.read(), 'html.parser').find_all('td')

        for cell in table_cells:
            sum += int(cell.text)

        print(sum)

def html_to_csv():
    response = requests.get('https://en.wikipedia.org/wiki/Vladivostok', headers=HEADERS).text
    table = str(BeautifulSoup(response, 'html.parser').find('table', class_='wikitable mw-collapsible'))

    table_rows = BeautifulSoup(table, 'html.parser').find_all('tr')

    list_rows = []



    for row in table_rows:
        list_rows.append([])
        row_content = BeautifulSoup(str(row), 'html.parser').find_all(['th', 'td'])
        for cell in row_content:
            list_rows[-1].append(cell.text[0:len(cell.text)-1])

    with open("climate.csv", "w", encoding='utf-8') as file:
        for row in list_rows:
            file.writelines(','.join(row) + '\n')


generate_matr_links()

article_unique_content_between_code_tags()

sum()

html_to_csv()

