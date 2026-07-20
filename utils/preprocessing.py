import pandas as pd

def load_data():
    df = pd.read_csv("data/dataset_graf.csv")
    return df