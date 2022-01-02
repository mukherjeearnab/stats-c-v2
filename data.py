import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./timeseries_india.csv')

# data = data[data['Country'] == 'India']

print(data)


plt.plot(data['date'], data['new_active'])
plt.show()
