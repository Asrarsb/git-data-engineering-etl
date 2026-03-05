def transform(df):
    df = df.dropna()
    df.columns = df.columns.str.lower()
    print("Rows after cleaning:", len(df))
    print("Data Transformed Successfully")
    return df