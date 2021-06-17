import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString

with open('data.csv', 'w') as f:
    f.write(f'recovery,active,death,new_recovery,new_active,new_death,date\n')

url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India'
page = requests.get(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})


soup = BeautifulSoup(page.content, "html.parser")

table_div = soup.find(lambda tag: tag.name == 'div'
                      and tag.has_attr('class')
                      and 'barbox' in tag['class'])


# print(table_div)

table = table_div.find(lambda tag: tag.name == 'table')

rows = table.find_all(lambda tag: tag.name == 'tr')
print("ROWS", len(rows))

# Memory
p_recv, p_actv, p_dts = 0, 0, 0

for row in rows:
    if 'Date' in row.text or 'Ministry' in row.text:
        continue

    if not (row.has_attr('class')):  # and 'mw-collapsible' in row['class']):
        continue

    # Dates
    td = row.find(lambda tag: tag.name == 'td'
                  and tag.has_attr('class')
                  #   and tag.has_attr('style')
                  and 'bb-c' in tag['class']
                  #   and 'text-align:center' in tag['style']
                  )

    date = td.contents[0]

    # Case Stats
    tds = row.find_all(lambda tag: tag.name == 'td'
                       and tag.has_attr('class')
                       and 'bb-b' in tag['class']
                       )

    if len(tds) == 0:
        continue

    divs = []
    for td in tds:
        divs = td.find_all(lambda tag: tag.name == 'div'
                           and tag.has_attr('style')
                           )

    if len(divs) == 0:
        continue

    actv, recv, dts = 0, 0, 0
    for div in divs:
        if 'background:SkyBlue;' in div['style']:
            recv = int(div['title'])
        elif 'background:Tomato;' in div['style']:
            actv = int(div['title'])
        else:
            dts = int(div['title'])

    # Calculate Changes
    n_recv, n_dts = recv - p_recv, dts - p_dts
    n_actv = n_recv + n_dts + actv - p_actv

    # Set Previous
    p_recv, p_actv, p_dts = recv, actv, dts

    print(recv, actv, dts, n_recv, n_actv, n_dts, date)

    with open('data.csv', 'a') as f:
        f.write(f'{recv},{actv},{dts},{n_recv},{n_actv},{n_dts},{date}\n')


# print()
