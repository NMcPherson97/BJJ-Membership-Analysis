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
print(df.head()) 
print(df.info())


current1x_members = df[
    (df['Current_Member'] == True) &
    (df['Membership_Type'] == '1x per week')
].reset_index()
descriptors_1x = current1x_members.describe()

full_members = df[
    (df['Current_Member'] == True) &
    (df['Membership_Type'] == 'Full Access')
].reset_index()
descriptors_full = full_members.describe()

print(descriptors_1x)
print(descriptors_full)