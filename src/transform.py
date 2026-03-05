def transform(df):
    df = df.dropna()
    df.columns = df.columns.str.lower()
    print("Data Transformed Successfully")
    return df
