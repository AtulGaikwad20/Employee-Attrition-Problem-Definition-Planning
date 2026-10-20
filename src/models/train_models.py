
from pathlib import Path
import json
import time

import joblib
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
MODEL_DIR = ROOT / "models"
REPORT_DIR = ROOT / "reports"

MODEL_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = pd.read_csv(DATA_PATH)

    df = df.drop(
        columns=[
            "EmployeeCount",
            "EmployeeNumber",
            "Over18",
            "StandardHours",
        ],
        errors="ignore",
    )

    y = df["Attrition"].map({"No": 0, "Yes": 1})
    X = df.drop(columns=["Attrition"])

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    numeric_features = X.select_dtypes(include=["number"]).columns.tolist()
    categorical_features = X.select_dtypes(exclude=["number"]).columns.tolist()

    numeric_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessing = ColumnTransformer(
        [
            ("numeric", numeric_pipeline, numeric_features),
            ("categorical", categorical_pipeline, categorical_features),
        ]
    )

    models = {
        "Logistic Regression": LogisticRegression(
            max_iter=2000,
            class_weight="balanced",
            random_state=42,
        ),
        "Neural Network": MLPClassifier(
            hidden_layer_sizes=(64, 32),
            max_iter=500,
            early_stopping=True,
            random_state=42,
        ),
        "Naive Bayes": GaussianNB(),
        "Linear Discriminant Analysis": LinearDiscriminantAnalysis(),
    }

    results = []
    best_score = -1
    best_name = None
    best_pipeline = None

    for name, estimator in models.items():
        pipeline = Pipeline(
            [
                ("preprocessing", preprocessing),
                ("model", estimator),
            ]
        )

        start = time.time()
        pipeline.fit(X_train, y_train)
        training_seconds = round(time.time() - start, 3)

        predictions = pipeline.predict(X_test)
        probabilities = pipeline.predict_proba(X_test)[:, 1]

        scores = {
            "model": name,
            "accuracy": round(accuracy_score(y_test, predictions), 4),
            "precision": round(
                precision_score(y_test, predictions, zero_division=0), 4
            ),
            "recall": round(
                recall_score(y_test, predictions, zero_division=0), 4
            ),
            "f1_score": round(
                f1_score(y_test, predictions, zero_division=0), 4
            ),
            "roc_auc": round(roc_auc_score(y_test, probabilities), 4),
            "training_seconds": training_seconds,
        }

        results.append(scores)
        print(scores)

        if scores["roc_auc"] > best_score:
            best_score = scores["roc_auc"]
            best_name = name
            best_pipeline = pipeline

    results_df = pd.DataFrame(results).sort_values(
        "roc_auc", ascending=False
    )

    results_df.to_csv(REPORT_DIR / "advanced_model_comparison.csv", index=False)

    joblib.dump(best_pipeline, MODEL_DIR / "best_attrition_model.joblib")

    metadata = {
        "selected_model": best_name,
        "selection_metric": "ROC-AUC",
        "test_roc_auc": best_score,
        "features": X.columns.tolist(),
        "target": "Attrition",
    }

    with open(MODEL_DIR / "model_metadata.json", "w", encoding="utf-8") as file:
        json.dump(metadata, file, indent=4)

    print("\nModel comparison:")
    print(results_df.to_string(index=False))
    print(f"\nBest model: {best_name}")
    print(f"Saved model: {MODEL_DIR / 'best_attrition_model.joblib'}")
    print(f"Saved results: {REPORT_DIR / 'advanced_model_comparison.csv'}")


if __name__ == "__main__":
    main()
