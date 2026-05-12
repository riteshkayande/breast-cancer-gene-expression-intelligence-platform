# Explainable AI module

def generate_shap_plots():
    pass

import shap
import matplotlib.pyplot as plt


def explain_model(model, X):
    print("Running SHAP Explainability...")

    explainer = shap.Explainer(model, X)
    shap_values = explainer(X)

    return shap_values


def plot_summary(shap_values, X):
    print("Plotting SHAP summary...")

    shap.summary_plot(shap_values, X)


def plot_feature_importance(model, X):
    print("Feature importance (if available)...")

    try:
        import pandas as pd

        importance = model.feature_importances_
        features = X.columns

        df = pd.DataFrame({
            "Feature": features,
            "Importance": importance
        }).sort_values(by="Importance", ascending=False)

        print(df.head(10))

    except:
        print("Model does not support feature importance")


if __name__ == "__main__":
    print("SHAP module ready - connect trained model here")