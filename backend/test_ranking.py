from ranking_engine import rank_candidate

job_description = """
Financial Analyst

Requirements:
Financial Modeling
Budget Forecasting
Risk Analysis
Accounting
Microsoft Excel
"""

resume_text = """
Financial Analyst with experience in
financial reporting,
risk analysis,
budget planning,
accounting,
and advanced excel.
"""

score = rank_candidate(
    job_description,
    resume_text
)

print(score)