# Employee Attrition Analytics Platform

## 1. Project Overview

The Employee Attrition Analytics Platform uses machine learning to predict whether an employee may leave an organization. It compares classification models and provides an API and dashboard to support employee-retention analysis.

This project is developed for educational and research purposes.

## 2. Objectives

- Predict employee attrition using machine learning.
- Compare classification models using evaluation metrics.
- Analyze employee and job-related factors.
- Provide attrition predictions through a REST API.
- Display attrition trends and model results through a dashboard.
- Support responsible, data-informed HR analysis.

## 3. Dataset

- Dataset: IBM HR Analytics Employee Attrition
- Number of records: 1,470
- Original columns: 35
- Target variable: `Attrition`
- Target classes: `Yes` and `No`

The dataset contains employee demographics, job information, compensation-related fields, work history, and satisfaction-related information.

## 4. Machine Learning Models

The project evaluates Logistic Regression, Decision Tree, Random Forest, and XGBoost. Hyperparameter tuning and cross-validation are used for selected models.

The project also includes experiments with neural networks, Gaussian Naive Bayes, and Linear Discriminant Analysis in the local training workflow.

## 5. Model Evaluation

The following results are recorded in the project README.

| Model | Version | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---|---:|---:|---:|---:|---:|
| Logistic Regression | Baseline | 0.7517 | 0.3488 | 0.6383 | 0.4511 | 0.8032 |
| Decision Tree | Baseline | 0.7789 | 0.3043 | 0.2979 | 0.3011 | 0.5842 |
| Random Forest | Baseline | 0.8401 | 0.5000 | 0.3404 | 0.4051 | 0.7998 |
| XGBoost | Baseline | 0.8571 | 0.6667 | 0.2128 | 0.3226 | 0.7911 |
| Logistic Regression | Tuned | 0.7687 | 0.3765 | 0.6809 | 0.4848 | 0.8120 |
| Random Forest | Tuned | 0.8265 | 0.4524 | 0.4043 | 0.4270 | 0.7837 |

Tuned Logistic Regression achieved the highest recall, F1-score, and ROC-AUC among the six model versions shown above. Baseline XGBoost achieved the highest accuracy and precision.

## 6. Project Structure

```text
Employee-Attrition-Prediction/
├── data/
├── docs/
├── models/
├── notebooks/
├── reports/
├── src/
│   ├── api/
│   ├── dashboard/
│   └── models/
├── tests/
├── watson_deployment/
├── requirements.txt
├── requirements-deployment.txt
├── README.md
└── SECURITY_NOTES.md
```

## 7. Installation

Open a terminal in the project root directory.

Create a virtual environment:

```powershell
py -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```powershell
py -m pip install -r requirements.txt
```

## 8. Run the Project

### Train the model

From the project root:

```powershell
py .\src\models\train_models.py
```

Run training only when you intend to retrain the model.

### Start the API

From the project root:

```powershell
py -m uvicorn src.api.app:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

The API provides a prediction endpoint at `POST /predict`.

### Start the dashboard

Open another terminal in the project root and run:

```powershell
py -m streamlit run .\src\dashboard\app.py
```

Use the local URL displayed in the terminal to open the dashboard.

## 9. Deployment Status

The local FastAPI application has been started and tested successfully. A sample prediction returned an attrition prediction, an estimated probability, and a risk category.

The `watson_deployment` folder contains a separate copy of the API code, the trained model, model metadata, and deployment requirements.

Deployment to IBM Watson Machine Learning was not completed because IBM Cloud account creation required credit-card verification. Therefore, a live IBM Cloud scoring endpoint is not currently available.

## 10. Responsible Use

Model predictions are estimates and may be incorrect. Predictive relationships do not establish causation. Employee data is sensitive, and predictions should be used only as decision-support information.

The model should not be used as the sole basis for employment decisions. Privacy, fairness, model performance, and potential bias should be evaluated before real-world use.

## 11. Author

Atul Gaikwad

## 12. Disclaimer

This project is intended for educational and research purposes. It is not a validated HR decision-making system.


## Problem Definition and Planning Deliverables

- [Business Problem Statement](docs/Business_Problem_Statement.md)
- [Feature Dictionary](docs/Feature_Dictionary.md)
- [Dataset Report](docs/Dataset_Report.md)
- [Workflow Diagram](docs/Workflow_Diagram.md)
- [Ethics Report](docs/Ethics_Report.md)

## Additional Documentation

- [API Documentation](docs/API_DOCUMENTATION.md)
- [Technical Report](docs/TECHNICAL_REPORT.md)

