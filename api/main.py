from fastapi import FastAPI
from src.schemas import VineyardFeatures, RiskResponse
from src.predict import predict_cluster_and_risk

from src.predict import predict_cluster_and_risk, _features  # if you keep _features exported
# OR load features inside predict.py and expose a helper



app = FastAPI(title="Vineyard Risk API", version="1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=RiskResponse)
def predict(features: VineyardFeatures):
    return predict_cluster_and_risk(features.model_dump())


@app.post("/predict_debug")
def predict_debug(features: VineyardFeatures):
    payload = features.model_dump()
    out = predict_cluster_and_risk(payload)
    return {
        "input": payload,
        "cluster": out["cluster"],
        "risk_level": out["risk_level"]
    }
