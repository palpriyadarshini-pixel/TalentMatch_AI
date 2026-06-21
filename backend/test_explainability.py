from explainability_engine import (
    create_candidate_report
)

report = create_candidate_report(

    candidate_name="Candidate_01",

    score=82.5,

    matched_skills=[
        "Financial Modeling",
        "Accounting",
        "Risk Analysis"
    ],

    missing_skills=[
        "Microsoft Excel"
    ]

)

print(report)