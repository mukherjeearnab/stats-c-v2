import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')

sns.set()

# Set plot of current
plt.figure(figsize=(90.00, 10.80))
plt.plot(data['date'], data['recovery'], label='Recovery')
plt.plot(data['date'], data['active'], label='Active')
plt.ylabel('Cases')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.legend()
plt.savefig('current.png', format='png', bbox_inches='tight')
plt.clf()

# Set plot of new
plt.plot(data['date'], data['new_recovery'], label='Recovery')
plt.plot(data['date'], data['new_active'], label='Active')
plt.plot(data['date'], data['new_death'], label='Death')
plt.ylabel('New Cases')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.legend()
plt.savefig('new.png', format='png', bbox_inches='tight')
