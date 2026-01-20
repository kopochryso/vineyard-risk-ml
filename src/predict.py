import pandas as pd
from src.artifacts import load_artifacts

_features, _scaler, _kmeans, _risk_map = load_artifacts()

def predict_cluster_and_risk(payload: dict) -> dict:
    # Build a 1-row dataframe and enforce training column order
    X = pd.DataFrame([payload]).reindex(columns=_features)

    # Scale and predict
    X_scaled = _scaler.transform(X)
    cluster = int(_kmeans.predict(X_scaled)[0])
    risk = _risk_map.get(cluster, "UNKNOWN")

    return {"cluster": cluster, "risk_level": risk}
