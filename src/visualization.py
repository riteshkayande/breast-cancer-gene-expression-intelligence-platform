# Visualization module

def plot_heatmap():
    pass

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def run_pca(df):
    print("Running PCA...")

    # convert to numeric
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.fillna(df.mean())

    pca = PCA(n_components=2)
    result = pca.fit_transform(df)

    print("Explained variance:", pca.explained_variance_ratio_)

    return result


def plot_pca(result):
    print("Plotting PCA...")

    plt.scatter(result[:, 0], result[:, 1])
    plt.title("PCA of Breast Cancer Gene Expression")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.show()


if __name__ == "__main__":
    # dummy load (replace with your pipeline output later)
    file_path = "data/raw/GSE2034_series_matrix.txt"

    df = pd.read_csv(file_path, sep="\t", comment="!")

    result = run_pca(df)
    plot_pca(result)