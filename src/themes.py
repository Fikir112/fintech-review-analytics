THEMES = {
    'Login & Authentication': ['login', 'password', 'otp', 'sign in', 'fingerprint', 'access'],
    'Transfer & Payments': ['transfer', 'send money', 'payment', 'transaction', 'failed'],
    'App Performance': ['crash', 'slow', 'bug', 'error', 'freeze', 'update'],
    'UI & Design': ['interface', 'design', 'easy', 'user friendly', 'navigation'],
    'Customer Service': ['support', 'service', 'help', 'response', 'agent'],
}

def assign_theme(review):
    review_lower = str(review).lower()
    for theme, keywords in THEMES.items():
        for keyword in keywords:
            if keyword in review_lower:
                return theme
    return 'General'