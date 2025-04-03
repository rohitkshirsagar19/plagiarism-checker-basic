from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import preprocess

def calculate_similarity(text1, text2):
    """
    Calculate similarity % using TF-IDF and cosine similarity
    """
    corpus = [preprocess(text1), preprocess(text2)]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return round(similarity * 100, 2)  # Convert to percentage