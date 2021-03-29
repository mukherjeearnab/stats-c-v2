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

table = soup.find(lambda tag: tag.name == 'table'
                  and tag.has_attr('style')
                  and tag['style'] == "text-align:left; border-collapse:collapse; width:100%;"
                  )

rows = table.find_all(lambda tag: tag.name == 'tr')
print(len(rows))

# Memory
p_recv, p_actv, p_dts = 0, 0, 0

for row in rows:

    if not (row.has_attr('class')):  # and 'mw-collapsible' in row['class']):
        continue

    td = row.find(lambda tag: tag.name == 'td'
                  and tag.has_attr('class')
                  and tag.has_attr('style')
                  and 'bb-04em' in tag['class']
                  and 'text-align:center' in tag['style']
                  )

    date = td.contents[0]

    tds = row.find_all(lambda tag: tag.name == 'td'
                       and tag.has_attr('class')
                       and 'bb-lr' in tag['class']
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
