# News Aggregator

Welcome to the News Aggregator project! This project provides a simple News Aggregator application using Python with Flask on the server-side and HTML on the client side. It fetches the latest news from a public news API and displays them on a web page.

## Features

- Fetches top headlines from a public news API.
- Displays news articles with titles, descriptions, and links to read more.

## How to Run

1. **Clone the Repository:**
    
    ```bash
    git clone [repository_url]
    
    ```
    
2. **Navigate to the Project Directory:**
    
    ```bash
    cd news-aggregator
    
    ```
    
3. **Install Dependencies:**
    
    ```bash
    pip install Flask requests
    
    ```
    
4. **Replace API Key:**
    - Open the `app.py` file.
    - Replace `'YOUR_API_KEY'` with a valid API key obtained from the News API (https://newsapi.org/).
5. **Run the Server:**
    
    ```bash
    python app.py
    
    ```
    
6. **View Top News:**
    - Open a web browser and go to `http://localhost:5000`.

## Customization

- Explore the News API documentation (https://newsapi.org/docs/endpoints/top-headlines) to customize the `get_news` function for different countries, categories, or sources.
- Add styling to improve the visual appearance of the news aggregator.
- Implement pagination for handling a larger number of news articles.

## Important Note

- Ensure you have a valid API key from the News API. Replace `'YOUR_API_KEY'` with your own API key in the `app.py` file.

## Author

Jeel patel
