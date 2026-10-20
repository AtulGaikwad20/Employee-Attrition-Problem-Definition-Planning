
from pathlib import Path

import joblib
import pandas as pd
import plotly.express as px
import streamlit as st


ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
MODEL_PATH = ROOT / "models" / "best_attrition_model.joblib"
COMPARISON_PATH = ROOT / "reports" / "advanced_model_comparison.csv"

st.set_page_config(
    page_title="Employee Attrition Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("Employee Attrition Analytics Platform")
st.caption("Workforce insights, attrition risk, and model performance")

if not DATA_PATH.exists():
    st.error(f"Dataset not found: {DATA_PATH}")
    st.stop()

df = pd.read_csv(DATA_PATH)

if "Attrition" not in df.columns:
    st.error("The dataset does not contain the Attrition column.")
    st.stop()

if "Department" not in df.columns:
    st.error("The dataset does not contain the Department column.")
    st.stop()

st.sidebar.header("Dashboard Filters")

departments = sorted(df["Department"].dropna().unique().tolist())
selected_departments = st.sidebar.multiselect(
    "Department",
    departments,
    default=departments,
)

genders = sorted(df["Gender"].dropna().unique().tolist())
selected_genders = st.sidebar.multiselect(
    "Gender",
    genders,
    default=genders,
)

age_min = int(df["Age"].min())
age_max = int(df["Age"].max())

selected_age = st.sidebar.slider(
    "Age range",
    min_value=age_min,
    max_value=age_max,
    value=(age_min, age_max),
)

filtered = df[
    df["Department"].isin(selected_departments)
    & df["Gender"].isin(selected_genders)
    & df["Age"].between(selected_age[0], selected_age[1])
].copy()

total_employees = len(filtered)
employees_left = int((filtered["Attrition"] == "Yes").sum())
employees_stayed = int((filtered["Attrition"] == "No").sum())
attrition_rate = (
    employees_left / total_employees * 100
    if total_employees
    else 0
)
retention_rate = (
    employees_stayed / total_employees * 100
    if total_employees
    else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Employees", f"{total_employees:,}")
col2.metric("Employees Left", f"{employees_left:,}")
col3.metric("Attrition Rate", f"{attrition_rate:.2f}%")
col4.metric("Retention Rate", f"{retention_rate:.2f}%")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Attrition by Department")

    if not filtered.empty:
        department_data = (
            filtered.groupby("Department")["Attrition"]
            .apply(lambda values: (values == "Yes").sum())
            .reset_index(name="Employees Left")
        )

        figure = px.bar(
            department_data,
            x="Department",
            y="Employees Left",
            color="Department",
            title="Number of Employees Who Left",
        )
        st.plotly_chart(figure, use_container_width=True)
    else:
        st.info("No employees match the selected filters.")

with right:
    st.subheader("Attrition Distribution")

    if not filtered.empty:
        attrition_data = (
            filtered["Attrition"]
            .value_counts()
            .rename_axis("Attrition")
            .reset_index(name="Employees")
        )

        figure = px.pie(
            attrition_data,
            names="Attrition",
            values="Employees",
            hole=0.45,
            title="Employees Who Stayed vs Left",
        )
        st.plotly_chart(figure, use_container_width=True)
    else:
        st.info("No employees match the selected filters.")

left, right = st.columns(2)

with left:
    st.subheader("Workforce Age Distribution")

    if not filtered.empty:
        figure = px.histogram(
            filtered,
            x="Age",
            color="Attrition",
            nbins=20,
            barmode="overlay",
            title="Employee Age and Attrition",
        )
        st.plotly_chart(figure, use_container_width=True)

with right:
    st.subheader("Monthly Income by Attrition")

    if not filtered.empty:
        figure = px.box(
            filtered,
            x="Attrition",
            y="MonthlyIncome",
            color="Attrition",
            title="Monthly Income Comparison",
        )
        st.plotly_chart(figure, use_container_width=True)

st.divider()

st.subheader("Employee Attrition Risk Prediction")

if not MODEL_PATH.exists():
    st.warning(
        "The trained model was not found. Run src/models/train_models.py first."
    )
else:
    model = joblib.load(MODEL_PATH)

    numeric_columns = [
        "Age",
        "DailyRate",
        "DistanceFromHome",
        "Education",
        "EnvironmentSatisfaction",
        "HourlyRate",
        "JobInvolvement",
        "JobLevel",
        "JobSatisfaction",
        "MonthlyIncome",
        "MonthlyRate",
        "NumCompaniesWorked",
        "PercentSalaryHike",
        "PerformanceRating",
        "RelationshipSatisfaction",
        "StockOptionLevel",
        "TotalWorkingYears",
        "TrainingTimesLastYear",
        "WorkLifeBalance",
        "YearsAtCompany",
        "YearsInCurrentRole",
        "YearsSinceLastPromotion",
        "YearsWithCurrManager",
    ]

    categorical_columns = [
        "BusinessTravel",
        "Department",
        "EducationField",
        "Gender",
        "JobRole",
        "MaritalStatus",
        "OverTime",
    ]

    with st.form("prediction_form"):
        st.write("Enter employee details to estimate attrition probability.")

        values = {}

        for column in numeric_columns:
            default_value = int(df[column].median())
            values[column] = st.number_input(
                column,
                value=default_value,
                step=1,
            )

        for column in categorical_columns:
            options = sorted(df[column].dropna().unique().tolist())
            values[column] = st.selectbox(column, options)

        submitted = st.form_submit_button("Predict Attrition Risk")

    if submitted:
        try:
            employee = pd.DataFrame([values])
            probability = float(model.predict_proba(employee)[0, 1])

            prediction = "Yes" if probability >= 0.5 else "No"

            if probability >= 0.60:
                risk = "High"
            elif probability >= 0.30:
                risk = "Medium"
            else:
                risk = "Low"

            result1, result2, result3 = st.columns(3)
            result1.metric("Predicted Attrition", prediction)
            result2.metric("Attrition Probability", f"{probability:.2%}")
            result3.metric("Risk Category", risk)

            st.caption(
                "This prediction is an estimate for decision support, "
                "not a guarantee or a basis for making employment decisions."
            )
        except Exception as exc:
            st.error(f"Prediction failed: {exc}")

st.divider()

st.subheader("Advanced Model Performance")

if COMPARISON_PATH.exists():
    comparison = pd.read_csv(COMPARISON_PATH)
    st.dataframe(comparison, use_container_width=True, hide_index=True)

    if {"model", "roc_auc"}.issubset(comparison.columns):
        figure = px.bar(
            comparison.sort_values("roc_auc", ascending=False),
            x="model",
            y="roc_auc",
            title="Model Comparison by ROC-AUC",
            labels={"model": "Model", "roc_auc": "ROC-AUC"},
        )
        st.plotly_chart(figure, use_container_width=True)
else:
    st.warning("Run the model training script to generate the comparison report.")

st.subheader("Filtered Workforce Data")
st.dataframe(filtered, use_container_width=True, hide_index=True)

csv_data = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Filtered Workforce Data",
    data=csv_data,
    file_name="filtered_employee_workforce.csv",
    mime="text/csv",
)
