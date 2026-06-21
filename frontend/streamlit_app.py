import streamlit as st
import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if project_root not in sys.path:
    sys.path.append(project_root)

from backend.resume_parser import extract_resume_text

from backend.pipeline import run_pipeline
print("Import Success")

def get_recommendation(score):

    if score >= 80:
        return "🟢 Strongly Recommended"

    elif score >= 60:
        return "🟡 Recommended"

    elif score >= 40:
        return "🟠 Consider"

    else:
        return "🔴 Not Recommended"

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)
st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 {
    color: white;
    text-align: center;
}

.metric-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
}

.skill-match {
    background-color: #064e3b;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
}

.skill-missing {
    background-color: #7f1d1d;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1>
 TalentMatch AI
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<center>
<h4>AI Powered Resume Screening & Candidate Ranking System</h4>
</center>
""", unsafe_allow_html=True)

st.markdown(
    """
    Upload a Job Description and Resume
    to evaluate candidate suitability.
    """
)

left,right = st.columns([2,1])

with left:

    job_description = st.text_area(
        "📋 Job Description",
        height=350
    )

with right:

    uploaded_resume = st.file_uploader(
        "📄 Upload Resumes",
        type=["pdf"],
        accept_multiple_files=True
    )

    st.info(
        f"Uploaded: {len(uploaded_resume) if uploaded_resume else 0} resumes"
    )

analyze = st.button(
    " Analyze Candidates",
    use_container_width=True
)

if analyze:
    if not job_description:
        st.error("Please enter a Job Description")

    elif not uploaded_resume:
        st.error("Please upload at least one Resume PDF")

    else:

        results = []

        progress_bar = st.progress(0)

        for i, resume_file in enumerate(uploaded_resume):

            temp_path = f"temp_{resume_file.name}"

            with open(temp_path, "wb") as f:
                f.write(resume_file.getbuffer())

            resume_text = extract_resume_text(
                temp_path
            )

            result = run_pipeline(
                job_description,
                resume_text
            )

            results.append({
                "Resume": resume_file.name,
                "Score": result["Score"],
                "Skill Match %": result["Skill Match %"],
                "Matched Skills": result["Matched Skills"],
                "Missing Skills": result["Missing Skills"],
                "Explanation": result["Explanation"]
            })

        progress_bar.progress(
            (i + 1) / len(uploaded_resume)
        )

        results = sorted(
            results,
            key=lambda x: x["Score"],
            reverse=True
        )

        st.success("Analysis Complete")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Candidates",
                len(results)
            )

        with col2:
            st.metric(
                "Top Score",
                round(
                    max(
                        r["Score"]
                        for r in results
                    ),
                    2
                )
            )

        with col3:
            st.metric(
                "Average Score",
                round(
                    sum(
                        r["Score"]
                        for r in results
                    ) / len(results),
                    2
                )
            )

        import pandas as pd

        leaderboard = pd.DataFrame([
            {
                "Rank": idx + 1,
                "Resume": r["Resume"],
                "Score": round(r["Score"], 2),
                "Skill Match": round(r["Skill Match %"], 2)
            }
            for idx, r in enumerate(results)
        ])

        st.subheader(" Candidate Leaderboard")

        st.dataframe(
            leaderboard,
            use_container_width=True
        )

        csv = leaderboard.to_csv(
            index=False
        )

        st.download_button(
            label="📥 Download Ranking Report",
            data=csv,
            file_name="candidate_ranking.csv",
            mime="text/csv"
        )

        st.subheader(" Candidate Ranking")

        for idx, candidate in enumerate(results, start=1):

            st.markdown(
                f"""
                ## Rank #{idx}
                ### {candidate['Resume']}
                """
            )

            col1,col2 = st.columns(2)

            with col1:
                st.metric(
                    "Candidate Score",
                    f"{candidate['Score']:.2f}%"
                )

            with col2:
                st.metric(
                    "Skill Match",
                    f"{candidate['Skill Match %']:.2f}%"
                )

            st.subheader(
                "Hiring Recommendation"
            )

            st.info(
                get_recommendation(
                    candidate["Score"]
                )
            )

            st.subheader(
                "Skill Coverage"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Required Skills",
                    len(candidate["Matched Skills"])
                    +
                    len(candidate["Missing Skills"])
                )

            with col2:
                st.metric(
                    "Matched Skills",
                    len(candidate["Matched Skills"])
                )

            with col3:
                st.metric(
                    "Missing Skills",
                    len(candidate["Missing Skills"])
                )

            st.write("### Matched Skills")

            for skill in candidate["Matched Skills"]:
                st.markdown(
                    f"""
                    <div class='skill-match'>
                        ✅ {skill}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("### Missing Skills")

            for skill in candidate["Missing Skills"]:
                st.markdown(
                    f"""
                    <div class='skill-missing'>
                        ❌ {skill}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            summary = f"""
            Candidate matched
            {len(candidate['Matched Skills'])}
            out of
            {len(candidate['Matched Skills']) + len(candidate['Missing Skills'])}
            required skills.

            Overall suitability score:
            {candidate['Score']:.2f}%.
            """

            st.subheader(
                "AI Summary"
            )

            st.write(summary)

            with st.expander("View Explanation"):
                st.write(candidate["Explanation"])

            st.divider()
