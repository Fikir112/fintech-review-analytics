# Fintech Review Analytics

## Overview
Customer Experience Analytics for Ethiopian Fintech Apps. This project analyzes Google Play Store reviews for three major Ethiopian banks to deliver actionable insights on user satisfaction, pain points, and feature priorities.

## Banks Analyzed
| Bank | App ID | Reviews Collected |
|------|--------|------------------|
| Commercial Bank of Ethiopia | com.combanketh.mobilebanking | 482 |
| Bank of Abyssinia | com.boa.boaMobileBanking | 498 |
| Dashen Bank | com.dashen.dashensuperapp | 498 |

## Project Structure
fintech-review-analytics/
├── data/
│   └── raw/              # Scraped and cleaned review data (not tracked by Git)
├── notebooks/
│   ├── task1_scraping.ipynb        # Data collection and preprocessing
│   ├── task2_sentiment.ipynb       # Sentiment and thematic analysis
│   ├── task3_database.ipynb        # PostgreSQL database storage
│   └── task4_visualization.ipynb   # Visualizations and insights
├── src/
│   ├── scraper.py        # Production scraping and cleaning functions
│   ├── sentiment.py      # VADER sentiment analysis functions
│   └── themes.py         # TF-IDF and keyword theme analysis
├── tests/                # Unit tests
├── scripts/              # Standalone scripts
├── .github/workflows/    # CI/CD with GitHub Actions
├── requirements.txt      # Python dependencies
└── README.md

## Tasks Completed

### Task 1: Data Collection & Preprocessing
- Tool: google-play-scraper Python library
- Reviews collected: 1,478 (after cleaning from 1,500 raw)
- Duplicates removed: 22
- Missing values: 0
- Columns: review, rating, date, bank, source
- Error handling: try/except with Python logging throughout

### Task 2: Sentiment & Thematic Analysis
- Sentiment tool: VADER (chosen over DistilBERT for speed and suitability)
- Scoring: compound score ≥0.05 = positive, ≤-0.05 = negative, else neutral
- Results: 61.2% positive, 24.7% neutral, 14.1% negative
- Thematic analysis: keyword matching + TF-IDF (scikit-learn) + spaCy NER
- Themes: Login & Auth, Transfer & Payments, App Performance, UI & Design, Customer Service, Account Management

### Task 3: Database Storage
- Database: PostgreSQL 18
- Tables: banks (3 rows) + reviews (1,478 rows)
- Connection: psycopg2
- Design: relational schema with foreign key linking reviews to banks

### Task 4: Visualizations & Insights
- Sentiment distribution by bank
- Average sentiment score by star rating
- Theme distribution by bank
- Top organizations mentioned (spaCy NER)
- TF-IDF keywords per bank

## Key Findings
| Bank | Avg Rating | Positive % | Negative % |
|------|-----------|-----------|-----------|
| CBE | 4.09/5.0 | 66.6% | 10.6% |
| Dashen | 3.92/5.0 | 64.1% | 13.7% |
| BOA | 3.56/5.0 | 53.0% | 18.1% |

## Installation
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Usage
Run notebooks in order:
1. `notebooks/task1_scraping.ipynb`
2. `notebooks/task2_sentiment.ipynb`
3. `notebooks/task3_database.ipynb`
4. `notebooks/task4_visualization.ipynb`

## Limitations
- English reviews only (country='us')
- Maximum 500 reviews per bank due to API limits
- VADER may misclassify financial domain terms
- DistilBERT not used due to GPU requirements

## Author
Fikirte Endeshaw Mihretie
10 Academy KAIM Program — Week 2