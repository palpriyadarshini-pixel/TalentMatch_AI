from backend.jd_analyzer import create_jd_profile

from backend.ranking_engine import (
    rank_candidate
)

from backend.utils import (
    compare_skills,
    calculate_skill_match_percentage
)

from backend.explainability_engine import (
    create_candidate_report
)


def run_pipeline(
    job_description,
    resume_text,
    candidate_name="Candidate"
):

    jd_profile = create_jd_profile(
        job_description
    )

    score = rank_candidate(
        job_description,
        resume_text
    )

    required_skills = (
        jd_profile["Required_Skills"]
    )

    matched_skills, missing_skills = (
        compare_skills(
            resume_text,
            required_skills
        )
    )

    skill_match = (
        calculate_skill_match_percentage(
            matched_skills,
            required_skills
        )
    )

    report = create_candidate_report(
        candidate_name,
        score,
        matched_skills,
        missing_skills
    )

    report["Skill Match %"] = skill_match

    return report