import pickle

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)