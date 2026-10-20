# Employee Attrition Analytics Platform
## Technical Report

## 1. Introduction

Employee attrition occurs when employees leave an organization. High attrition can increase recruitment and training costs and cause organizations to lose experienced employees. This project uses machine learning to analyze employee data and predict possible attrition.

The project includes model comparison, a saved prediction model, a REST API, and a dashboard for exploring attrition information.

## 2. Objectives

- Build a machine learning system to predict employee attrition.
- Compare different classification algorithms.
- Evaluate models using accuracy, precision, recall, F1-score, and ROC-AUC.
- Provide predictions through a REST API.
- Display attrition information through a dashboard.
- Document deployment preparation and project limitations.

## 3. Dataset

The project uses the IBM HR Analytics Employee Attrition dataset.

- Records: 1,470
- Original columns: 35
- Target variable: `Attrition`
- Classes: `Yes` and `No`
- Training records: 1,176
- Testing records: 294

The dataset contains employee demographics, job details, satisfaction ratings, compensation information, and employment history.

## 4. Data Preparation

The training workflow removes `EmployeeCount`, `EmployeeNumber`, `Over18`, and `StandardHours`. The target is encoded as `No = 0` and `Yes = 1`.

The data is divided into training and testing sets using an 80/20 stratified split with `random_state=42`. Numerical features use median imputation and standard scaling. Categorical features use most-frequent imputation and one-hot encoding.

## 5. Machine Learning Models

The advanced training workflow compares four models:

1. Logistic Regression
2. Neural Network using an MLP classifier
3. Gaussian Naive Bayes
4. Linear Discriminant Analysis

A separate evaluation workflow compares Logistic Regression, Decision Tree, Random Forest, and XGBoost, including tuned versions of Logistic Regression and Random Forest.

## 6. Advanced Model Comparison Results

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.7517 | 0.3488 | 0.6383 | 0.4511 | 0.8032 |
| Linear Discriminant Analysis | 0.8639 | 0.6207 | 0.3830 | 0.4737 | 0.7971 |
| Neural Network | 0.8605 | 0.6250 | 0.3191 | 0.4225 | 0.7915 |
| Naive Bayes | 0.6463 | 0.2605 | 0.6596 | 0.3735 | 0.7032 |

Logistic Regression was selected by the current training script because it achieved the highest ROC-AUC among these four models.

## 7. Separate Evaluation Experiment

The separate evaluation report compared six model versions. Tuned Logistic Regression achieved an accuracy of 0.7687, precision of 0.3765, recall of 0.6809, F1-score of 0.4848, and ROC-AUC of 0.8120.

Baseline XGBoost achieved the highest accuracy (0.8571) and precision (0.6667) in that experiment. These results belong to a separate workflow and should not be treated as the metrics of the model currently saved for the API.

## 8. Model Deployment and API

The saved model is stored at `models/best_attrition_model.joblib`. Model information is stored in `models/model_metadata.json`.

A FastAPI application provides these endpoints:

- `GET /`: API status
- `GET /health`: health check
- `POST /predict`: employee attrition prediction
- `GET /docs`: interactive API documentation

The prediction response contains the predicted attrition class, probability, risk category, classification threshold, and a responsible-use note.

The API has been tested locally. IBM Watson Machine Learning cloud deployment was not completed because creating the cloud account required credit-card verification. A live cloud endpoint and automated cloud deployment workflow have not been verified.

## 9. Dashboard

The Streamlit dashboard provides a user interface for exploring attrition information, viewing summary metrics and charts, comparing model results, and submitting employee details for a prediction.

## 10. Limitations

- The dataset may not represent all organizations or employee populations.
- The dataset contains fewer attrition cases than non-attrition cases.
- Predictions can produce false positives and false negatives.
- Model results depend on the dataset, training process, and classification threshold.
- Feature importance and model coefficients show associations, not proof of causation.
- A live cloud deployment and automated retraining workflow have not been completed or verified.

## 11. Responsible Use

The model should support investigation and voluntary retention activities, not replace human judgment. Predictions must not be the sole basis for hiring, firing, promotion, or other employment decisions. Any real-world use requires privacy protection, fairness checks, and ongoing performance monitoring.

## 12. Conclusion

The project demonstrates an end-to-end local employee attrition analytics workflow, including data preparation, model comparison, model saving, API predictions, and dashboard-based analysis.

Logistic Regression was selected in the advanced workflow based on ROC-AUC. A separate experiment reported stronger ROC-AUC for tuned Logistic Regression. The results show that model selection depends on the metric and business objective. Further validation, fairness evaluation, and cloud deployment work are required before operational use.
