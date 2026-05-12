def extract_expression_matrix(file_path):
    print("Extracting gene expression matrix...")

    with open(file_path, "r") as f:
        lines = f.readlines()

    # remove metadata lines
    data_lines = [line for line in lines if not line.startswith("!")]

    print("Total usable lines:", len(data_lines))

    return data_lines


if __name__ == "__main__":
    file_path = "data/raw/GSE2034_series_matrix.txt"
    matrix = extract_expression_matrix(file_path)