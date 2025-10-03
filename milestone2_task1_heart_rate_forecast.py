 Step 1: Import required libraries
import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

# Step 2: Create sample heart rate data for 60 days
np.random.seed(42)  # for reproducibility
dates = pd.date_range(start='2023-01-01', periods=60)
heart_rate = 70 + np.random.normal(0, 2, size=60)  # average ~70 bpm with noise
df = pd.DataFrame({'ds': dates, 'y': heart_rate})

# Step 3: Fit Prophet model
model = Prophet()
model.fit(df)

# Step 4: Make 14-day forecast
future = model.make_future_dataframe(periods=14)
forecast = model.predict(future)

# Step 5: Visualize results
fig = model.plot(forecast)
plt.title("Heart Rate Forecast")
plt.xlabel("Date")
plt.ylabel("Heart Rate (bpm)")
plt.show()

# Step 6: Calculate MAE (Mean Absolute Error)
# Simulate actual heart rate for next 14 days
actual = 70 + np.random.normal(0, 2, size=14)
predicted = forecast['yhat'][-14:].values
mae = mean_absolute_error(actual, predicted)
print(f"Mean Absolute Error (MAE): {mae:.2f}")

# Step 7: Forecasted heart rate for Day 67
day_67 = forecast.iloc[66]  # Day 67 is index 66
print(f"Forecasted heart rate for Day 67: {day_67['yhat']:.2f} bpm")
print(f"Confidence Interval: [{day_67['yhat_lower']:.2f}, {day_67['yhat_upper']:.2f}] bpm")
