''' objetivo construir um crawler da fonte legislabahia usando apenas python'''
from bs4 import BeautifulSoup, CData
import requests
import re
link_main = 'https://www.legislabahia.ba.gov.br'

response = requests.get(link_main).text

soup = BeautifulSoup(response, 'html.parser')
categories = soup.find('tbody').find_all('a') # 'td', class_='views-field')
links_categories = []
for n in categories:
    links_categories.append((n.get('href')))
# criar outro for p/ links_categorias e identar

href_law_ordinarias = categories[7].get('href')
print('href:', href_law_ordinarias)

response_ordinarias = requests.get(link_main+href_law_ordinarias).text
law_ordinarias = BeautifulSoup(response_ordinarias, 'html.parser')
law_ordinarias.prettify()
line_table = law_ordinarias.find('table', class_='table').find('tbody').find_all('tr')
#spans = law_ordinarias.find('table', class_='table').find('tbody').find_all('span')
#td_categorias = law_ordinarias.find('table', class_='table').find('tbody').find_all('td', class_='views-field-field-categoria-doc')

print(type(line_table[1]))

for line in line_table:    
    line = line.get_text()

    array = (line.strip().splitlines())
    array.remove(array[2])
    #print((line.replace('                              ', ',')))
    print('lei: ', array[0], 'texto: ', array[1].strip(), 'categoria: ', array[2])
    #print(line.prettify(), '\n')
    # lei LEI Nº .* DE
    # data DE .*
    # texto </a> .* </span>
# tem que paginar

# for item in links_categorias_str:
#     if 'Leis Ordinárias' in item:
#         print(item)


