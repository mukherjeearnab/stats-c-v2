import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString

with open('data.csv', 'w') as f:
    f.write(f'recovery,active,date\n')

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
for row in rows:
    # print(row.attrs['class'])
    # if 'class="bb-lr"' in row:
    #     print(True)
    # else:
    #     print(False)

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

    # print(tds)

    if len(tds) == 0:
        continue

    divs = []
    for td in tds:
        divs = td.find_all(lambda tag: tag.name == 'div'
                           and tag.has_attr('style')
                           )

    # print(divs)

    if len(divs) == 0:
        continue

    actv, recv = 0, 0
    for div in divs:
        if not ('background:Tomato;' in div['style'] or 'background:SkyBlue;' in div['style']):
            continue

        # if i == 0

        # Active
        if 'background:SkyBlue;' in div['style']:
            recv = int(div['title'])
        elif 'background:Tomato;' in div['style']:
            actv = int(div['title'])
        # Recovery

    print(recv, actv, date)
    # break
    with open('data.csv', 'a') as f:
        f.write(f'{recv},{actv},{date}\n')


# print()
