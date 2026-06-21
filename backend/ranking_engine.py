from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def create_embedding(text):

    embedding = model.encode([text])

    return embedding

def calculate_similarity(
    jd_embedding,
    resume_embedding
):

    similarity = cosine_similarity(
        jd_embedding,
        resume_embedding
    )[0][0]

    return float(round(similarity * 100, 2))

def rank_candidate(
    job_description,
    resume_text
):

    jd_embedding = create_embedding(
        job_description
    )

    resume_embedding = create_embedding(
        resume_text
    )

    score = calculate_similarity(
        jd_embedding,
        resume_embedding
    )

    return score

