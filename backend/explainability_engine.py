def generate_explanation(
    score,
    matched_skills,
    missing_skills
):

    explanation = f"""

Candidate Score: {score}

Matched Skills:
{', '.join(matched_skills)}

Missing Skills:
{', '.join(missing_skills)}

Reason:

The candidate demonstrates alignment with the job requirements based on semantic similarity and skill overlap.

"""

    return explanation

def create_candidate_report(
    candidate_name,
    score,
    matched_skills,
    missing_skills
):

    return {

        "Candidate": candidate_name,

        "Score": score,

        "Matched Skills": matched_skills,

        "Missing Skills": missing_skills,

        "Explanation":
            generate_explanation(
                score,
                matched_skills,
                missing_skills
            )

    }

