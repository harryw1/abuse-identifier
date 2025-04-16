# %% imports
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# %% load data
df = pd.read_csv("/Users/harrisonweiss/Documents/abuse-identifier/data/output.csv")
df.head()

# %% create regressor
rfc = RandomForestClassifier()

# %% create training/testing sets
X = df.drop(columns=["is_bot","date_created"])
y = df["is_bot"]
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=0
)

# %% fit the model
rfc.fit(X_train, y_train)

# %% score the model
rfc.score(X_test, y_test)
