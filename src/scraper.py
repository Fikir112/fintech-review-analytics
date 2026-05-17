from google_play_scraper import reviews, Sort
import pandas as pd

def scrape_reviews(app_id, bank_name, count=500):
    result, _ = reviews(
        app_id,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=count
    )
    data = [{
        'review': r['content'],
        'rating': r['score'],
        'date': r['at'].strftime('%Y-%m-%d'),
        'bank': bank_name,
        'source': 'Google Play'
    } for r in result]
    return pd.DataFrame(data)

def clean_reviews(df):
    df = df.drop_duplicates()
    df = df.dropna(subset=['review', 'rating'])
    df['date'] = pd.to_datetime(df['date'])
    return df