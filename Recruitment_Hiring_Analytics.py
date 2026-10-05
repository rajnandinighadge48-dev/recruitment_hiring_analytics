import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================================================
# PROJECT 2: RECRUITMENT & HIRING ANALYTICS
# Python Analysis
# =========================================================

# 1. LOAD DATASET
file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Dataset",
    "Recruitment_Hiring_Data_FINAL_60.csv"
)

df = pd.read_csv(file_path)

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_", regex=False)
    .str.replace("-", "_", regex=False)
)

# Convert date column
df["Application_Date"] = pd.to_datetime(
    df["Application_Date"],
    errors="coerce"
)

# Convert numeric columns
numeric_columns = [
    "Experience_Years",
    "Time_to_Hire_Days",
    "Hiring_Cost",
    "Salary_Offered"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# 2. BASIC RECRUITMENT METRICS
total_candidates = len(df)

shortlisted = df["Screening_Status"].eq(
    "Shortlisted"
).sum()

interviewed = df["Interview_Status"].ne(
    "Not Conducted"
).sum()

selected = df["Selection_Status"].eq(
    "Selected"
).sum()

joined = df["Joining_Status"].eq(
    "Joined"
).sum()

avg_time_to_hire = df.loc[
    df["Time_to_Hire_Days"] > 0,
    "Time_to_Hire_Days"
].mean()

total_hiring_cost = df["Hiring_Cost"].sum()

avg_salary = df["Salary_Offered"].mean()

screening_conversion = (
    shortlisted / total_candidates * 100
)

interview_to_selection = (
    selected / interviewed * 100
)

selection_to_joining = (
    joined / selected * 100
)

# 3. PROFESSIONAL SUMMARY
print("\n" + "=" * 55)
print("       RECRUITMENT & HIRING ANALYTICS")
print("=" * 55)

print(
    f"Total Candidates              : {total_candidates}"
)
print(
    f"Shortlisted Candidates        : {shortlisted}"
)
print(
    f"Interviewed Candidates        : {interviewed}"
)
print(
    f"Selected Candidates           : {selected}"
)
print(
    f"Joined Candidates             : {joined}"
)

print(
    f"\nScreening Conversion Rate     : "
    f"{screening_conversion:.2f}%"
)

print(
    f"Interview-to-Selection Rate   : "
    f"{interview_to_selection:.2f}%"
)

print(
    f"Selection-to-Joining Rate     : "
    f"{selection_to_joining:.2f}%"
)

print(
    f"\nAverage Time to Hire          : "
    f"{avg_time_to_hire:.2f} days"
)

print(
    f"Total Hiring Cost             : "
    f"₹{total_hiring_cost:,.2f}"
)

print(
    f"Average Salary Offered        : "
    f"₹{avg_salary:,.2f}"
)

print("=" * 55)

# 4. SOURCE-WISE ANALYSIS
source_analysis = (
    df.groupby("Source")
    .agg(
        Candidates=("Candidate_ID", "count"),
        Selected=(
            "Selection_Status",
            lambda x: (x == "Selected").sum()
        ),
        Joined=(
            "Joining_Status",
            lambda x: (x == "Joined").sum()
        )
    )
    .reset_index()
)

source_analysis[
    "Selection_Rate_Percent"
] = (
    source_analysis["Selected"]
    / source_analysis["Candidates"]
    * 100
).round(2)

source_analysis[
    "Joining_Rate_Percent"
] = (
    source_analysis["Joined"]
    / source_analysis["Candidates"]
    * 100
).round(2)

print("\nSOURCE-WISE ANALYSIS")
print(
    source_analysis.to_string(index=False)
)

# 5. DEPARTMENT-WISE ANALYSIS
department_analysis = (
    df.groupby("Department")
    .agg(
        Candidates=("Candidate_ID", "count"),
        Selected=(
            "Selection_Status",
            lambda x: (x == "Selected").sum()
        ),
        Joined=(
            "Joining_Status",
            lambda x: (x == "Joined").sum()
        ),
        Average_Salary=(
            "Salary_Offered",
            "mean"
        )
    )
    .reset_index()
)

department_analysis[
    "Selection_Rate_Percent"
] = (
    department_analysis["Selected"]
    / department_analysis["Candidates"]
    * 100
).round(2)

department_analysis[
    "Joining_Rate_Percent"
] = (
    department_analysis["Joined"]
    / department_analysis["Candidates"]
    * 100
).round(2)

department_analysis[
    "Average_Salary"
] = (
    department_analysis["Average_Salary"]
    .round(2)
)

print("\nDEPARTMENT-WISE ANALYSIS")
print(
    department_analysis.to_string(index=False)
)

# 6. JOB ROLE ANALYSIS
job_role_analysis = (
    df.groupby("Job_Role")
    .agg(
        Candidates=("Candidate_ID", "count"),
        Selected=(
            "Selection_Status",
            lambda x: (x == "Selected").sum()
        ),
        Joined=(
            "Joining_Status",
            lambda x: (x == "Joined").sum()
        ),
        Average_Salary=(
            "Salary_Offered",
            "mean"
        )
    )
    .reset_index()
)

job_role_analysis[
    "Average_Salary"
] = (
    job_role_analysis["Average_Salary"]
    .round(2)
)

print("\nJOB ROLE ANALYSIS")
print(
    job_role_analysis.to_string(index=False)
)

# 7. HIRING TIME ANALYSIS
hiring_time = df.loc[
    df["Time_to_Hire_Days"] > 0,
    "Time_to_Hire_Days"
]

print("\nHIRING TIME ANALYSIS")

print(
    f"Average Time to Hire : "
    f"{hiring_time.mean():.2f} days"
)

print(
    f"Minimum Time to Hire : "
    f"{hiring_time.min()} days"
)

print(
    f"Maximum Time to Hire : "
    f"{hiring_time.max()} days"
)

# 8. SALARY ANALYSIS
print("\nSALARY ANALYSIS")

print(
    f"Average Salary : "
    f"₹{df['Salary_Offered'].mean():,.2f}"
)

print(
    f"Minimum Salary : "
    f"₹{df['Salary_Offered'].min():,.2f}"
)

print(
    f"Maximum Salary : "
    f"₹{df['Salary_Offered'].max():,.2f}"
)

# 9. EXPERIENCE ANALYSIS
print("\nEXPERIENCE ANALYSIS")

print(
    f"Average Experience : "
    f"{df['Experience_Years'].mean():.2f} years"
)

print(
    f"Minimum Experience : "
    f"{df['Experience_Years'].min():.1f} years"
)

print(
    f"Maximum Experience : "
    f"{df['Experience_Years'].max():.1f} years"
)

# 10. MONTHLY RECRUITMENT TREND
monthly_analysis = (
    df.groupby(
        df["Application_Date"].dt.to_period("M")
    )
    .agg(
        Applications=("Candidate_ID", "count"),
        Selected=(
            "Selection_Status",
            lambda x: (x == "Selected").sum()
        ),
        Joined=(
            "Joining_Status",
            lambda x: (x == "Joined").sum()
        )
    )
    .reset_index()
)

monthly_analysis[
    "Application_Month"
] = (
    monthly_analysis["Application_Date"]
    .astype(str)
)

print("\nMONTHLY RECRUITMENT TREND")

print(
    monthly_analysis[
        [
            "Application_Month",
            "Applications",
            "Selected",
            "Joined"
        ]
    ].to_string(index=False)
)

# 11. CHART 1 — RECRUITMENT FUNNEL
funnel_stages = [
    "Applications",
    "Shortlisted",
    "Interviewed",
    "Selected",
    "Joined"
]

funnel_values = [
    total_candidates,
    shortlisted,
    interviewed,
    selected,
    joined
]

plt.figure(figsize=(9, 5))

plt.bar(
    funnel_stages,
    funnel_values
)

plt.title(
    "Recruitment Funnel",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Recruitment Stage")
plt.ylabel("Number of Candidates")

plt.tight_layout()
plt.show()

# 12. CHART 2 — CANDIDATES BY RECRUITMENT SOURCE
source_chart = source_analysis.sort_values(
    "Candidates",
    ascending=True
)

plt.figure(figsize=(9, 5))

plt.barh(
    source_chart["Source"],
    source_chart["Candidates"]
)

plt.title(
    "Candidates by Recruitment Source",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Number of Candidates")
plt.ylabel("Recruitment Source")

plt.tight_layout()
plt.show()

# 13. FINAL MESSAGE
print("\n" + "=" * 55)
print(
    "Python HR Analytics Analysis "
    "Completed Successfully"
)
print("=" * 55)