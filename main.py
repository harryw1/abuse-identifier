# %% imports
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, train_test_split

# %% load data
df = pd.read_csv("./data/output.csv")
df.head()

# %% create regressor
rfc = RandomForestClassifier()

# %% create training/testing sets
X = df.drop(columns=["is_bot", "date_created"])
y = df["is_bot"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# %% fit the model
rfc.fit(X_train, y_train)

# %% score the model
rfc.score(X_test, y_test)

# %% hyperparameter tuning
tuned_rf = RandomForestClassifier()
param_grid = {
    "n_estimators": [int(x) for x in np.linspace(start=100, stop=1000, num=10)],
    "max_features": ["auto", "sqrt"],
    "max_depth": [int(x) for x in np.linspace(5, 50, 10)],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "bootstrap": [True, False],
}
rfc_tuned = RandomizedSearchCV(
    estimator=tuned_rf, param_distributions=param_grid, n_iter=100, cv=3, n_jobs=-1
)

# %% fit the new model
rfc_tuned.fit(X_train, y_train)


# %% test accuracy
def evaluate(model, test_features, test_labels):
    predictions = model.predict(test_features)
    errors = abs(predictions - test_labels)
    mape = 100 * np.mean(errors / test_labels)
    accuracy = 100 - mape
    print("Model Performance")
    print("Average Error: {:0.4f} degrees.".format(np.mean(errors)))
    print("Accuracy = {:0.2f}%.".format(accuracy))

    return accuracy


print(f"Base accuracy: {evaluate(rfc, X_test, y_test)}")
print(f"Tuned accuracy: {evaluate(rfc_tuned, X_test, y_test)}")
