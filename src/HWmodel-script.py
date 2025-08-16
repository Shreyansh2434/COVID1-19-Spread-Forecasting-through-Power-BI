import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = dataset.copy()

df['Date'] = pd.to_datetime(
    df['Month'].astype(str) + ' ' +
    df['Day'].astype(str) + ' ' +
    df['Year'].astype(str),
    format='%B %d %Y'
)

df = df.sort_values('Date')
series = df.set_index('Date')['Spread Rate %']

fit = ExponentialSmoothing(
    series,
    trend='add',
    seasonal=None,
    initialization_method='estimated'
).fit(optimized=True)

last_date = series.index.max()
future = pd.date_range(start=last_date + pd.Timedelta(days=1),
                       end='2023-12-31', freq='D')
forecast = fit.forecast(len(future))
forecast.index = future

plt.figure(figsize=(10, 6))
plt.plot(series, label='Historical', linewidth=2)
plt.plot(forecast, label='Forecast', linestyle='--', linewidth=2)
plt.fill_between(forecast.index,
                 forecast * 0.9,
                 forecast * 1.1,
                 color='orange', alpha=0.2, label='±10%')

plt.title('COVID-19 Spread Rate %: Actual vs Forecast', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Spread Rate %', fontsize=12)
plt.legend(loc='upper left')
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
