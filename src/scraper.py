from google_play_scraper import reviews, Sort
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

APPS = [
    {"bank": "Commercial Bank of Ethiopia", "app_id": "com.combanketh.mobilebanking"},
    {"bank": "Bank of Abyssinia", "app_id": "com.boa.boaMobileBanking"},
    {"bank": "Dashen Bank", "app_id": "com.dashen.dashensuperapp"},
]

def scrape_reviews(app_id, bank_name, count=500):
    """Scrape reviews from Google Play Store with error handling"""
    try:
        logger.info(f"Scraping reviews for {bank_name}...")
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
        logger.info(f"Successfully scraped {len(data)} reviews for {bank_name}")
        return pd.DataFrame(data)
    except Exception as e:
        logger.error(f"Error scraping {bank_name}: {e}")
        return pd.DataFrame()

def clean_reviews(df):
    """Clean and preprocess reviews with error handling"""
    try:
        original_len = len(df)
        df = df.drop_duplicates()
        df = df.dropna(subset=['review', 'rating'])
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date'])
        logger.info(f"Cleaned data: {original_len} -> {len(df)} reviews")
        return df
    except Exception as e:
        logger.error(f"Error cleaning data: {e}")
        return df

def scrape_all_banks():
    """Scrape all banks and return combined dataframe"""
    all_reviews = []
    for app in APPS:
        try:
            df = scrape_reviews(app['app_id'], app['bank'])
            if not df.empty:
                all_reviews.append(df)
        except Exception as e:
            logger.error(f"Failed to scrape {app['bank']}: {e}")
    return pd.concat(all_reviews, ignore_index=True) if all_reviews else pd.DataFrame()