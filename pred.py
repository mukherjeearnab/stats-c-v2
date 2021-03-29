from statsmodels.tsa.holtwinters import ExponentialSmoothing
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

STEPS = 720

data = pd.read_csv('data.csv')

# fit recovery
model = ExponentialSmoothing(data['recovery'])
model_fit = model.fit()
# make prediction
recovery = model_fit.forecast(steps=STEPS)

# fit active
model = ExponentialSmoothing(data['active'])
model_fit = model.fit()
# make prediction
active = model_fit.forecast(steps=STEPS)


sns.set()
# plt.tight_layout()
# plt.subplots_adjust(left=0.5, right=0.5)
# plt.figure(figsize=(80.00, 10.80))
plt.plot(range(0, STEPS), recovery, label='Recovery')
plt.plot(range(0, STEPS), active, label='Active')
plt.ylabel('Cases')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.legend()
plt.savefig('pred.png', format='png', bbox_inches='tight')
