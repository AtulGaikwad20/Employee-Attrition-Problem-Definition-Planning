# Employee Attrition Prediction Models
## 1. Objective
The objective of this project is to build and compare machine learning classification models that predict whether an employee is likely to leave an organization.

## 2. Dataset
- Dataset: IBM HR Analytics Employee Attrition dataset
- Total records: 1470
- Original columns: 35
- Target variable: Attrition
- Positive class: Yes (employee leaves)
- Negative class: No (employee stays)
- Training records: 1176
- Testing records: 294

## 3. Data Preparation
- Removed non-informative columns: EmployeeCount, EmployeeNumber, Over18, and StandardHours.
- Encoded the target variable: No = 0 and Yes = 1.
- Applied median imputation and standard scaling to numerical features.
- Applied most-frequent imputation and one-hot encoding to categorical features.
- Used an 80/20 stratified train-test split with random_state=42.

## 4. Models Evaluated
Four baseline classifiers were trained:
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Logistic Regression and Random Forest were also tuned using GridSearchCV with five-fold stratified cross-validation and ROC-AUC scoring.

## 5. Test-Set Results
              Model  Version  Accuracy  Precision  Recall  F1-Score  ROC-AUC
Logistic Regression Baseline    0.7517     0.3488  0.6383    0.4511   0.8032
      Decision Tree Baseline    0.7789     0.3043  0.2979    0.3011   0.5842
      Random Forest Baseline    0.8401     0.5000  0.3404    0.4051   0.7998
            XGBoost Baseline    0.8571     0.6667  0.2128    0.3226   0.7911
Logistic Regression    Tuned    0.7687     0.3765  0.6809    0.4848   0.8120
      Random Forest    Tuned    0.8265     0.4524  0.4043    0.4270   0.7837

## 6. Model Selection
Tuned Logistic Regression achieved the highest recall (0.6809), F1-Score (0.4848), and ROC-AUC (0.8120) among the six evaluated versions.

It is the recommended model when identifying as many potential attrition cases as possible is a priority. Baseline XGBoost achieved the highest accuracy and precision, so it may be more suitable when avoiding false alerts is a greater priority.

## 7. Confusion Matrix Analysis
For tuned Logistic Regression:
- True negatives: 194
- False positives: 53
- False negatives: 15
- True positives: 32

The model identified 32 of the 47 employees who left in the test set. It missed 15 attrition cases and generated 53 false-positive alerts.

## 8. Feature Importance
The tuned Random Forest model ranked these features highest by feature importance:
- Monthly Income
- Age
- Total Working Years
- Daily Rate
- Years at Company
- Distance From Home
- Monthly Rate
- Hourly Rate
- Number of Companies Worked
- Years With Current Manager

Logistic Regression coefficients also highlighted overtime status, job role, business travel, and employment-history features.

Feature importance and coefficients indicate model associations, not proof of causation.

## 9. Limitations
- The dataset is imbalanced, with fewer employees leaving than staying.
- False positives and false negatives both require consideration.
- Results depend on the dataset and the selected classification threshold.
- Feature importance does not establish causal relationships.
- Predictions should support, not replace, fair and responsible HR decisions.

## 10. Conclusion
The experiments show that no single model performs best on every metric. Tuned Logistic Regression is the preferred model for attrition detection based on recall, F1-Score, and ROC-AUC. Baseline XGBoost leads in accuracy and precision. The final model choice should reflect the organization's priorities and the cost of missed attrition cases versus false alerts.
