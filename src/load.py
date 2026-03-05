def load(df):
    df.to_csv("data/cleaned_data.csv", index=False)
    print("Data Loaded Successfully")
