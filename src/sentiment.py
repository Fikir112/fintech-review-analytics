from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(str(text))['compound']
    if score >= 0.05:
        return 'positive', score
    elif score <= -0.05:
        return 'negative', score
    else:
        return 'neutral', score

def add_sentiment_to_df(df):
    results = df['review'].apply(lambda x: analyze_sentiment(x))
    df['sentiment_label'] = results.apply(lambda x: x[0])
    df['sentiment_score'] = results.apply(lambda x: x[1])
    return df