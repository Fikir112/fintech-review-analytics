from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import spacy

# Load English language model
nlp = spacy.load('en_core_web_sm')

# Theme keywords dictionary
THEMES = {
    'Login & Authentication': ['login', 'password', 'otp', 'sign in', 'fingerprint', 'access', 'verification'],
    'Transfer & Payments': ['transfer', 'send money', 'payment', 'transaction', 'failed', 'money', 'deposit'],
    'App Performance': ['crash', 'slow', 'bug', 'error', 'freeze', 'update', 'loading', 'fix'],
    'UI & Design': ['interface', 'design', 'easy', 'user friendly', 'navigation', 'simple', 'beautiful'],
    'Customer Service': ['support', 'service', 'help', 'response', 'agent', 'call', 'contact'],
    'Account Management': ['account', 'balance', 'statement', 'block', 'suspend', 'limit'],
}

def assign_theme(review):
    """Assign a theme to a review based on keywords"""
    try:
        review_lower = str(review).lower()
        for theme, keywords in THEMES.items():
            for keyword in keywords:
                if keyword in review_lower:
                    return theme
        return 'General'
    except Exception as e:
        return 'General'

def get_tfidf_keywords(texts, n_keywords=10):
    """Extract top keywords using TF-IDF"""
    try:
        vectorizer = TfidfVectorizer(
            max_features=500,
            stop_words='english',
            ngram_range=(1, 2)
        )
        tfidf_matrix = vectorizer.fit_transform(texts)
        feature_names = vectorizer.get_feature_names_out()
        scores = tfidf_matrix.mean(axis=0).A1
        top_indices = scores.argsort()[-n_keywords:][::-1]
        return [feature_names[i] for i in top_indices]
    except Exception as e:
        return []

def extract_keywords_per_bank(df):
    """Get top TF-IDF keywords for each bank"""
    try:
        results = {}
        for bank in df['bank'].unique():
            bank_reviews = df[df['bank'] == bank]['review'].tolist()
            keywords = get_tfidf_keywords(bank_reviews)
            results[bank] = keywords
        return results
    except Exception as e:
        return {}