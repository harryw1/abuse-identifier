# %% imports
import numpy as np
import pandas as pd
from pandas.core.arrays.datetimelike import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# %% load data
df = pd.read_csv("./data/output.csv")
df.head()

# %% convert date feature
df['date_created'] = pd.to_datetime(df['date_created'])

# %% create usable features from datetime object
# Time components
df['creation_year'] = df['date_created'].dt.year
df['creation_month'] = df['date_created'].dt.month
df['creation_day'] = df['date_created'].dt.day
df['creation_dayofweek'] = df['date_created'].dt.dayofweek
df['creation_quarter'] = df['date_created'].dt.quarter

# Derived time features
reference_date = pd.Timestamp('2000-01-01')
df['days_since_2000'] = (df['date_created'] - reference_date).dt.days

current_date = pd.Timestamp(datetime.now().date())
df['account_age_days'] = (current_date - df['date_created']).dt.days

# Cyclical encoding for periodic features
df['month_sin'] = np.sin(2 * np.pi * df['creation_month']/12)
df['month_cos'] = np.cos(2 * np.pi * df['creation_month']/12)

df['dayofweek_sin'] = np.sin(2 * np.pi * df['creation_dayofweek']/7)
df['dayofweek_cos'] = np.cos(2 * np.pi * df['creation_dayofweek']/7)

# %% create features and targets
X = df.drop(columns=['is_bot', 'date_created'])
y = df['is_bot']

# %% split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# %% classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# %% score
clf.score(X_test, y_test)
