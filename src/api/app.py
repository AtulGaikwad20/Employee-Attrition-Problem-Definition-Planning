
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT / "models" / "best_attrition_model.joblib"
METADATA_PATH = ROOT / "models" / "model_metadata.json"

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model not found at {MODEL_PATH}. Run src/models/train_models.py first."
    )

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="Employee Attrition Analytics API",
    description="Predicts employee attrition risk using a trained machine learning model.",
    version="1.0.0",
)


class EmployeeInput(BaseModel):
    Age: int = Field(ge=18, le=100)
    BusinessTravel: str
    DailyRate: float = Field(ge=0)
    Department: str
    DistanceFromHome: int = Field(ge=0)
    Education: int = Field(ge=1, le=5)
    EducationField: str
    EnvironmentSatisfaction: int = Field(ge=1, le=4)
    Gender: str
    HourlyRate: float = Field(ge=0)
    JobInvolvement: int = Field(ge=1, le=4)
    JobLevel: int = Field(ge=1, le=5)
    JobRole: str
    JobSatisfaction: int = Field(ge=1, le=4)
    MaritalStatus: str
    MonthlyIncome: float = Field(ge=0)
    MonthlyRate: float = Field(ge=0)
    NumCompaniesWorked: int = Field(ge=0)
    OverTime: str
    PercentSalaryHike: int = Field(ge=0)
    PerformanceRating: int = Field(ge=1, le=5)
    RelationshipSatisfaction: int = Field(ge=1, le=4)
    StockOptionLevel: int = Field(ge=0, le=3)
    TotalWorkingYears: int = Field(ge=0)
    TrainingTimesLastYear: int = Field(ge=0)
    WorkLifeBalance: int = Field(ge=1, le=4)
    YearsAtCompany: int = Field(ge=0)
    YearsInCurrentRole: int = Field(ge=0)
    YearsSinceLastPromotion: int = Field(ge=0)
    YearsWithCurrManager: int = Field(ge=0)


@app.get("/")
def home():
    return {
        "message": "Employee Attrition Analytics API is running",
        "docs": "/docs",
        "prediction_endpoint": "/predict",
    }


@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": model is not None}


@app.post("/predict")
def predict(employee: EmployeeInput):
    try:
        employee_data = pd.DataFrame([employee.model_dump()])
        probability = float(model.predict_proba(employee_data)[0][1])
        prediction = int(probability >= 0.5)

        if probability >= 0.60:
            risk_category = "High"
        elif probability >= 0.30:
            risk_category = "Medium"
        else:
            risk_category = "Low"

        return {
            "attrition_prediction": "Yes" if prediction else "No",
            "attrition_probability": round(probability, 4),
            "risk_category": risk_category,
            "threshold": 0.5,
            "note": "Use predictions as decision support, not as the sole basis for employment decisions.",
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Prediction failed. Check that the supplied employee fields are valid.") from None
