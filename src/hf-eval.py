"""Module testing the use of an hf dataset for training."""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

categories = [
    "hate",
    "offensive",
    "neither"
]

df = pd.read_parquet("hf://datasets/tdavidson/hate_speech_offensive/data/train-00000-of-00001.parquet")

X = df["tweet"]
y = df["class"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2
)

vectorizer = TfidfVectorizer(
    sublinear_tf=True, max_df=0.5, min_df=5, stop_words="english"
)
X_train = vectorizer.fit_transform(X_train)

X_test = vectorizer.transform(X_test)

clf = RidgeClassifier(tol=1e-2, solver="sparse_cg")
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

fig,ax = plt.subplots(figsize=(10,5))
ConfusionMatrixDisplay.from_predictions(y_test, pred, ax=ax)
ax.xaxis.set_ticklabels(categories)
ax.yaxis.set_ticklabels(categories)
__ = ax.set_title(
    f"Confusion Matrix for {clf.__class__.__name__}\n on the dataset"
)
plt.show()
