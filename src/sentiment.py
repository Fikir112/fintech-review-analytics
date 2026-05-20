from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging

logger = logging.getLogger(__name__)

def analyze_sentiment(text):
    """Analyze sentiment of a single review with error handling"""
    try:
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(str(text))['compound']
        if score >= 0.05:
            return 'positive', score
        elif score <= -0.05:
            return 'negative', score
        else:
            return 'neutral', score
    except Exception as e:
        logger.error(f"Error analyzing sentiment: {e}")
        return 'neutral', 0.0

def add_sentiment_to_df(df):
    """Add sentiment labels and scores to dataframe with error handling"""
    try:
        results = df['review'].apply(lambda x: analyze_sentiment(x))
        df['sentiment_label'] = results.apply(lambda x: x[0])
        df['sentiment_score'] = results.apply(lambda x: x[1])
        return df
    except Exception as e:
        logger.error(f"Error adding sentiment to dataframe: {e}")
        return df