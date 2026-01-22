import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity


# Step 1: Train Word2Vec model
def train_word2vec(sentences, vector_size=100, window=5):
    model = Word2Vec(
        sentences=sentences,
        vector_size=vector_size,
        window=window,
        min_count=1,
        workers=4
    )
    return model


# Step 2: Convert sentence (tokens) into vector
def get_sentence_vector(tokens, model):
    vectors = [model.wv[word] for word in tokens if word in model.wv]

    if len(vectors) == 0:
        return np.zeros(model.vector_size)

    return np.mean(vectors, axis=0)


# Step 3: Calculate match score
def calculate_match_score(resume_tokens, jd_tokens):
    model = train_word2vec([resume_tokens, jd_tokens])

    resume_vec = get_sentence_vector(resume_tokens, model)
    jd_vec = get_sentence_vector(jd_tokens, model)

    similarity = cosine_similarity(
        resume_vec.reshape(1, -1),
        jd_vec.reshape(1, -1)
    )[0][0]

    return round(similarity * 100, 2)


# Step 4: Recommendation based on score
def get_recommendation(score):
    if score >= 80:
        return "Good Match"
    elif score >= 50:
        return "Average Match"
    else:
        return "Poor Match"

