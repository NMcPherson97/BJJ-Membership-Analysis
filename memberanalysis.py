import pyodbc
import pandas as pd


conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=BJJMEMBERS;"
    "Trusted_Connection=yes;"
)

query = """
SELECT *
FROM member_analysis
"""
df = pd.read_sql(query, conn)
df.to_csv('members.csv', index=False)

#KPI 1: Average membership duration 1x per week vs full
avg_members_dur = df.groupby('Membership_Type')['Membership_Duration_Days'].mean()
kpi_table = avg_members_dur.round(2).reset_index()

# KPI 2: Churn rate 1x per week vs full access
cancelled_1x = len(df[
    (df['Current_Member'] == False) &
    (df['Membership_Type'] == '1x per week')
])
total_1x = len(df[df['Membership_Type'] == '1x per week'])
churn_1x = cancelled_1x / total_1x

cancelled_full = len(df[
        (df['Current_Member'] == False) &
        (df['Membership_Type'] == 'Full Access')
    ])
total_full = len(df[df['Membership_Type'] == 'Full Access'])
churn_full = cancelled_full / total_full

kpi_table['Churn Rate'] = [f'{churn_1x:.2%}', f'{churn_full: .2%}']

# KPI 3: Membership LTV
df['Membership_Duration_Months'] = (
    df['Membership_Duration_Days'] / 30
).round(2)

df['LTV'] = (df['Monthly_Dues'] * df['Membership_Duration_Months']).round(2)

ltv_table = (
    df.groupby('Membership_Type')['LTV']
      .mean()
      .round(2)
      .reset_index())

kpi_table = kpi_table.merge(
    ltv_table,
    on='Membership_Type',
    how='left')

# KPI 4: Hold metrics
avg_hold_days = (
    df.groupby('Membership_Type')
    ['Hold_Duration_Days'].mean().round(2).reset_index())

kpi_table = kpi_table.merge(
    avg_hold_days,
    on='Membership_Type',
    how='left').drop_duplicates().dropna().reset_index()

kpi_table.to_csv('kpi_summary.csv', index=False)