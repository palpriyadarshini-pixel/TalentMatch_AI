from jd_analyzer import create_jd_profile

job_description = """
Financial Analyst

Requirements:
Financial Modeling
Budget Forecasting
Risk Analysis
Accounting
Microsoft Excel
Data Analysis
Financial Reporting

Education:
B.Com / MBA Finance

Experience:
2+ years
"""

profile = create_jd_profile(job_description)

print(profile)