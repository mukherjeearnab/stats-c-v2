from datetime import timedelta, datetime
import pandas as pd

data = pd.read_csv('preds-17-4-21.csv')


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = datetime(2021, 4, 17)
end_date = start_date + timedelta(days=200)
index = 0

dalis = []

for single_date in daterange(start_date, end_date):
    print(data['prediction'][index], single_date.strftime("%Y-%m-%d"), index)
    dalis.append(single_date.strftime("%Y-%m-%d"))
    index += 1

se = pd.Series(dalis)
data['date'] = se

data.to_csv('prediction.csv', index=False)
