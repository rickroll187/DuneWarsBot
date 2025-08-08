import os
import pickle
import csv
import random
from sklearn.ensemble import RandomForestClassifier

MODEL_PATH = "data/ai_strategy_model.pkl"
DATA_PATH = "data/gameplay_data.csv"

def load_data():
    X, y = [], []
    if not os.path.exists(DATA_PATH):
        return X, y
    with open(DATA_PATH, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            *features, result = row
            X.append([float(x) for x in features])
            y.append(int(result))
    return X, y

def train_ai(X, y):
    if not X:
        return
    clf = RandomForestClassifier(n_estimators=50)
    clf.fit(X, y)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(clf, f)

def predict_ai(features):
    if not os.path.exists(MODEL_PATH):
        # Fallback: random move
        return random.choice([0, 1])
    with open(MODEL_PATH, "rb") as f:
        clf = pickle.load(f)
    return clf.predict([features])[0]