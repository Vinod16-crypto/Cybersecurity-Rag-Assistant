"""
Train a basic intrusion detection model.
Recommended dataset: UNSW-NB15 or CICIDS2017 CSV.
Expected target column: 'label', 'Label', or 'attack_cat'.
Output: models/intrusion_model.joblib
"""
import os
import argparse
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

TARGET_CANDIDATES = ["label", "Label", "attack_cat", "target"]

def find_target(df):
    for col in TARGET_CANDIDATES:
        if col in df.columns:
            return col
    raise ValueError(f"No target column found. Rename your target column to one of: {TARGET_CANDIDATES}")

def main(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna(axis=1, thresh=int(len(df) * 0.6))
    df = df.dropna()

    target = find_target(df)

    y_raw = df[target]
    if y_raw.dtype == "object":
        y = y_raw.apply(lambda x: 0 if str(x).lower() in ["normal", "benign", "0"] else 1)
    else:
        y = y_raw.astype(int)

    X = df.drop(columns=[target])
    # Remove ID-like columns if present
    for col in ["id", "srcip", "dstip", "stime", "ltime", "timestamp"]:
        if col in X.columns:
            X = X.drop(columns=[col])

    numeric_cols = X.select_dtypes(include=["int64", "float64", "int32", "float32"]).columns.tolist()
    categorical_cols = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ]
    )

    model = RandomForestClassifier(n_estimators=150, random_state=42, class_weight="balanced")
    pipe = Pipeline(steps=[("preprocess", preprocessor), ("model", model)])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    print(classification_report(y_test, preds))

    os.makedirs("models", exist_ok=True)
    joblib.dump(pipe, "models/intrusion_model.joblib")
    print("Saved model to models/intrusion_model.joblib")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="Path to intrusion detection CSV file")
    args = parser.parse_args()
    main(args.csv)
