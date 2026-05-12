import pandas as pd


def load_clean_lines(file_path):
    print("Reading GEO file...")

    with open(file_path, "r") as f:
        lines = f.readlines()

    # remove metadata lines
    clean_lines = [line.strip() for line in lines if not line.startswith("!")]

    return clean_lines


def extract_matrix(lines):
    print("Extracting expression matrix...")

    data = []

    for line in lines:
        parts = line.split("\t")
        if len(parts) > 5:   # ensures real data row
            data.append(parts)

    df = pd.DataFrame(data)

    print("Matrix shape:", df.shape)

    return df


if __name__ == "__main__":
    file_path = "data/raw/GSE2034_series_matrix.txt"

    lines = load_clean_lines(file_path)
    df = extract_matrix(lines)

    print(df.head())

import pandas as pd
import numpy as np


def load_clean_matrix(file_path):
    print("Loading GEO dataset...")

    with open(file_path, "r") as f:
        lines = f.readlines()

    # remove metadata
    data_lines = [line.strip() for line in lines if not line.startswith("!")]

    return data_lines


def to_dataframe(lines):
    print("Converting to DataFrame...")

    data = []

    for line in lines:
        parts = line.split("\t")
        if len(parts) > 10:   # ensures expression row
            data.append(parts)

    df = pd.DataFrame(data)

    print("Raw shape:", df.shape)

    return df


def clean_numeric(df):
    print("Cleaning numeric values...")

    # replace missing values
    df = df.replace("", np.nan)
    df = df.dropna()

    return df


def normalize(df):
    print("Applying log normalization...")

    # convert everything to numeric where possible
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.fillna(df.mean())

    # log transform (common in gene expression)
    df = np.log1p(df)

    return df


if __name__ == "__main__":
    file_path = "data/raw/GSE2034_series_matrix.txt"

    lines = load_clean_matrix(file_path)
    df = to_dataframe(lines)
    df = clean_numeric(df)
    df = normalize(df)

    print("Final dataset shape:", df.shape)
    print(df.head())