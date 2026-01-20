import joblib

FEATURES_PATH = "models/features.pkl"
SCALER_PATH = "models/scaler.pkl"
KMEANS_PATH = "models/kmeans.pkl"
RISK_MAP_PATH = "models/risk_map.pkl"

def load_artifacts():
    features = joblib.load(FEATURES_PATH)
    scaler = joblib.load(SCALER_PATH)
    kmeans = joblib.load(KMEANS_PATH)
    risk_map = joblib.load(RISK_MAP_PATH)
    return features, scaler, kmeans, risk_map
