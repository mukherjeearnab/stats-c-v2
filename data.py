import pandas as pd

data = pd.read_csv('./timeseries_india.csv')

# data = data[data['Country'] == 'India']

print(data)


import matplotlib.pyplot as plt

plt.plot(data['date'], data['new_confirmed'])
plt.show()