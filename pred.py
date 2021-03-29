from statsmodels.tsa.arima.model import ARIMA
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

STEPS = 30

data = pd.read_csv('data.csv')

# fit recovery
model = ARIMA(data['new_recovery'], order=(1, 1, 1))
model_fit = model.fit()
# make prediction
recovery = model_fit.forecast(steps=STEPS)

# fit active
model = ARIMA(data['new_active'], order=(1, 1, 1))
model_fit = model.fit()
# make prediction
active = model_fit.forecast(steps=STEPS)


sns.set()
plt.plot(range(0, STEPS), recovery, label='Recovery')
plt.plot(range(0, STEPS), active, label='Active')
plt.ylabel('Cases')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.legend()
plt.savefig('pred.png', format='png', bbox_inches='tight')
