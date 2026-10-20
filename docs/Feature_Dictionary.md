# Employee Attrition Feature Dictionary

## 1. Dataset Overview

The dataset contains 35 columns describing employee demographics, job information, compensation, satisfaction, and work experience. The target variable is `Attrition`.

- **Target variable:** `Attrition`
- **Target values:** `Yes` and `No`
- **Prediction task:** Binary classification
- **Dataset file:** `data/WA_Fn-UseC_-HR-Employee-Attrition.csv`

## 2. Feature Dictionary

| No. | Feature | Description | Data Type |
|---:|---|---|---|
| 1 | Age | Employee's age in years | Integer |
| 2 | Attrition | Indicates whether the employee left the organization | Categorical (Target) |
| 3 | BusinessTravel | Frequency or category of business travel | Categorical |
| 4 | DailyRate | Employee's daily rate value | Integer |
| 5 | Department | Department in which the employee works | Categorical |
| 6 | DistanceFromHome | Distance between home and workplace | Integer |
| 7 | Education | Employee's education level, represented numerically | Ordinal integer |
| 8 | EducationField | Employee's field of education | Categorical |
| 9 | EmployeeCount | Employee count field in the dataset | Integer |
| 10 | EmployeeNumber | Employee identification number | Integer (Identifier) |
| 11 | EnvironmentSatisfaction | Employee's satisfaction with the work environment | Ordinal integer |
| 12 | Gender | Employee's gender category | Categorical |
| 13 | HourlyRate | Employee's hourly rate value | Integer |
| 14 | JobInvolvement | Employee's level of job involvement | Ordinal integer |
| 15 | JobLevel | Employee's job level | Ordinal integer |
| 16 | JobRole | Employee's job role | Categorical |
| 17 | JobSatisfaction | Employee's job satisfaction level | Ordinal integer |
| 18 | MaritalStatus | Employee's marital status category | Categorical |
| 19 | MonthlyIncome | Employee's monthly income | Integer |
| 20 | MonthlyRate | Employee's monthly rate value | Integer |
| 21 | NumCompaniesWorked | Number of companies the employee has worked for | Integer |
| 22 | Over18 | Indicates whether the employee is over 18 | Categorical |
| 23 | OverTime | Indicates whether the employee works overtime | Categorical |
| 24 | PercentSalaryHike | Percentage increase in salary | Integer |
| 25 | PerformanceRating | Employee's performance rating | Ordinal integer |
| 26 | RelationshipSatisfaction | Satisfaction with workplace relationships | Ordinal integer |
| 27 | StandardHours | Standard working-hours field in the dataset | Integer |
| 28 | StockOptionLevel | Employee's stock option level | Ordinal integer |
| 29 | TotalWorkingYears | Total years of work experience | Integer |
| 30 | TrainingTimesLastYear | Number of training sessions in the previous year | Integer |
| 31 | WorkLifeBalance | Employee's work-life balance rating | Ordinal integer |
| 32 | YearsAtCompany | Years the employee has worked at the company | Integer |
| 33 | YearsInCurrentRole | Years spent in the current role | Integer |
| 34 | YearsSinceLastPromotion | Years since the last promotion | Integer |
| 35 | YearsWithCurrManager | Years working with the current manager | Integer |

## 3. Target Variable

The target variable is `Attrition`.

- `Yes`: The employee left the organization.
- `No`: The employee stayed with the organization.

The machine learning model uses the other selected features to predict the target variable.

## 4. Feature Categories

### Demographic Features
Age, Gender, MaritalStatus, Education, and EducationField.

### Job and Department Features
Department, JobRole, JobLevel, JobInvolvement, and BusinessTravel.

### Compensation Features
DailyRate, HourlyRate, MonthlyIncome, MonthlyRate, PercentSalaryHike, and StockOptionLevel.

### Satisfaction and Workplace Features
EnvironmentSatisfaction, JobSatisfaction, RelationshipSatisfaction, WorkLifeBalance, and OverTime.

### Experience and Career Features
NumCompaniesWorked, TotalWorkingYears, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager, TrainingTimesLastYear, and PerformanceRating.

### Administrative Features
EmployeeCount, EmployeeNumber, Over18, and StandardHours.

## 5. Data Preparation Notes

The existing training workflow removes `EmployeeCount`, `EmployeeNumber`, `Over18`, and `StandardHours` before model training. These fields are excluded because they are administrative, identifiers, or do not provide useful variation for the prediction task in this dataset.

The training workflow treats numerical and categorical features separately. Numerical features use median imputation and scaling, while categorical features use most-frequent imputation and one-hot encoding.

## 6. Conclusion

The feature dictionary explains the meaning and type of each column in the employee attrition dataset. It helps understand the data before exploratory data analysis and machine learning. Correct identification of the target variable and feature types supports suitable data preprocessing and model development.