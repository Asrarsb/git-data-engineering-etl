import pandas as pd

def extract():
    df = pd.read_csv("data/raw_data.csv")
    print("Data Extracted Successfully")
    return df
