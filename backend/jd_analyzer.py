import re
import spacy

nlp = spacy.load("en_core_web_sm")

import re

def extract_skills(job_description):

    skills = []

    match = re.search(
        r"requirements:(.*?)(education:|experience:|$)",
        job_description,
        flags=re.IGNORECASE | re.DOTALL
    )

    if match:

        requirements_text = match.group(1)

        for line in requirements_text.split("\n"):

            line = line.strip()

            if len(line) > 2:

                skills.append(line)

    return skills

def extract_education(job_description):

    education_patterns = [
        r"b\.?tech",
        r"b\.?e",
        r"m\.?tech",
        r"mba",
        r"b\.?com",
        r"m\.?com",
        r"phd",
        r"bachelor",
        r"master"
    ]

    text = job_description.lower()

    education = []

    for pattern in education_patterns:

        matches = re.findall(pattern, text)

        education.extend(matches)

    return list(set(education))

def extract_experience(job_description):

    pattern = r"\d+\+?\s*years?"

    matches = re.findall(
        pattern,
        job_description.lower()
    )

    return matches

def create_jd_profile(job_description):

    return {

        "Required_Skills":
            extract_skills(job_description),

        "Education":
            extract_education(job_description),

        "Experience":
            extract_experience(job_description)

    }

