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