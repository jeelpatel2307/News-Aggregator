# app.py

from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_news(api_key, country='us', category='general'):
    """
    Get the latest news from a public news API.

    Args:
    - api_key (str): Your API key for the news service.
    - country (str): The country for which news is requested (default: 'us').
    - category (str): The news category (default: 'general').

    Returns:
    - list: List of news articles.
    """
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': country,
        'category': category,
        'apiKey': api_key,
    }
    response = requests.get(base_url, params=params)
    news_data = response.json()

    if 'articles' in news_data:
        return news_data['articles']
    else:
        return []

@app.route('/')
def index():
    # Replace 'YOUR_API_KEY' with a valid News API key
    api_key = 'YOUR_API_KEY'
    
    # Fetch top headlines in the 'general' category for the 'us' country
    news_articles = get_news(api_key)

    return render_template('index.html', news_articles=news_articles)

if __name__ == '__main__':
    app.run(debug=True)






<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News Aggregator</title>
</head>
<body>

    <h1>Top News Headlines</h1>

    <ul>
        {% for article in news_articles %}
            <li>
                <h2>{{ article.title }}</h2>
                <p>{{ article.description }}</p>
                <a href="{{ article.url }}" target="_blank">Read more</a>
            </li>
        {% endfor %}
    </ul>

</body>
</html>
