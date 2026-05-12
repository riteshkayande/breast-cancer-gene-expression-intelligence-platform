import pandas as pd


def load_data(file_path):
    print("Loading dataset...")
    
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    return lines


def clean_data(lines):
    print("Cleaning dataset...")
    
    cleaned = [line for line in lines if not line.startswith("!")]
    
    return cleaned


def normalize_data(data):
    print("Normalizing dataset...")
    
    # placeholder normalization logic
    return data


if __name__ == "__main__":
    file_path = "data/raw/GSE2034_series_matrix.txt"
    
    raw = load_data(file_path)
    clean = clean_data(raw)
    final = normalize_data(clean)
    
    print("Pipeline executed successfully")
