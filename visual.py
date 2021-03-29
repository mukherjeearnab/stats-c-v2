import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')

sns.set()
# plt.tight_layout()
# plt.subplots_adjust(left=0.5, right=0.5)
plt.figure(figsize=(80.00, 10.80))
plt.plot(data['date'], data['recovery'], label='Recovery')
plt.plot(data['date'], data['active'], label='Active')
plt.ylabel('Cases')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.legend()
plt.savefig('current.png', format='png', bbox_inches='tight')
