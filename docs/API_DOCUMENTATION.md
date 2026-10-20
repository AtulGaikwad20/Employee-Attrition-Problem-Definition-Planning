# Employee Attrition Analytics API Documentation

## 1. Overview

The Employee Attrition Analytics API is a REST API developed using FastAPI. It uses a trained machine learning model to estimate the probability that an employee may leave an organization.

The API runs locally for this project. Deployment to IBM Watson Machine Learning was not completed because cloud account creation required credit-card verification.

## 2. Local Setup

Open PowerShell in the project root directory and install the required packages:

```powershell
py -m pip install -r requirements-deployment.txt
```

Start the API:

```powershell
py -m uvicorn src.api.app:app --reload
```

The local API address is:

`http://127.0.0.1:8000`

## 3. Available Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Displays API status and endpoint information |
| GET | `/health` | Checks API health and model loading |
| POST | `/predict` | Predicts employee attrition risk |
| GET | `/docs` | Opens interactive Swagger documentation |

## 4. Prediction Request

Send a JSON object containing all 30 employee features to `POST /predict`.

The request must include these fields:

`Age`, `BusinessTravel`, `DailyRate`, `Department`, `DistanceFromHome`, `Education`, `EducationField`, `EnvironmentSatisfaction`, `Gender`, `HourlyRate`, `JobInvolvement`, `JobLevel`, `JobRole`, `JobSatisfaction`, `MaritalStatus`, `MonthlyIncome`, `MonthlyRate`, `NumCompaniesWorked`, `OverTime`, `PercentSalaryHike`, `PerformanceRating`, `RelationshipSatisfaction`, `StockOptionLevel`, `TotalWorkingYears`, `TrainingTimesLastYear`, `WorkLifeBalance`, `YearsAtCompany`, `YearsInCurrentRole`, `YearsSinceLastPromotion`, and `YearsWithCurrManager`.

Use valid values consistent with the dataset and the API's field validation rules.

## 5. Prediction Response

A successful response contains:

- `attrition_prediction`: predicted class, `Yes` or `No`
- `attrition_probability`: estimated probability of attrition
- `risk_category`: `Low`, `Medium`, or `High`
- `threshold`: classification threshold, currently `0.5`
- `note`: reminder to use predictions as decision support

Risk categories are assigned as follows:

- High: probability greater than or equal to `0.60`
- Medium: probability greater than or equal to `0.30` and below `0.60`
- Low: probability below `0.30`

## 6. Model Information

The saved model is Logistic Regression, selected using ROC-AUC in the advanced model comparison workflow. Its recorded test ROC-AUC is `0.8032`.

A separate experiment compared baseline and tuned models and reported a ROC-AUC of `0.8120` for tuned Logistic Regression. That tuned model is not confirmed as the model currently saved for the API.

## 7. Error Handling

Invalid requests may return HTTP `422` due to request validation. Prediction failures return HTTP `400` with a general error message.

## 8. Deployment Status

The API has been tested locally. The separate `watson_deployment` folder contains files prepared for deployment, but a live IBM Watson Machine Learning endpoint and automated cloud deployment workflow have not been verified.

## 9. Responsible Use

Predictions are estimates and may be incorrect. They should not be used as the sole basis for employment decisions. Any real-world use requires appropriate privacy, fairness, security, and performance checks.