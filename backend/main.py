from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os
from typing import List

from hybrid_logic import predict_hybrid

# --------------------------------------------------
# APP SETUP
# --------------------------------------------------
app = FastAPI(
    title="HARIS – Hybrid AI Risk Intelligence System for Wildfires"
)

# --------------------------------------------------
# CORS (VERY IMPORTANT)
# --------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# INPUT SCHEMAS
# --------------------------------------------------
class Type1Input(BaseModel):
    fire_count: int
    avg_frp: float
    max_frp: float
    night_fire_ratio: float
    confidence_score: float
    fire_trend: int


class Type2Input(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    rainfall: float


class PredictRequest(BaseModel):
    type1: Type1Input
    type2: Type2Input


# --------------------------------------------------
# OUTPUT SCHEMA
# --------------------------------------------------
class PredictResponse(BaseModel):
    type1_risk: str
    type2_risk: str
    hybrid_score: float
    final_risk: str
    explanation: List[str]


# --------------------------------------------------
# LOAD MODELS ON STARTUP
# --------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

type1_bundle = joblib.load(
    os.path.join(PROJECT_ROOT, "models", "type1_model.pkl")
)
type2_bundle = joblib.load(
    os.path.join(PROJECT_ROOT, "models", "type2_model.pkl")
)

type1_model = type1_bundle["model"]
type1_features = type1_bundle["features"]

type2_model = type2_bundle["model"]
type2_features = type2_bundle["features"]

# --------------------------------------------------
# ROUTES
# --------------------------------------------------
@app.get("/")
def root():
    return {
        "message": "HARIS Backend – Wildfire Risk Prediction API is running"
    }


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    try:
        result = predict_hybrid(
            type1=request.type1,
            type2=request.type2,
            type1_model=type1_model,
            type1_features=type1_features,
            type2_model=type2_model,
            type2_features=type2_features,
        )
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --------------------------------------------------
# LOCAL DEV ENTRY POINT
# --------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
