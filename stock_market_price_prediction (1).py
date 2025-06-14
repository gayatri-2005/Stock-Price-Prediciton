# -*- coding: utf-8 -*-
"""Stock Market Price Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-bGpbXljAem_bXq8vZE3FfXdtddwVDH7
"""

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

# Download stock data for Google (GOOG)
ticker = "GOOG"
df = yf.download(ticker, start="2024-08-01", end="2024-11-30")
df = df[["Open", "High", "Low", "Volume", "Close"]]
df.dropna(inplace=True)
df.columns = [f'{col}_{ticker}' for col in df.columns]

df.columns = [col.split(',')[0].replace("('", "").replace("'", "").strip().capitalize() for col in df.columns]
df.columns

# Create lag features for 'Close'
for lag in range(1, 6):
    df[f"Close_lag_{lag}"] = df["Close"].shift(lag)

df.dropna(inplace=True)

# Features and target
feature_cols = [
    "Open",
    "High",
    "Low",
    "Volume",
    *[f"Close_lag_{i}" for i in range(1, 6)]
]
X = df[feature_cols]
y = df["Close"]

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

model = XGBRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediction on test data
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}")

df.columns

import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf

# Step 1: Data Collection
ticker = "GOOG"
df = yf.download(ticker, start="2024-08-01", end="2024-12-01")
df = df[["Open", "High", "Low", "Volume", "Close"]]

# Step 2: Create lag features for 'Close'
for i in range(1, 6):
    df[f"Close_lag_{i}"] = df["Close"].shift(i)

df.dropna(inplace=True)

# Step 3: Feature and target setup
features = ["Open", "High", "Low", "Volume"] + [f"Close_lag_{i}" for i in range(1, 6)]
target = "Close"

X = df[features]
y = df[target]















