import pandas as pd

URL = 'https://www.isibang.ac.in/~athreya/incovid19/dataopen/summarymohfw1update.csv'

# Load Dataset
data = pd.read_csv(URL)

# Replace Column with new row
data = (data.T.reset_index().T.reset_index(drop=True)
            .set_axis([f'Q1.{i+1}' for i in range(data.shape[1])], axis=1))
# Transpose it
data.set_index('Q1.1', inplace=True)
data = data.transpose()

# data.reset_index()


print(data.columns)

# Remove duplicate dates
data = data[data['NUMBERS'].str.contains("TCIN")]


print(data)

dates = data['DATES'].to_list()
total = data['Totals'].to_list()

with open('./timeseries_india_isib.csv', 'w') as f:
    f.write('date,confirmed,new_active\n')

for i, cases in enumerate(total[1:]):
    if cases <= total[i]:
        continue

    active = int(cases) - int(total[i])
    date = dates[i+1].split('.')[0]

    with open('./timeseries_india_isib.csv', 'a') as f:
        f.write(f'{date},{cases},{active}\n')
