from utils import (
    compare_skills,
    calculate_skill_match_percentage
)

required_skills = [

    "Financial Modeling",
    "Accounting",
    "Risk Analysis",
    "Microsoft Excel"

]

candidate_text = """

Experienced Financial Analyst.

Expert in Financial Modeling,
Accounting,
Risk Analysis.

"""

matched, missing = compare_skills(
    candidate_text,
    required_skills
)

print("Matched Skills:")
print(matched)

print()

print("Missing Skills:")
print(missing)

print()

print(
    calculate_skill_match_percentage(
        matched,
        required_skills
    )
)