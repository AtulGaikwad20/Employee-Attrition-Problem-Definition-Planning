# Employee Attrition Dataset Report

## 1. Introduction

This report presents the exploratory data analysis (EDA) of the employee attrition dataset. The analysis examines dataset structure, missing values, duplicate records, target distribution, feature distributions, and numerical correlations with attrition.

**Dataset file:** `data/WA_Fn-UseC_-HR-Employee-Attrition.csv`

## 2. Dataset Overview

| Item | Result |
|---|---:|
| Total records | 1,470 |
| Total columns | 35 |
| Duplicate rows | 0 |
| Missing values | 0 |
| Target variable | Attrition |
| Problem type | Binary classification |

The dataset contains employee demographic information, job details, compensation, satisfaction ratings, and work experience.

## 3. Missing Values and Duplicate Records

The analysis found no missing values in any column. No duplicate rows were found.

Therefore, no missing-value removal was required for this initial EDA. Data preprocessing may still be needed for future data and model pipelines.

## 4. Attrition Distribution

| Attrition | Employees | Percentage |
|---|---:|---:|
| No | 1,233 | 83.88% |
| Yes | 237 | 16.12% |
| Total | 1,470 | 100% |

Most employees in the dataset stayed with the organization. Approximately 16.12% left.

This imbalance should be considered when evaluating machine learning models. Accuracy should be assessed together with precision, recall, F1-score, and ROC-AUC.

## 5. Feature Distribution Analysis

### 5.1 Business Travel

| Category | Employees |
|---|---:|
| Travel_Rarely | 1,043 |
| Travel_Frequently | 277 |
| Non-Travel | 150 |

Travel_Rarely is the most common category in the dataset.

### 5.2 Department

| Department | Employees |
|---|---:|
| Research & Development | 961 |
| Sales | 446 |
| Human Resources | 63 |

Research & Development has the largest number of records, while Human Resources has the smallest.

### 5.3 Education Field

| Education Field | Employees |
|---|---:|
| Life Sciences | 606 |
| Medical | 464 |
| Marketing | 159 |
| Technical Degree | 132 |
| Other | 82 |
| Human Resources | 27 |

Life Sciences is the most frequently recorded education field.

### 5.4 Gender

| Gender | Employees |
|---|---:|
| Male | 882 |
| Female | 588 |

The dataset contains more male records than female records. This difference should be considered when checking model fairness.

### 5.5 Job Role

| Job Role | Employees |
|---|---:|
| Sales Executive | 326 |
| Research Scientist | 292 |
| Laboratory Technician | 259 |
| Manufacturing Director | 145 |
| Healthcare Representative | 131 |
| Manager | 102 |
| Sales Representative | 83 |
| Research Director | 80 |
| Human Resources | 52 |

Sales Executive is the most common job role in the dataset.

### 5.6 Marital Status

| Marital Status | Employees |
|---|---:|
| Married | 673 |
| Single | 470 |
| Divorced | 327 |

Married is the most common marital-status category.

### 5.7 Overtime

| Overtime | Employees |
|---|---:|
| No | 1,054 |
| Yes | 416 |

Most employees are recorded as not working overtime. Overtime may be investigated further when studying attrition, but these counts alone do not establish whether overtime causes employees to leave.

## 6. Numerical Feature Summary

| Feature | Mean | Minimum | Maximum |
|---|---:|---:|---:|
| Age | 36.92 | 18 | 60 |
| DistanceFromHome | 9.19 | 1 | 29 |
| MonthlyIncome | 6,502.93 | 1,009 | 19,999 |
| TotalWorkingYears | 11.28 | 0 | 40 |
| YearsAtCompany | 7.01 | 0 | 40 |
| JobSatisfaction | 2.73 | 1 | 4 |
| WorkLifeBalance | 2.76 | 1 | 4 |
| TrainingTimesLastYear | 2.80 | 0 | 6 |

These statistics describe the numerical fields in the dataset. Satisfaction and work-life balance are represented using rating values, so their averages should be interpreted in the context of the rating scales.

## 7. Numerical Correlation with Attrition

For this analysis, Attrition was encoded as No = 0 and Yes = 1. Pearson correlations were calculated between the numerical columns and this encoded target.

| Feature | Correlation |
|---|---:|
| TotalWorkingYears | -0.171 |
| JobLevel | -0.169 |
| YearsInCurrentRole | -0.161 |
| MonthlyIncome | -0.160 |
| Age | -0.159 |
| YearsWithCurrManager | -0.156 |
| StockOptionLevel | -0.137 |
| YearsAtCompany | -0.134 |
| JobInvolvement | -0.130 |
| JobSatisfaction | -0.103 |
| EnvironmentSatisfaction | -0.103 |
| DistanceFromHome | 0.078 |
| NumCompaniesWorked | 0.043 |

The strongest negative correlations among these numerical features include TotalWorkingYears, JobLevel, YearsInCurrentRole, MonthlyIncome, and Age. DistanceFromHome and NumCompaniesWorked have small positive correlations with the encoded target.

These are simple numerical associations, not proof of cause and effect. Correlation also does