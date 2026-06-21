from pipeline import run_pipeline

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

resume_text = """
Financial Analyst with experience in:

Financial Modeling
Risk Analysis
Accounting
Financial Reporting

Strong communication and analytical skills.
"""

report = run_pipeline(

    job_description,

    resume_text,

    candidate_name="John Doe"

)

print(report)