from pydantic import BaseModel

class VineyardFeatures(BaseModel):
    ndvi_mean: float
    ndvi_max: float
    ndvi_min: float
    ndvi_std: float
    ndvi_slope: float
    ndvi_drop: float

class RiskResponse(BaseModel):
    cluster: int
    risk_level: str
