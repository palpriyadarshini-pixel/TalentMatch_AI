def compare_skills(
    candidate_text,
    required_skills
):

    candidate_text = candidate_text.lower()

    matched = []

    for skill in required_skills:

        if skill.lower() in candidate_text:

            matched.append(skill)

    missing = list(
        set(required_skills) - set(matched)
    )

    return matched, missing

def calculate_skill_match_percentage(
    matched_skills,
    required_skills
):

    if len(required_skills) == 0:
        return 0

    percentage = (

        len(matched_skills)

        /

        len(required_skills)

    ) * 100

    return round(percentage, 2)