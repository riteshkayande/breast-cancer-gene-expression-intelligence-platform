# Evaluation module

def evaluate_model():
    pass

import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    RocCurveDisplay
)


def evaluate_model(model, X_test, y_test, model_name="Model"):
    print(f"\nEvaluating {model_name}")

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    cm = confusion_matrix(y_test, preds)
    report = classification_report(y_test, preds)

    print("Accuracy:", acc)
    print("\nConfusion Matrix:\n", cm)
    print("\nClassification Report:\n", report)

    return acc


def plot_roc(model, X_test, y_test, model_name="Model"):
    try:
        RocCurveDisplay.from_estimator(model, X_test, y_test)
        plt.title(f"ROC Curve - {model_name}")
        plt.show()
    except:
        print("ROC not available for this model")


def compare_models(results):
    print("\nMODEL COMPARISON TABLE")
    for name, acc in results.items():
        print(f"{name}: {acc}")